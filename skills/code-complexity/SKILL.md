---
name: code-complexity
description: "Policy A1 detector (docs/local-analysis-policy.md) — finds over-complex (cyclomatic > 10) and over-long (> 50 AST statements) functions via pure stdlib ast parsing. Deterministic, 0 cloud tokens. Every finding carries the five mandatory policy fields (preuve, cout_estime, gain_attendu, risque, refactoring_minimal). Use before refactors or during checkup. Not for duplicated bodies — use code-duplication (A6); not for module-level state or import cycles — use code-state (A2); not for passthrough functions — use code-wrappers (A3)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code_complexity
---
# code-complexity — anomaly A1 detector

## When NOT to use

- Two function bodies look like copies of each other — use code_duplication.
- The smell is global mutable state or a circular import — use code_state.
- The smell is a function that only forwards its arguments — use code_wrappers.

Implements A1 of [[../../docs/local-analysis-policy.md]]: cyclomatic
complexity (1 + branch points: if/elif, loops, except, ternaries, boolean
operators, comprehension guards, asserts, match cases) and function length
(AST statements, nested scopes excluded and reported separately).

```bash
python -m skills.code_complexity.cli [path]        # human-readable report
python -m skills.code_complexity.cli skills --json # compact JSON
python -m skills.code_complexity.test_code_complexity
```

Reports ONLY anomalies (at least one threshold exceeded). Report-only:
never fails the build. Pairs with future detectors of the same policy
(duplication A6, wrappers A3, …) which will share the five-field finding shape.
