---
name: botte-wrap
description: "Wrap an installed coding agent so its traffic goes through the local compression proxy, and unwrap it again — wrap, unwrap, list, status, with the proxy supervised on its port and the agents discovered on the machine. Use when an existing agent binary should benefit from compression without editing the agent. Not for deciding what to compress — use token-shaper (policy) or universal-compressor (content); not for installing cross-agent MCP plugins — use plugins; not for measuring the resulting saving — use metrics."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: botte_wrap
---
# botte-wrap — route an agent through the compression proxy

## Purpose

Wraps an agent so its requests are compressed before leaving the machine, and
restores it on demand. The wrapper state is tracked per agent and listable.

    python -m skills.botte_wrap.cli list
    python -m skills.botte_wrap.cli wrap <agent>
    python -m skills.botte_wrap.cli unwrap <agent>
    python -m skills.botte_wrap.cli status

## When NOT to use

- You want to choose the compression policy — use token_shaper.
- You want to compress a specific payload — use universal_compressor.
- You want an MCP server installed into several agents — use plugins.
