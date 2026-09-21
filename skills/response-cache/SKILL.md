---
name: response-cache
description: "Cache model responses so a repeated or similar query does not pay for a full call again — an exact hash check first, then semantic similarity through the local vector service, then the model as fallback, for a reported 60 percent saving on repetitive traffic. Use when the same or nearly the same question recurs. Not for caching a deterministic result keyed by code fingerprint — use agent-cache; not for governed, revocable long-term memory — use memory-hub; not for compressing the stored payload — use universal-compressor."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: response_cache
---
# response-cache — hash first, semantics second, model last

## Purpose

    Query -> exact hash check (fast) -> semantic similarity -> model (fallback)

Exact matches are cheap and deterministic; near matches go through the local
vector service so a paraphrase does not trigger a fresh paid call.

## When NOT to use

- The output is deterministic and keyed by code rather than by question —
  use agent-cache.
- You want memory with a lifecycle, sensitivity and permissions — use memory_hub.
