---
name: code-duplication
description: "Policy A6 detector (docs/local-analysis-policy.md) — finds duplicated function bodies and near-duplicate functions across a tree, exactly and semantically (same AST shape with renamed identifiers, via --semantic), through normalized AST hashing with formatting and comments ignored and a minimum of 6 statements. Deterministic, pure stdlib, 0 cloud tokens. Every finding carries the five mandatory policy fields (preuve, cout_estime, gain_attendu, risque, refactoring_minimal). Use before refactors or during checkup, and to prevent the same capability being implemented twice. Not for complexity or length — use code-complexity (A1); not for duplicate descriptions across skills — that is the catalog-level check, see skill-finder."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: code_duplication
---
# code-duplication — anomaly A6 detector (exact + semantic)

## When NOT to use

- The problem is a function that is too complex or too long — use code_complexity.
- The duplication is between two skill descriptions rather than two code
  bodies — the catalog-level overlap check belongs with skill_finder.

Implements both halves of A6 of
[[../../docs/local-analysis-policy.md]]: two function bodies are duplicates
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
Report-only: never fails the build. Pairs with code_complexity (A1) which
shares the five-field finding shape.
