---
name: hermes-second-brain
description: "A compounding knowledge layer for sessions — a goal layer, a retrieved knowledge layer and a history layer filter every response, and a harvest step writes the session's learnings back into the local vector store, so a new session starts from retrieved memory instead of a re-injected history. Use when repeated sessions should accumulate knowledge rather than restart. Not for governed memory with sensitivity, visibility and a promote or forget lifecycle — use memory-hub; not for caching model responses — use response-cache; not for measuring the injected context — use context-profiler."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: hermes-second-brain
---
# Hermes Second Brain

> A self-learning system that filters every output through goals, business data,
> and history — getting smarter every session.

## Purpose

The design of a persistent knowledge loop: context before the session, vector
retrieval during it, harvest after it. The claimed benefit is a much smaller
per-session context because history is retrieved rather than re-injected.

Read the design, components and usage in [DESIGN.md](DESIGN.md).

## Boundaries

- The claimed savings are design figures, not measured on the current tree.
- Retrieval quality is not the same as recall of the full history.

## When NOT to use

- You need memory with permissions and revocation — use memory_hub.
- You need a response cache — use response_cache.
