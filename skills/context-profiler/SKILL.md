---
name: context-profiler
description: "Guidance for upstream prefix measurement or estimation across agent directives, core rules, MCP schemas, skill catalogs and host memory. Use to plan context-budget diagnostics and compare available windows. Label estimates and unavailable measurements; not for context selection (context-budget), pruning or code-change detection."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: context_profiler
---
# context-profiler — how much window is gone before you start?

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## When NOT to use

- You want to pick a subset of skills for one task — use context_budget.
- You want to delete dead context sections — use prefix_pruner.
- You want to skip unchanged code during an audit — use code_fingerprint.

On a modest machine the usable window is shared between the model weights' RAM and
the KV-cache. The upstream profiler measures or estimates the **prefix** an agent carries and compares it with configured window sizes. Distinguish exact measurements from estimates and report unavailable host data.

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
  cost depends on the actual injected inventory).
- **skill_catalog** — the skills' descriptions IF the whole catalogue is injected.
- **host prefix** (`--host`) — runtime-imposed system prompt, memory context, user profile,
  host skill catalog, and MCP descriptions.
- **memory files** (`--memory`) — token count of `MEMORY.md` and related memory banks with threshold alerts.

It compares prefix costs with configured windows and proposes a **reduction plan**. Verify actual before/after measurements:
- **lazy tool loading** — expose the necessary core tools + a `find_tool(query)` that loads a
  schema on demand (the pattern this very harness uses via ToolSearch).
- **on-demand skill search** — don't inject the catalogue; use [[skill-finder]] /
  [[context-budget]] to load only the relevant skills per task.

The upstream MCP integration describes `context_profile` through [[llm-mcp]]. This catalog supplies no measured prefix baseline or verified reduction; record the actual runtime, injected inventory and tokenizer when reporting results.
