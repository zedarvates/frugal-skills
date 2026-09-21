---
name: memory-hub
description: "The governed agent memory store — searchable entries with context bundles and an explicit propose, promote and forget lifecycle, typed assets, sensitivity levels and visibility, exposed as MCP tools whose access checks can refuse a read. Use when durable agent memory must be inspectable, permissioned and revocable rather than implicit. Not for caching model responses — use response-cache; not for compressing an in-flight message — use agent-compression or universal-compressor; not for scanning sessions for failure patterns — use botte-learn."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: memory_hub
---
# memory-hub — governed, revocable agent memory

## Purpose

A versioned store for durable memories, with the full lifecycle made explicit:
propose, promote, forget. Entries carry a type, a sensitivity level and a
visibility, and MCP access can raise rather than silently return data.

    MCP tools: search_hub, context_bundle, propose_memory, promote_memory, forget_memory

## When NOT to use

- You want a response cached — use response_cache.
- You want a payload compressed — use universal_compressor.
- You want failure patterns mined from logs — use botte_learn.
