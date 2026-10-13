---
name: prefix-pruner
description: "Instructions for upstream context pruning using recorded usefulness: auto, aggressive and conservative strategies. Validate the records and preserve required instructions; do not assume fixed token savings. Not for context transport deltas or prefix measurement."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: prefix_pruner
---
# Prefix Pruner

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Élimine les sections de contexte que l'agent n'utilise jamais.

## Stratégies

| Stratégie | Description |
|-----------|-------------|
| `auto` | Prefix tree + usage tracking |
| `aggressive` | Supprime les sections sous le seuil de pertinence déclaré |
| `conservative` | Ne supprime que les sections sans usage observé |

Mesurer les effets et préserver les instructions nécessaires ; aucun gain fixe n'est fourni ici.

## Usage

```bash
python -m skills.prefix_pruner.cli prune < context.txt
python -m skills.prefix_pruner.cli tree
python -m skills.prefix_pruner.cli stats
```
