---
name: efficiency
description: "Measure tokens, cloud calls, money, latency and local energy per verified task without storing task content."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: efficiency
---
# Efficiency ledger

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
