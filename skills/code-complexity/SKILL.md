---
name: code-complexity
description: "Instructions for upstream Policy A1 analysis: cyclomatic complexity above 10 or function length above 50 AST statements, with five policy finding fields. Use to plan Python complexity review and interpret evidence. Not for duplication (code-duplication), global state/import cycles (code-state) or passthrough functions (code-wrappers)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code_complexity
---
# code-complexity — anomaly A1 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## When NOT to use

- Two function bodies look like copies of each other — use code_duplication.
- The smell is global mutable state or a circular import — use code_state.
- The smell is a function that only forwards its arguments — use code_wrappers.

The upstream detector is described by A1 of the upstream `docs/local-analysis-policy.md` (not bundled here): cyclomatic
complexity (1 + branch points: if/elif, loops, except, ternaries, boolean
operators, comprehension guards, asserts, match cases) and function length
(AST statements, nested scopes excluded and reported separately).

```bash
python -m skills.code_complexity.cli [path]        # human-readable report
python -m skills.code_complexity.cli skills --json # compact JSON
python -m skills.code_complexity.test_code_complexity
```

Reports ONLY anomalies (at least one threshold exceeded). The documented upstream mode is report-only; verify the installed command exit status and CI integration. Pairs with future detectors of the same policy
(duplication A6, wrappers A3, …) which will share the five-field finding shape.
