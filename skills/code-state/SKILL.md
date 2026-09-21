---
name: code-state
description: "Policy A2 detector (docs/local-analysis-policy.md) — finds mutable module-level state (dict/list/set assignments) and circular imports via a static AST import graph. TYPE_CHECKING blocks are ignored. Deterministic, 0 cloud tokens. Every finding carries the five mandatory policy fields. Use before isolating tests or flattening package imports. Not for duplicate bodies — use code-duplication (A6); not for passthrough wrappers — use code-wrappers (A3)."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: code_state
---
# code-state — anomaly A2 detector

## When NOT to use

- The smell is a duplicated function body — use code_duplication.
- The smell is a chain of passthrough functions — use code_wrappers.

Implements A2 of [[../../docs/local-analysis-policy.md]]:

- **etat_global** — module-level `NAME = {}` / `[]` / `set()` / `dict()`
  (and common constructors). Constants and `None` are ignored. Assignments
  inside `if TYPE_CHECKING` are ignored.
- **import_circulaire** — cycles in the local import graph. Relative and
  absolute imports that resolve inside the scanned tree are followed.
  `if TYPE_CHECKING` imports are not edges.

```bash
python -m skills.code_state.cli [path]
python -m skills.code_state.cli skills --json
python -m skills.code_state.test_code_state
```

Report-only: never fails the build. Pairs with code_wrappers (A3).
