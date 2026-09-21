---
name: prompt-repetition
description: "Policy A8 detector (docs/local-analysis-policy.md) — finds repeated prompts and system contexts (>500 tokens, repeated >=3 times) in event logs (.botte/events.jsonl). Deterministic, pure stdlib, 0 cloud tokens. Every finding carries the five mandatory policy fields (preuve, cout_estime, gain_attendu, risque, refactoring_minimal). Use to identify prefix caching and prompt template factoring opportunities. Not for rewriting a prompt — use prompt-improver; not for measuring the declared always-on prefix — use context-profiler; not for the delta-only transport across loops — use context-windows or prefix-tree."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: prompt_repetition
---
# prompt-repetition — anomaly A8 detector

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

Pure stdlib, 0 cloud tokens, JSON-serialisable.
