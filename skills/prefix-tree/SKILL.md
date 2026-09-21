---
name: prefix-tree
description: "Registry of each agent's stable prompt prefix in one compressed trie, so feedback loops and multi-agent exchanges send only the diff instead of the full prompt (register, diff, common, stats). Deterministic and local, with a store under ~/.botte. Use when several agents share a large common prefix and the repeated transmission is the cost. Not for deleting sections that nobody uses — use prefix-pruner; not for per-loop windows over a shared context — use context-windows; not for detecting repeated prompts in the logs — use prompt-repetition."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: prefix_tree
---
# prefix-tree — one trie of agent prefixes, then diffs only

## Purpose

Each agent has a stable prefix. The trie stores them together, finds the common
part, and produces the diff for a new payload, so a retroactive loop sends what
changed rather than the whole prompt again.

## When NOT to use

- You want to remove dead sections permanently — use prefix_pruner.
- The repetition is detected after the fact in event logs — use prompt_repetition.
- The reuse unit is a loop step over one shared context — use context_windows.

## Usage

```bash
python -m skills.prefix_tree.cli --help
```
