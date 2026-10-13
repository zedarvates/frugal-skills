---
name: prompt-repetition
description: "Instructions for the upstream repeated-prompt detector: review long recurring prefixes in event logs using its declared policy thresholds. Confirm policy files and evidence fields before running it. Not for prompt rewriting, prefix measurement or delta transport."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: prompt_repetition
---
# prompt-repetition — anomaly A8 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## When NOT to use

- You want a better prompt, not a report on wasted ones — use prompt_improver.
- The cost is the static prefix, measured rather than observed in logs —
  use context_profiler.
- You already accept the repetition and want to send deltas —
  use context_windows or prefix_tree.

Implements A8 of [[../../docs/local-analysis-policy.md]]:

- Identifies prompt/context prefix patterns of >500 tokens repeated >= 3 times
  in `.botte/events.jsonl` or session event logs.
- Measures estimated wasted tokens across repeated calls.
- Emits standard five policy fields with clear template extraction refactoring.

```bash
python -m skills.prompt_repetition.cli [.botte/events.jsonl]
botte prompts
python -m skills.prompt_repetition.test_prompt_repetition
```

The upstream detector describes a JSON-serialisable result; validate it against the installed policy and evidence.
