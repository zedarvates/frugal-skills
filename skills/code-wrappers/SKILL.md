---
name: code-wrappers
description: "Policy A3 detector (docs/local-analysis-policy.md) — finds passthrough functions whose body is exactly return f(*args, **kwargs) (or 1:1 argument forwarding) with no transformation, guard, decorator, or distinct docstring. Skips names referenced via getattr/patch. Deterministic, 0 cloud tokens. Every finding carries the five mandatory policy fields. Use before flattening call chains or during checkup. Not for complexity — use code-complexity (A1); not for module-level state or import cycles — use code-state (A2)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code_wrappers
---
# code-wrappers — anomaly A3 detector

## When NOT to use

- The smell is complexity or length rather than pure forwarding —
  use code_complexity.
- The smell is global state or a circular import — use code_state.

Implements A3 of [[../../docs/local-analysis-policy.md]]: a function is a
valueless wrapper when it forwards every argument unchanged to another callable
and adds no docstring, decorator, or transformation.

Skipped (fail-closed, not reported):

- functions with a docstring (public alias)
- decorated functions (caching, retry, metrics)
- dunder methods
- names referenced via `getattr` / `setattr` / `patch` in the scanned tree
- signatures that are not a 1:1 forward (defaults, keyword-only args)

```bash
python -m skills.code_wrappers.cli [path]        # human-readable report
python -m skills.code_wrappers.cli skills --json # compact JSON
python -m skills.code_wrappers.test_code_wrappers
```

Report-only: never fails the build. Pairs with code_complexity (A1) and
code_duplication (A6).
