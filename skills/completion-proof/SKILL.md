---
name: completion-proof
description: "Instructions for upstream Policy A11 review of completion claims lacking a referenced test, command output, artifact hash or passed validation. Use before trusting a done/fixed report. Examine the actual evidence; the catalog does not run the detector or prove the claimed result."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: completion_proof
---
# completion-proof — anomaly A11 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The upstream detector is described by A11 of the upstream `docs/local-analysis-policy.md` (not bundled here): a completion claim
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

Scans `.json` / `.jsonl` plus report-named `.md/.txt/.html` files. The documented upstream mode is report-only; verify the installed command exit status and CI integration. Pairs with code_complexity (A1) and code_duplication (A6).
