---
name: agent-cache
description: "Instructions for evaluating upstream agent-run caching with exact hashes, code fingerprints and fuzzy matches. Use for repeated runs with comparable inputs; verify cache validity before skipping execution. Not for project scan caching (cache) or model-answer caching (response-cache)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: agent_cache
---
# Agent Cache

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

Evaluate whether a verified upstream cache entry can replace a repeated agent run. Reuse requires compatible inputs, analysis settings and dependencies; semantic similarity alone is not proof that the result is interchangeable. Include relevant environment settings, governing rules and tool/runtime versions in the cache identity, or invalidate the entry when they change. Unchanged source alone does not establish an unchanged result.

## Stratégies de matching

| Stratégie | Description | Quand |
|-----------|-------------|-------|
| Exact hash | Same validated inputs and analysis configuration | Tâches déterministes |
| Fingerprint | Unchanged code plus compatible analysis inputs | Audit, linting |
| Fuzzy match | Chevauchement lexical approximatif; pertinence à vérifier | Questions similaires |

## Usage

```bash
python -m skills.agent_cache.cli check "query" --agent audit
python -m skills.agent_cache.cli store "query" "response" --agent fix
python -m skills.agent_cache.cli stats
```
