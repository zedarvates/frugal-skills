---
name: hermes-bridge
description: "Instructions for the upstream workflow: Expose auto_route/local_chat/fusion/find_skills/infra_tips to Hermes-Agent (or any framework that expects OpenAI-function-calling tool specs instead of MCP) — plus a one-call MCP config generator for the zero-code path if the framework already speaks MCP. Use when connecting the toolkit's routing belt to another agent framework."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: hermes_bridge
---
# hermes-bridge — connect the belt to another agent framework

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

the toolkit already runs a standard MCP server (`skills.llm_mcp.server`,
stdio JSON-RPC). If the target framework speaks MCP, **that's the whole
integration** — no code in this module runs:

```bash
python -m skills.hermes_bridge.cli config --cwd /path/to/project
# → paste the printed {"mcpServers": {...}} block into the framework's MCP config
```

This module exists for frameworks — [[hermes-second-brain]] among them — that
instead expect a flat list of OpenAI-function-calling tool specs + a
dispatcher, a common shape for agents built before/without MCP support.

```bash
python -m skills.hermes_bridge.cli schemas          # the 5 tool specs, OpenAI-shaped
python -m skills.hermes_bridge.cli call botte_auto_route --prompt "rename x to y"
```

```python
from skills.hermes_bridge import TOOL_SCHEMAS, dispatch

# register TOOL_SCHEMAS with the framework's tool-calling mechanism, then:
dispatch("botte_auto_route", {"prompt": "..."})   # → JSON string, same shape as the MCP tool
```

## The 5 tools

Deliberately a subset of the ~35-tool MCP surface — the ones that matter for
a second-brain / routing integration:

| tool | what it does |
|------|----------------|
| `botte_auto_route` | plan local-vs-cloud routing; `execute=true` to actually run it |
| `botte_local_chat` | run a prompt on a configured local model; inspect usage and forwarding |
| `botte_fusion` | cascade / draft_refine / vote — models collaborating |
| `botte_find_skills` | 0-token local search over installed skill catalogs |
| `botte_infra_tips` | hardware/software setup advice for running local models |

## Why this matters for a second-brain agent

Every task [[hermes-second-brain]] would otherwise send straight to its own
model gets a chance to resolve locally or via the cheapest capable tier
first — see [[bench]] for how to measure it with a compatible runtime; no result is established by this catalog.
`botte_find_skills` also gives Hermes 0-token access to the local skill
catalog instead of re-deriving capabilities from scratch each session.

Related: [[llm-mcp]] (the native MCP server this bridges from), [[auto-router]],
[[bench]] (the proof), `docs/integrations/hermes.md` (the full integration write-up).
