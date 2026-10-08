#!/usr/bin/env python3
"""Create and locally check the public skills-only plugin ZIP (stdlib only)."""
from __future__ import annotations

import json
import re
from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent
repo = root.parents[1]
manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
assert manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
assert manifest["name"] == "frugal-agent-kit"
assert re.fullmatch(r"\\d+\\.\\d+\\.\\d+", manifest["version"])
ui = manifest["extensions"]["com.openai"]["interface"]
assert len(ui["displayName"]) <= 30
assert len(ui["shortDescription"]) <= 30

entries = [root / "plugin.json", root / "PROVENANCE.md"]
skill_paths = sorted((root / "skills").glob("*/SKILL.md"))
assert len(skill_paths) == 4
for p in skill_paths:
    body = p.read_text(encoding="utf-8")
    assert re.match(r"^---\\nname: [a-z][a-z0-9-]+\\ndescription:", body), p
    assert not re.search(r"sk-proj-|ghp_|BEGIN PRIVATE KEY", body)
entries += skill_paths
for field in ("composerIcon", "logo"):
    value = ui[field]
    assert value.startswith("./") and ".." not in Path(value).parts
    icon = root / value.removeprefix("./")
    assert icon.exists() and icon.suffix == ".svg"
    ElementTree.fromstring(icon.read_text(encoding="utf-8"))
    entries.append(icon)
license_file = repo / "LICENSE"
assert license_file.exists(), "Repository root MIT license is required"

out = root / "dist" / f"frugal-agent-kit-openai-submission-v{manifest['version']}.zip"
out.parent.mkdir(exist_ok=True)
with ZipFile(out, "w", ZIP_DEFLATED) as z:
    for src in sorted(set(entries)):
        z.write(src, src.relative_to(root).as_posix())
    z.write(license_file, "LICENSE")
with ZipFile(out) as z:
    names = z.namelist()
    assert len(names) == len(set(names))
    assert not any(n.startswith("/") or ".." in Path(n).parts for n in names)
    assert "mcp.json" not in names and ".app.json" not in names
print(f"Static checks PASS: {len(names)} files, {len(skill_paths)} skills, ZIP={out}")
print("Portal checks, independent skill behavior tests, and publication are NOT completed.")
