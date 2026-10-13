#!/usr/bin/env python3
"""Check, package and optionally smoke-test the instructions-only Codex plugin."""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
WITHHELD = {"caveman", "karpathy-guidelines", "cwe-kb"}
SKILL_COUNT = 115


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_interface(interface):
    """Guard the stricter directory listing fields before ZIP ingestion.

    This is a local metadata guard, not the portal's safety, identity or review
    checks. Field types and final limits follow the official submission-errors
    reference linked in docs/CODEX.md.
    """
    require(isinstance(interface, dict), "Missing plugin interface")

    def text_field(value, label, limit):
        require(isinstance(value, str) and bool(value.strip()),
                f"{label} must be a non-empty string")
        require(len(value) <= limit, f"{label} exceeds {limit} characters")
        require(not any(unicodedata.category(char) in {"Cc", "Cf", "Zl", "Zp"}
                        for char in value), f"{label} must use supported single-line text")

    for field, limit in (("displayName", 30), ("shortDescription", 30), ("developerName", 80)):
        text_field(interface.get(field), f"interface.{field}", limit)
    require(isinstance(interface.get("longDescription"), str)
            and 0 < len(interface["longDescription"].strip()) <= 4000,
            "interface.longDescription must be a non-empty string of at most 4000 characters")
    capabilities = interface.get("capabilities")
    require(isinstance(capabilities, list) and 1 <= len(capabilities) <= 20,
            "interface.capabilities must be a non-empty array of at most 20 strings")
    for capability in capabilities:
        text_field(capability, "interface.capabilities entry", 120)
    prompts = interface.get("defaultPrompt")
    if isinstance(prompts, str):
        prompts = [prompts]
    require(isinstance(prompts, list) and 1 <= len(prompts) <= 3,
            "interface.defaultPrompt must be a string or a non-empty array of at most 3 strings")
    normalized = set()
    for prompt in prompts:
        text_field(prompt, "interface.defaultPrompt entry", 128)
        require("@" not in prompt, "interface.defaultPrompt must not contain app @mentions")
        value = " ".join(unicodedata.normalize("NFKC", prompt).split())
        require(value not in normalized, "interface.defaultPrompt entries must be unique")
        normalized.add(value)


def branding_files(interface):
    """Validate the two original SVG assets against the documented icon rules."""
    files = []
    for field in ("composerIcon", "logo"):
        reference = interface.get(field)
        require(isinstance(reference, str) and reference.startswith("./")
                and ".." not in Path(reference).parts and "\\" not in reference,
                f"interface.{field} must be a ./-prefixed internal asset path")
        path = ROOT / reference
        require(path.resolve().is_relative_to(ROOT.resolve()) and path.is_file()
                and not path.is_symlink(), f"Missing or external branding asset: {reference}")
        require(path.suffix == ".svg", "Review any change from the package's SVG branding format")
        data = path.read_bytes()
        require(len(data) <= 5 * 1024 * 1024, f"Branding asset exceeds 5 MiB: {reference}")
        text = data.decode("utf-8")
        require("<!DOCTYPE" not in text and "<!ENTITY" not in text,
                f"Branding SVG must not declare entities: {reference}")
        svg = ET.fromstring(text)
        require(svg.tag == "{http://www.w3.org/2000/svg}svg", f"Invalid SVG root: {reference}")
        dimensions = []
        if "width" in svg.attrib or "height" in svg.attrib:
            dimensions.append((float(svg.attrib["width"]), float(svg.attrib["height"])))
        if "viewBox" in svg.attrib:
            box = [float(value) for value in re.split(r"[\s,]+", svg.attrib["viewBox"].strip())]
            require(len(box) == 4 and all(math.isfinite(value) for value in box),
                    f"Invalid SVG viewBox: {reference}")
            dimensions.append((box[2], box[3]))
        require(dimensions, f"Missing numeric SVG dimensions: {reference}")
        require(all(math.isfinite(width) and math.isfinite(height)
                    and width == height and width >= 48 for width, height in dimensions),
                f"Branding SVG must be square and at least 48 by 48: {reference}")
        for element in svg.iter():
            require(element.tag not in {"{http://www.w3.org/2000/svg}script",
                                        "{http://www.w3.org/2000/svg}foreignObject"},
                    f"Branding SVG must contain only static geometry: {reference}")
            require(not any(key.lower().startswith("on") or key.endswith("href")
                            for key in element.attrib),
                    f"Branding SVG must not contain scripts or external resources: {reference}")
        files.append(path)
    return files


