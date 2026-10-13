---
name: fast-context
description: "Instructions for upstream repository exploration using targeted read, glob and search operations with a compact file-and-line report. Confirm the runtime before invoking its commands and measure latency and host model usage. Not for choosing skills or profiling the always-on prefix."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: fast_context
---
# FastContext Agent — exploration repo

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Un sous-agent d'exploration déterministe qui sépare la **collecte de contexte**
du **raisonnement**. Les recherches locales peuvent réduire le contexte à fournir, mais leurs coûts et leur latence doivent être mesurés avec le runtime installé.

L'approche upstream est inspirée par Microsoft FastContext et utilise des recherches locales. Ce catalogue ne fournit ni son modèle ni son runtime.

## Usage

```bash
# Explorer un dossier
python -m skills.fast_context.cli explore /path/to/project "find DB connection patterns"

# Types de requête supportés
python -m skills.fast_context.cli explore . "find all imports in main.py"
python -m skills.fast_context.cli explore . "understand function: calibrate()"
python -m skills.fast_context.cli explore . "where are the tests?"
python -m skills.fast_context.cli explore . "queue usage patterns"
python -m skills.fast_context.cli explore . "audit security: eval, exec, shell"

# Mode verbeux
python -m skills.fast_context.cli explore . "find async patterns" --verbose

# Limiter les résultats
python -m skills.fast_context.cli explore . "import pathlib" --max-results 10

# Utiliser le cache
python -m skills.fast_context.cli explore . "class FastContext" --cache
```

## API Python

```python
from skills.fast_context import explore, cached_explore
from skills.fast_context import discover_query_type, QueryType

# Exploration simple
results = explore(".", "find DB connection patterns")
# → [{"file": "src/db.py:15", "snippet": "...", "score": 0.92, "type": "import"}, ...]

# Avec cache
results = cached_explore(".", "find async patterns", ttl=60)

# Découverte du type de requête
qt = discover_query_type("find all imports")
# → QueryType.IMPORTS
```

## Types de requête

| Type | Mots-clés | Action |
|------|-----------|--------|
| `IMPORTS` | import, dependency, require | grep imports + suggest files |
| `FUNCTION` | function, method, def, understand | grep def → contexte fichier |
| `TESTS` | test, spec, unittest | glob test_* + grep |
| `PATTERN` | pattern, usage, find, where | grep générique |
| `SECURITY` | security, audit, eval, malicious | grep dangereux |

## Architecture

```
FastContext Agent
  ┌─────────────────────────────────┐
  │  agent.py                       │
  │  - discover_query_type(query)   │
  │  - explore(query, path) → list  │
  ├─────────────────────────────────┤
  │  readers.py                     │
  │  - fast_read(file, lines)       │
  │  - fast_glob(pattern, root)     │
  │  - fast_grep(pattern, root)     │
  ├─────────────────────────────────┤
  │  ranker.py                      │
  │  - score(file, match, query)    │
  │  - rank_results(results)        │
  ├─────────────────────────────────┤
  │  compiler.py                    │
  │  - compile_report(results)      │
  │  - format_compact(results)      │
  ├─────────────────────────────────┤
  │  store.py                       │
  │  - LRUCache(ttl=30)             │
  └─────────────────────────────────┘
```

## Mesures

Comparer le contexte retourné, la qualité de recherche, la latence et la consommation réelle de l'agent. Aucun benchmark de gains n'est fourni dans ce catalogue.

## Pitfalls

1. **Ne remplace pas LLM pour compréhension complexe** — FastContext livre du
   contexte brut (fichier:ligne:snippet). Le LLM principal doit encore raisonner
   dessus. C'est le but : le LLM ne fait QUE raisonner.
2. **Cache TTL** — Le cache LRU évite de rescanner 30 fois le même fichier dans
   la même session. TTL par défaut: 30s. Passer `--no-cache` pour forcer.
3. **Gros repos** — Pour les repos >1000 fichiers, `fast_grep` utilise
   `subprocess.run("grep -rl ...")` plutôt qu'un glob Python (mesurer les performances sur le dépôt concerné).
4. **Binaire/symlinks** — Skip automatiquement les fichiers binaires, .git/,
   node_modules/, __pycache__/, .venv/.
