---
name: agent-overlap
description: "Policy A9 detector (docs/local-analysis-policy.md) — finds redundant concurrent agent missions with >=70% objective overlap in event logs (.botte/events.jsonl). Pure stdlib, 0 cloud tokens. Every finding carries the five mandatory policy fields. Use to avoid duplicate work and coordinate multi-agent tasks."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: agent_overlap
---
# agent-overlap — anomaly A9 detector

Implements A9 of [[../../docs/local-analysis-policy.md]]:

- Compares declared objectives/missions across concurrent sessions and distinct agents.
- Detects >= 70% vocabulary overlap without declared shared locks.
- Emits standard five policy fields with clear pilot agent coordinator refactoring.

```bash
python -m skills.agent_overlap.cli [.botte/events.jsonl]
botte overlap
python -m skills.agent_overlap.test_agent_overlap
```

Pure stdlib, 0 cloud tokens, JSON-serialisable.
