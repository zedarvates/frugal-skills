---
name: plugins
description: "Install cross-agent MCP plugins into supported coding agents through one installer with a declared list of supported tools, so several agents get the same server without per-agent manual configuration. Use when wiring an MCP server into more than one agent. Not for discovering what should be installed — use mcp-gateway or skill-finder; not for routing an agent's traffic through the compression proxy — use botte-wrap; not for the governed memory store exposed as MCP — use memory-hub."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: plugins
---
# plugins — one installer, several agents

## Purpose

Removes the per-agent manual step when the same MCP server must be available in
several coding agents. The supported tool list is declared, so an unsupported
agent is refused rather than half-configured.

    from skills.plugins import SUPPORTED_TOOLS, install_plugins

## When NOT to use

- You do not yet know what to install — use mcp_gateway or skill_finder.
- You want an agent's requests compressed — use botte_wrap.