def package_files():
    portable = read_json(ROOT / "plugin.json")
    codex = read_json(ROOT / ".codex-plugin/plugin.json")
    for key in ("name", "version", "description", "author", "license", "repository"):
        require(portable.get(key) == codex.get(key), f"Manifest mismatch: {key}")
    require(portable.get("$schema") ==
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "Unexpected portable schema")
    require(codex.get("name") == "frugal-skills", "Unexpected plugin name")
    require(re.fullmatch(r"\d+\.\d+\.\d+", codex.get("version", "")),
            "Use a stable semantic plugin version")
    require(codex.get("skills") == "./skills/", "Unexpected skill path")
    validate_interface(codex.get("interface"))
    assets = branding_files(codex["interface"])
    extensions = portable.get("extensions", {})
    require(isinstance(extensions, dict) and "com.openai" not in extensions,
            "An inline OpenAI overlay would replace the compatibility overlay")
    require(not {"mcpServers", "apps", "hooks"}.intersection(codex),
            "This package must remain skills-only")
    require(not (ROOT / "mcp.json").exists() and not (ROOT / ".mcp.json").exists(),
            "MCP configuration does not belong in this skills-only package")

    marketplace = read_json(ROOT / ".agents/plugins/marketplace.json")
    require(marketplace.get("name") == "frugal-skills-marketplace",
            "Unexpected marketplace name")
    require(marketplace.get("plugins") == [{
        "name": "frugal-skills",
        "source": {"source": "local", "path": "./"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }], "Marketplace source or policy changed; review install behaviour")

    directories = sorted((ROOT / "skills").iterdir())
    require(len(directories) == SKILL_COUNT, f"Expected {SKILL_COUNT} skill folders")
    skills = []
    for directory in directories:
        require(directory.is_dir() and not directory.is_symlink(),
                f"Skill folder must be a real directory: {directory.name}")
        require(directory.name not in WITHHELD,
                f"Unresolved provenance: {directory.name}")
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", directory.name),
                f"Invalid skill directory: {directory.name}")
        path = directory / "SKILL.md"
        require(path.is_file() and not path.is_symlink(), f"Missing skill: {path}")
        text = path.read_text(encoding="utf-8")
        require(text.startswith("---\n") and "\n---\n" in text[4:],
                f"Missing frontmatter: {path}")
        header, body = text[4:].split("\n---\n", 1)
        require(re.search(rf"^name: {re.escape(directory.name)}$", header, re.M),
                f"Frontmatter name mismatch: {path}")
        require(re.search(r"^description: \S", header, re.M) and body.strip(),
                f"Missing description or instructions: {path}")
        # Only SKILL.md is distributed today. Extra resources need an explicit
        # inventory update so no referenced asset is silently omitted.
        require(list(directory.iterdir()) == [path], f"Review new skill resources: {directory}")
        skills.append(path)

    files = [ROOT / name for name in (
        "plugin.json", ".codex-plugin/plugin.json", "LICENSE",
        "THIRD_PARTY_NOTICES.md", "docs/CODEX.md",
    )] + skills + assets
    for path in files:
        require(path.is_file() and not path.is_symlink(), f"Invalid package file: {path}")
    return codex, sorted(files)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def smoke_codex(files, version):
    require(shutil.which("codex"), "Codex CLI is required for --smoke-codex")
    with tempfile.TemporaryDirectory(prefix="frugal-codex-home-") as task_home:
        # CODEX_HOME is the documented configuration root; use a temporary root
        # so the smoke check cannot change the user's installed plugins.
        task_env = dict(os.environ, CODEX_HOME=task_home)

        def run(*args):
            result = subprocess.run(
                ["codex", *args, "--json"], env=task_env,
                cwd=task_home, text=True, capture_output=True, timeout=30,
            )
            require(result.returncode == 0,
                    f"Codex command failed: {' '.join(args)}\n{result.stderr}")
            return json.loads(result.stdout)

        run("plugin", "marketplace", "add", str(ROOT))
        catalog = run("plugin", "list", "--marketplace",
                      "frugal-skills-marketplace", "--available")
        require(any(item.get("name") == "frugal-skills" and item.get("version") == version
                    for item in catalog.get("available", [])),
                "Codex did not discover the packaged plugin version")
        installed = run("plugin", "add", "frugal-skills@frugal-skills-marketplace")
        installed_root = Path(installed["installedPath"]).resolve()
        require(installed_root.is_relative_to(Path(task_home).resolve()),
                "Codex installed outside the isolated configuration root")
        run("plugin", "add", "frugal-skills@frugal-skills-marketplace")
        for path in files:
            cached = installed_root / path.relative_to(ROOT)
            require(cached.is_file() and digest(cached) == digest(path),
                    f"Installed package differs from source: {cached}")
        require(len(list((installed_root / "skills").glob("*/SKILL.md"))) == SKILL_COUNT,
                "Installed skill inventory differs from source")
    print(f"Codex discovery, install, reinstall and {SKILL_COUNT}-skill integrity: OK")


def build_zip(files, version):
    target = ROOT / "dist" / f"frugal-skills-{version}.zip"
    target.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            info = zipfile.ZipInfo(f"frugal-skills/{path.relative_to(ROOT).as_posix()}",
                                   date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(target) as archive:
        require(archive.testzip() is None, "Corrupt release archive")
        require(len(archive.namelist()) == len(files), "Archive inventory mismatch")
    print(f"Built {target.relative_to(ROOT)} ({len(files)} files, SHA256 {digest(target)})")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without writing a ZIP")
    parser.add_argument("--smoke-codex", action="store_true", help="Install in an isolated Codex cache")
    args = parser.parse_args()
    manifest, files = package_files()
    print(f"Plugin {manifest['name']} {manifest['version']}: {SKILL_COUNT} skills; provenance exclusions: OK")
    if args.smoke_codex:
        smoke_codex(files, manifest["version"])
    if not args.check:
        build_zip(files, manifest["version"])


if __name__ == "__main__":
    main()
