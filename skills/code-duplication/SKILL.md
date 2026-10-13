---
name: code-duplication
description: "Instructions for upstream Policy A6 analysis of duplicated Python bodies using normalized AST hashes and an optional semantic mode; the documented minimum is six statements. Use to plan duplication review and examine five-field findings. Not for complexity (code-complexity) or skill-description overlap (skill-finder); verify equivalence before merging code."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code_duplication
---
# code-duplication — anomaly A6 detector (exact + semantic)

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## When NOT to use

- The problem is a function that is too complex or too long — use code_complexity.
- The duplication is between two skill descriptions rather than two code
  bodies — the catalog-level overlap check belongs with skill_finder.

The upstream detector describes both halves of A6 of
the upstream `docs/local-analysis-policy.md` (not bundled here): two function bodies are duplicates
when their statement sequences produce identical hashes (comments and
formatting ignored; function names irrelevant — the exact half), or when
their AST shape is identical after identifier normalization (same operators,
same call shapes, constants preserved — the semantic half, opt-in via
`--semantic`). Only bodies of >= 6 statements (nested blocks included) are
considered.

```bash
python -m skills.code_duplication.cli [path]        # human-readable report
python -m skills.code_duplication.cli skills --json # compact JSON
python -m skills.code_duplication.cli . --semantic # exact + semantic report
python -m skills.code_duplication.test_code_duplication
```

Semantic findings are reported separately (`dup_semantique`) and never
duplicate an exact group. Because two similar bodies can differ
intentionally, the policy requires a line-by-line equivalence diff before any
merge; findings carry that caveat in `risque` and `refactoring_minimal`.
The documented upstream mode is report-only; verify the installed command exit status and CI integration. Pairs with code_complexity (A1) which
shares the five-field finding shape.
