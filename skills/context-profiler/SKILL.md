---
name: context-profiler
description: "Measure a project's always-on prefix (agent directives + core rules + MCP tool schemas + skill catalogue) in tokens and as a % of small local-model windows (64k/128k/256k), with a concrete reduction plan (lazy tool loading, on-demand skill search). Use to see how much of a modest machine's usable context is spent before any real work, and how to shrink it so weaker machines can run local LLMs usably. Not for choosing what to load for one task — use context-budget; not for deleting sections that are never used — use prefix-pruner; not for hashing code so a re-analysis can skip unchanged files — use code-fingerprint."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: context_profiler
---
# context-profiler — how much window is gone before you start?

## When NOT to use

- You want to pick a subset of skills for one task — use context_budget.
- You want to delete dead context sections — use prefix_pruner.
- You want to skip unchanged code during an audit — use code_fingerprint.

On a modest machine the usable window is shared between the model weights' RAM and
the KV-cache, and every always-on token is paid twice (RAM + each turn). This
measures the **prefix** an agent carries before its first message and frames it
against real local windows, so you can shrink it.

```bash
python -m skills.context_profiler.cli .            # prefix tokens + % of 64k/128k/256k
python -m skills.context_profiler.cli . --host     # project + host prefix estimation
python -m skills.context_profiler.cli . --memory   # measure memory files + threshold alert
python -m skills.context_profiler.cli . --json
```

Components measured:
- **directives** — CLAUDE.md / AGENTS.md instructions ([[metrics]] always-on).
- **core_agent** — the shared `core-agent.md` rules, if present.
- **tool_schemas** — the MCP tool definitions injected into the agent (the *hidden*
  cost: on this repo ~3.8k tok for 38 tools).
- **skill_catalog** — the skills' descriptions IF the whole catalogue is injected.
- **host prefix** (`--host`) — runtime-imposed system prompt, memory context, user profile,
  host skill catalog, and MCP descriptions.
- **memory files** (`--memory`) — token count of `MEMORY.md` and related memory banks with threshold alerts.

It then reports the % of 64k/128k/256k windows and a **reduction plan** with honest
token savings:
- **lazy tool loading** — expose ~5 core tools + a `find_tool(query)` that loads a
  schema on demand (the pattern this very harness uses via ToolSearch).
- **on-demand skill search** — don't inject the catalogue; use [[skill-finder]] /
  [[context-budget]] to load only the relevant skills per task.

On this repo: prefix ~7.9k tok (12% of a 64k window) → **~1.4k tok (2%)** once
lazy tools + on-demand skills are applied. Exposed via [[llm-mcp]] as
`context_profile`. Pure measurement, 0 cloud tokens.
