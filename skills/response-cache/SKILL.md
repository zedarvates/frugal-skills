---
name: response-cache
description: "Instructions for the upstream ResponseCache exact query/model/context lookup and optional lexical word-overlap matching. The main cache does not implement a semantic vector service. Use only when cached output remains valid for the context; not for durable governed memory or project-scan caching."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: response_cache
---
# response-cache — exact identity and optional lexical candidates

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Current upstream behavior

The main `skills.response_cache.ResponseCache` implementation stores entries in a local cache. Exact identity includes the query text with whitespace preserved, model and context. Its optional `get_semantic()` path is named semantically but currently computes word-set overlap; it does not call a vector database or learned embedding service. A separate experimental `semantic_cache.py` should not be confused with this main API.

Use exact caching only when the result remains valid for its inputs, dependencies, permissions and environment. Treat lexical matches as candidates: high word overlap does not prove the same meaning, context, authorization or correct answer. Verify them before reusing a response, particularly for changing state or sensitive questions. A miss does not automatically authorize a paid model call.

## Workflow

1. Inspect the compatible installed cache API and its configuration.
2. Include all response-relevant context in exact identity or invalidate when it changes.
3. Keep lexical reuse opt-in and validate candidate applicability; otherwise recompute within the user's task scope.
4. Report actual hit/miss counters separately from measured provider usage. No percentage saving is established by this catalog.

## When NOT to use

- For project-scan results keyed by fingerprints, consider agent-cache.
- For durable memory with lifecycle, sensitivity and permissions, consider memory-hub.
- For claims of semantic paraphrase equivalence or a working Qdrant integration, require a separately verified implementation.
