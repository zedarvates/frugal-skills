---
name: efficiency
description: "Instructions for the upstream workflow: Measure tokens, cloud calls, money, latency and local energy per verified task without storing task content."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: efficiency
---
# Efficiency ledger

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Use `start_run()` to create a random task identity, `record_usage()` for
provider-neutral counters, `record_verdict()` after deterministic verification,
and `end_run()` when the path finishes. Events contain bounded scalars only;
never add prompts, responses, paths, embeddings or transcripts.

The stable output contract is `docs/schemas/efficiency-sample-v1.schema.json`.
Missing measurements are `null` and must not be rewritten as zero.

Measure the local four-event write path without touching the project journal:

```text
python -m skills.efficiency.benchmark --iterations 200
```

This proves only ledger overhead on the current filesystem. It does not prove
provider coverage, task quality, or the 100-task adoption gate.

For an adoption decision, build separate baseline and candidate replay arms
whose `samples` map the 100 frozen case IDs to validated ledger samples. Pass
them to `compare_replay_arms()`. The comparator requires the frozen corpus,
distinct executions, matching project/model/tokenizer/verifier/tool controls,
no quality loss beyond one percentage point, no critical regression, and all
required measurements. Zero provider calls are reported `not_applicable`,
never as 100% provider-usage coverage.
