---
name: code-state
description: "Instructions for upstream Policy A2 review of mutable module-level state and cycles in the local AST import graph, excluding TYPE_CHECKING blocks. Use before isolating tests or flattening imports and inspect the five-field evidence. Not for duplication (code-duplication) or passthrough functions (code-wrappers)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code_state
---
# code-state — anomaly A2 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## When NOT to use

- The smell is a duplicated function body — use code_duplication.
- The smell is a chain of passthrough functions — use code_wrappers.

The upstream detector is described by A2 of the upstream `docs/local-analysis-policy.md` (not bundled here):

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

The documented upstream mode is report-only; verify the installed command exit status and CI integration. Pairs with code_wrappers (A3).
