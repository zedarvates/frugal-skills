---
name: context-windows
description: "Persistent context windows for feedback loops — register a window per loop step, then load only the deltas or a merged window instead of resending the whole context on every turn (step, merge, stats). Deterministic and local. Use when an agent iterates on the same context across many turns and the full resend is the cost. Not for keeping a per-agent stable prompt prefix and diffing between agents — use prefix-tree; not for file analysis across runs — use code-fingerprint."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: context_windows
---
# context-windows — load the delta, not the loop

## Purpose

Keeps named windows of context alive across the steps of a retroactive loop, so
a turn loads the changed deltas or a merged window rather than the full body.

## When NOT to use

- The prefix is stable per agent and you want agent-to-agent diffing —
  use prefix_tree.
- The repeated cost is re-analyzing unchanged code — use code_fingerprint.
- The wasted cost is a repeated prompt in event logs — use prompt_repetition.

## Usage

```bash
python -m skills.context_windows.cli --help
```
