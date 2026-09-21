---
name: prefix-pruner
description: "Prune context sections the agent never actually uses — a prefix tree plus usage tracking, with three strategies (auto, aggressive drops anything below 0.3 usefulness, conservative drops only never-used sections) for roughly 2 to 15 percent additional savings. Use when an always-on context has grown and part of it is dead weight that no task references. Not for sending only per-loop deltas — use context-windows; not for keeping per-agent stable prefixes and diffing between agents — use prefix-tree; not for measuring the cost in the first place — use context-profiler."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: prefix_pruner
---
# Prefix Pruner

Élimine les sections de contexte que l'agent n'utilise jamais.

## Stratégies

| Stratégie | Description | Gain |
|-----------|-------------|------|
| `auto` | Prefix tree + usage tracking | 5-10% |
| `aggressive` | Supprime toute section < 0.3 usefulness | 10-15% |
| `conservative` | Ne supprime que les sections jamais utilisées | 2-5% |

## Usage

```bash
python -m skills.prefix_pruner.cli prune < context.txt
python -m skills.prefix_pruner.cli tree
python -m skills.prefix_pruner.cli stats
```
