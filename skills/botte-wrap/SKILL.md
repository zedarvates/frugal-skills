---
name: botte-wrap
description: "Guidance for upstream wrap, unwrap, list and status commands that route an installed agent through a compression proxy. Use to plan integration without editing the agent binary; check wrapper and destination configuration. Not for compression policy, payload compression, MCP installation or measured savings."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: botte_wrap
---
# botte-wrap — route an agent through the compression proxy

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

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
