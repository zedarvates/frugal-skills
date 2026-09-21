---
name: code-rules
description: "Token-efficient coding standards — the three taxes to weigh before adding any dependency (latency, security surface, cold start), stdlib-first choices, flat architecture, data-oriented layout, the scale-based datastore table, the module registration pattern for extending an http.server without touching the core, a hard per-file line limit, and verification before announcement. Use before adding a dependency, choosing a datastore, adding a layer, or splitting a file. Not for detecting smells in existing code — use the code_* detectors; not for the agent-facing anti-pattern checklist — use karpathy-guidelines."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code-rules
---
# Code Rules — token-efficient coding standards

> "The best optimization is subtraction."

## Purpose

The standing rules for this codebase. They are constraints to apply while
writing, not a report to generate afterwards.

Key content:
- **Three taxes** before any dependency: latency, security surface, cold start.
- **stdlib first**, with the named defaults (http.server, sqlite3 in WAL mode,
  pathlib, dataclasses with slots, lru_cache).
- **Flat architecture**: route -> handler -> datastore, no abstraction circles.
- **Data-oriented design**: column-oriented batching for hot paths.
- **Datastore choice by scale** (SQLite WAL -> pgvector -> Qdrant -> Milvus).
- **Module registration**: each module exposes register(db_path) so the core is
  never edited to add a feature.
- **File size hard limit**: no single source file beyond the stated ceiling.
- **Verification before announcement**: never announce a result without having
  observed it yourself (service answers on its port, file exists and was read,
  process running and responding).

The full text is in [RULES.md](RULES.md).

## When NOT to use

- You want structural smells found in existing code — use code_complexity,
  code_duplication, code_state or code_wrappers.
- You want the review checklist for a change in progress — use karpathy-guidelines.
