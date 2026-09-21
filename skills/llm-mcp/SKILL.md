---
name: llm-mcp
description: "MCP server that lets Claude Code (or any MCP client) discover and call local LLM servers (LM Studio, Ollama, …) as tools, to offload cheap tasks off the cloud. Use when the user wants to wire local models into their agent, register an MCP server, or have the agent automatically route simple tasks to local hardware."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: llm_mcp
---
# llm-mcp — Local LLM tools over Model Context Protocol

Exposes [[llm-backends]] as MCP tools so an agent can route work to local models
on its own. Pure stdlib, stdio JSON-RPC 2.0, no dependencies.

## Tools exposed

| Tool | Purpose |
|------|---------|
| `discover_backends` | Scan localhost/network, register reachable LLM servers |
| `list_models` | List models the registered backends expose |
| `audit_local_usage` | Local-usage report + hardware-aware setup steps |
| `route_task` | Recommend cheapest tier + a concrete local backend/model |
| `local_chat` | Run a prompt on a local model (0 cloud tokens) |
| `session_handoff` | Create, validate, or render a bounded `brief_only` handoff |
| `agent_state` | Negotiate agent capabilities, authority, and mutation scopes |
| `recipe_run` | Lazily run one locally approved read-only declarative recipe |

## Register in Claude Code

Add to `.mcp.json` at the project root (an example ships at
`configs/mcp.example.json`):

```json
{
  "mcpServers": {
    "botte-llm": {
      "command": "python",
      "args": ["-m", "skills.llm_mcp.server"],
      "cwd": "/path/to/project"
    }
  }
}
```

Then in a session: *"discover my local backends"*, *"classify these 50 tickets
locally"*, *"is local routing active?"* — the agent calls the tools directly.

## Lazy tool loading (default on)

The server has grown to ~39 tools; injecting every full JSON Schema into an
agent's context costs ~3.9k tokens **on every turn**, whether or not that turn
uses them — [[context-profiler]] measured it as the single biggest slice of
always-on prefix on this repo. So `tools/list` returns only a small core
(`local_chat`, `auto_route`, `find_skills`, `conduct`) plus a `find_tool(query)`
meta-tool — the same pattern this very harness uses (ToolSearch). Call
`find_tool` to discover anything else; a strong match returns the full schema in
one round trip. `tools/call` still dispatches **any** tool by name regardless of
what was listed — lazy loading only shrinks the catalog, not what's callable.

Measured saving: ~3.3k tokens (84% of the tool-schema cost). Disable with
`BOTTE_MCP_LAZY_TOOLS=0` for a client that expects the full catalog upfront.

`recipe_run` remains outside the core list. Its schema is discovered only when
needed, and recipe approval never grants authority beyond the current MCP
dispatcher and deny-by-default read-only recipe policy. See [[recipes]].

## Manual smoke test

```bash
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{}}}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' \
 '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"local_chat","arguments":{"prompt":"ping","max_tokens":16}}}' \
 | python -m skills.llm_mcp.server
```

## Token strategy

Tell the agent: *route classification / extraction / short summaries through
`local_chat`, keep architecture & security reasoning on the cloud.* That single
rule typically moves 30-50% of calls to zero-cost local inference.
