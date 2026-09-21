---
name: code-fingerprint
description: "Hash every function, method, class and module (SHA-256 over normalized source) so a re-analysis only touches what actually changed, with a persistent cache under .botte-cache/fingerprints.json and roughly -80 percent analysis cost on stable codebases. Deterministic, local, 0 cloud tokens. Use as the gate in front of any audit or checkup run. This is not a detector: it decides what to re-run, and the findings themselves come from code-complexity (A1), code-duplication (A6), code-state (A2) and code-wrappers (A3)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code_fingerprint
---
# Code Fingerprinting (P13)

Hash every function/method/class and only re-analyze what changed.

## When NOT to use

- You want the actual findings, not the skip decision — this module is a gate;
  use code_complexity, code_duplication, code_state or code_wrappers.
- You want to compare two versions of a prompt rather than of code — use
  diff_language or prefix_tree.

**Trigger:** Before every audit — check fingerprints, skip unchanged files.

**Token savings:** -80% on re-analysis of stable codebases

**Usage:**
```python
from skills.code_fingerprint import CodeFingerprinter, skip_if_unchanged
fp = CodeFingerprinter()
result = skip_if_unchanged(fp, project_path, analyze_fn)
# If nothing changed: {"skipped": True, "reason": "no changes detected"}
```

**Module:** `skills/code_fingerprint`
**Cache:** .botte-cache/fingerprints.json
