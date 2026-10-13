---
name: sbom
description: "Instructions for the upstream workflow: Lightweight SBOM scanner for Python/Rust/Node dependencies"
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: sbom
---
# SBOM Scanner

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

The upstream workflow parses requirements.txt, Cargo.toml and package.json. Verify the compatible parser and inputs before reporting an inventory.
