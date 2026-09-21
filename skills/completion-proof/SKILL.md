---
name: completion-proof
description: "Policy A11 detector (docs/local-analysis-policy.md) — finds reports that claim done/complete/termine/fixed without an associated proof (test_id OR cmd_output_ref OR artifact_hash OR a passed validation with a reference). Deterministic, 0 cloud tokens. Every finding carries the five mandatory policy fields. Use before trusting a 'done' report or during checkup."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: completion_proof
---
# completion-proof — anomaly A11 detector

Implements A11 of [[../../docs/local-analysis-policy.md]]: a completion claim
without proof is an anomaly. Proof is one of:

- structured `proof.test_id` / `proof.cmd_output_ref` / `proof.artifact_hash`
- the same keys at the report root
- an `agent_state` completion whose `validations` contain a `passed` item
  with a non-empty `reference`
- lexical evidence in text reports (`N passed`, `exit_code=0`, `pytest`,
  `snapshot=`, `sha256:`)

```bash
python -m skills.completion_proof.cli [path]        # human-readable report
python -m skills.completion_proof.cli .botte --json # compact JSON
python -m skills.completion_proof.test_completion_proof
```

Scans `.json` / `.jsonl` plus report-named `.md/.txt/.html` files. Report-only:
never fails the build. Pairs with code_complexity (A1) and code_duplication (A6).
