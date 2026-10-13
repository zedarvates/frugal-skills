---
name: code-fingerprint
description: "Instructions for the upstream SHA-256 code-fingerprint cache and re-analysis gate. Use to assess whether an earlier analysis can be reused after checking code, analysis configuration and dependency changes. This is not a findings detector; use code-complexity, code-duplication, code-state or code-wrappers for findings."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code_fingerprint
---
# Code Fingerprinting (P13)

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The upstream fingerprint workflow hashes code to identify candidate reuse. Check analysis settings, dependencies and cache validity as well as source changes before skipping an analysis.

## When NOT to use

- You want the actual findings, not the skip decision — this module is a gate;
  use code_complexity, code_duplication, code_state or code_wrappers.
- You want to compare two versions of a prompt rather than of code — use
  diff_language or prefix_tree.

**Trigger:** Before every audit — check fingerprints, skip unchanged files.

**Usage:**
```python
from skills.code_fingerprint import CodeFingerprinter, skip_if_unchanged
fp = CodeFingerprinter()
result = skip_if_unchanged(fp, project_path, analyze_fn)
# If nothing changed: {"skipped": True, "reason": "no changes detected"}
```

**Module:** `skills/code_fingerprint`
**Cache:** .botte-cache/fingerprints.json
