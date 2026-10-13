---
name: code-wrappers
description: "Instructions for upstream Policy A3 review of unchanged argument-forwarding functions with no distinct transformation, guard, decorator or docstring. Use to plan wrapper review and inspect the five-field evidence; dynamic-name references and non-1:1 signatures are excluded. Not for complexity or module-level state/import cycles."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code_wrappers
---
# code-wrappers — anomaly A3 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## When NOT to use

- The smell is complexity or length rather than pure forwarding —
  use code_complexity.
- The smell is global state or a circular import — use code_state.

The upstream detector is described by A3 of the upstream `docs/local-analysis-policy.md` (not bundled here): a function is a
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

The documented upstream mode is report-only; verify the installed command exit status and CI integration. Pairs with code_complexity (A1) and
code_duplication (A6).
