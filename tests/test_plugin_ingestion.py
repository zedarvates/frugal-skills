"""Exercise package rejection for manifest shapes rejected during ingestion."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]


class PluginIngestionTests(unittest.TestCase):
    def setUp(self):
        self.task_tmp = tempfile.TemporaryDirectory(prefix="frugal-ingestion-")
        self.addCleanup(self.task_tmp.cleanup)
        self.root = Path(self.task_tmp.name) / "package"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(
            ".git", "dist", "__pycache__", "changes.json", "ingestion-fix.json", "review-fix.json"))
        self.manifest_path = self.root / ".codex-plugin/plugin.json"
        self.manifest = json.loads(self.manifest_path.read_text())

    def run_package(self, check=True):
        self.manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")
        args = [sys.executable, str(self.root / "scripts/package_plugin.py")]
        if check:
            args.append("--check")
        return subprocess.run(args, capture_output=True, text=True, timeout=20)

    def assert_rejected(self, field):
        result = self.run_package()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(field, result.stderr)

    def test_missing_capabilities_is_rejected(self):
        del self.manifest["interface"]["capabilities"]
        self.assert_rejected("interface.capabilities")

    def test_capabilities_must_be_a_string_array(self):
        self.manifest["interface"]["capabilities"] = "Context budget"
        self.assert_rejected("interface.capabilities")

    def test_nonstring_capability_is_rejected(self):
        self.manifest["interface"]["capabilities"] = [42]
        self.assert_rejected("interface.capabilities")

    def test_missing_starter_prompt_is_rejected(self):
        del self.manifest["interface"]["defaultPrompt"]
        self.assert_rejected("interface.defaultPrompt")

    def test_single_string_starter_prompt_is_supported(self):
        self.manifest["interface"]["defaultPrompt"] = "Choose a context-budget workflow."
        result = self.run_package()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_aligned_local_cachebuster_is_supported(self):
        version = "1.0.0+codex.local-20261013-184516"
        self.manifest["version"] = version
        path = self.root / "plugin.json"
        portable = json.loads(path.read_text())
        portable["version"] = version
        path.write_text(json.dumps(portable), encoding="utf-8")
        result = self.run_package()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_unaligned_cachebuster_is_rejected(self):
        self.manifest["version"] = "1.0.0+codex.local-20261013-184516"
        self.assert_rejected("Manifest mismatch: version")

    def test_final_prompt_length_is_enforced(self):
        self.manifest["interface"]["defaultPrompt"] = ["x" * 129]
        self.assert_rejected("interface.defaultPrompt")

    def test_normalized_duplicate_prompts_are_rejected(self):
        self.manifest["interface"]["defaultPrompt"] = ["Choose a workflow.", "Choose  a workflow."]
        self.assert_rejected("interface.defaultPrompt entries must be unique")

    def test_app_mention_is_rejected(self):
        self.manifest["interface"]["defaultPrompt"] = ["Ask @service for a workflow."]
        self.assert_rejected("interface.defaultPrompt")

    def test_final_short_description_limit_is_enforced(self):
        self.manifest["interface"]["shortDescription"] = "x" * 31
        self.assert_rejected("interface.shortDescription")

    def test_missing_logo_is_rejected(self):
        (self.root / "assets/frugal-logo.svg").unlink()
        self.assert_rejected("Missing or external branding asset")

    def test_asset_path_escape_is_rejected(self):
        self.manifest["interface"]["logo"] = "./../outside.svg"
        self.assert_rejected("interface.logo")

    def test_empty_inline_overlay_cannot_hide_compatibility_metadata(self):
        path = self.root / "plugin.json"
        portable = json.loads(path.read_text())
        portable["extensions"] = {"com.openai": {}}
        path.write_text(json.dumps(portable), encoding="utf-8")
        self.assert_rejected("An inline OpenAI overlay would replace the compatibility overlay")

    def test_nonsquare_icon_is_rejected(self):
        path = self.root / "assets/frugal-icon.svg"
        path.write_text(path.read_text().replace('height="128"', 'height="64"'))
        self.assert_rejected("Branding SVG must be square")

    def test_archive_includes_both_referenced_assets(self):
        result = self.run_package(check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(self.root / "dist" / f"frugal-skills-{self.manifest['version']}.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(len(archive.namelist()), 122)
            for field in ("logo", "composerIcon"):
                name = "frugal-skills/" + self.manifest["interface"][field][2:]
                self.assertEqual(archive.read(name), (self.root / name.split("/", 1)[1]).read_bytes())
            self.assertEqual(sum(name.endswith("/SKILL.md") for name in archive.namelist()), 115)


if __name__ == "__main__":
    unittest.main()
