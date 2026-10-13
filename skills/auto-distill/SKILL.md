---
name: auto-distill
description: "Instructions for the upstream cloud-to-small-classifier distillation module. Use to inspect its documented CLI and prerequisites before planning a distillation workflow. The executable module and trained models are not included in this catalog."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: auto_distill
---
# auto distill

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

Module de la session juillet 2026 — analyse Copilot.

## Usage

```bash
python -m skills.auto_distill.cli --help
```
