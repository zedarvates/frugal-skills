---
name: hermes-second-brain
description: "Instructions for the upstream workflow: A compounding knowledge layer for sessions — a goal layer, a retrieved knowledge layer and a history layer filter every response, and a harvest step writes the session's learnings back into the local vector store, so a new session starts from retrieved memory instead of a re-injected history. Use when repeated sessions should accumulate knowledge rather than restart. Not for governed memory with sensitivity, visibility and a promote or forget lifecycle — use memory-hub; not for caching model responses — use response-cache; not for measuring the injected context — use context-profiler."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: hermes-second-brain
---
# Hermes Second Brain

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

> A self-learning system that filters every output through goals, business data,
> and history — getting smarter every session.

## Purpose

The design of a persistent knowledge loop: context before the session, vector
retrieval during it, harvest after it. The claimed benefit is a much smaller
per-session context because history is retrieved rather than re-injected.

The complete upstream architecture depends on `DESIGN.md`, which is not included here. Obtain compatible design documentation before treating the listed components as a deployed or working integration.

## Boundaries

- The claimed savings are design figures, not measured on the current tree.
- Retrieval quality is not the same as recall of the full history.

## When NOT to use

- You need memory with permissions and revocation — use memory_hub.
- You need a response cache — use response_cache.
