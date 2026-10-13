---
name: agent-overlap
description: "Instructions for upstream Policy A9 analysis of concurrent missions with at least 70% vocabulary overlap and no declared shared locks. Use to review possible duplicated agent work; confirm findings against the actual missions. The upstream finding contract has five policy fields."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: agent_overlap
---
# agent-overlap — anomaly A9 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The upstream detector is described by A9 of the upstream `docs/local-analysis-policy.md` (not bundled here):

- Compares declared objectives/missions across concurrent sessions and distinct agents.
- Detects >= 70% vocabulary overlap without declared shared locks.
- Emits standard five policy fields with clear pilot agent coordinator refactoring.

```bash
python -m skills.agent_overlap.cli [.botte/events.jsonl]
botte overlap
python -m skills.agent_overlap.test_agent_overlap
```

The upstream design uses standard-library analysis and JSON-serialisable findings; validate the installed detector before relying on its output.
