---
name: agent-cache
description: "Skip an agent run whose result can be predicted instead of executing it again — three matching strategies: exact hash (same input, same output), code fingerprint (unchanged code, unchanged result) and fuzzy match (semantically similar questions), for an estimated 10 to 15 percent fewer redundant runs. Deterministic and local, 0 cloud tokens. Use when the same agent run is triggered repeatedly with effectively identical inputs. Not for caching a project scan that the next agent reads — use cache; not for caching a model answer keyed by question — use response-cache."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: agent_cache
---
# Agent Cache

Skippe l'exécution d'un agent si son résultat peut être prédit.

## Stratégies de matching

| Stratégie | Description | Quand |
|-----------|-------------|-------|
| Exact hash | Même input → même output | Tâches déterministes |
| Fingerprint | Code inchangé → résultat inchangé | Audit, linting |
| Fuzzy match | Similarité sémantique | Questions similaires |

## Usage

```bash
python -m skills.agent_cache.cli check "query" --agent audit
python -m skills.agent_cache.cli store "query" "response" --agent fix
python -m skills.agent_cache.cli stats
```
