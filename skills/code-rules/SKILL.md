---
name: code-rules
description: "Guidance for evaluating dependencies, standard-library options, flat architecture, data layout, datastore choices and verification before announcing results. Use before adding a dependency or layer. The full upstream RULES.md and any project-specific file limit are separate prerequisites; do not invent a missing ceiling."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: code-rules
---
# Code Rules — token-efficient coding standards

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

> "The best optimization is subtraction."

## Purpose

These are summarized upstream coding principles to consider while writing. Apply the current project's governing instructions and inspect the full compatible upstream resource before imposing any additional project-specific limit.

Key content:
- **Three taxes** before any dependency: latency, security surface, cold start.
- **stdlib first**, with the named defaults (http.server, sqlite3 in WAL mode,
  pathlib, dataclasses with slots, lru_cache).
- **Flat architecture**: route -> handler -> datastore, no abstraction circles.
- **Data-oriented design**: column-oriented batching for hot paths.
- **Datastore choice by scale** (SQLite WAL -> pgvector -> Qdrant -> Milvus).
- **Module registration**: each module exposes register(db_path) so the core is
  never edited to add a feature.
- **File size limit**: inspect the actual governing rule before asserting a ceiling; this summary contains no verified numeric limit.
- **Verification before announcement**: never announce a result without having
  observed it yourself (service answers on its port, file exists and was read,
  process running and responding).

The full `RULES.md` is a separate upstream workflow resource, not included in this catalog. Obtain the compatible upstream text before relying on omitted tables, commands or limits; if it is unavailable, report that limitation and use only the summary above.

## When NOT to use

- You want structural smells found in existing code — use code_complexity,
  code_duplication, code_state or code_wrappers.
- The upstream `karpathy-guidelines` neighbour is excluded from this catalog pending provenance review; do not assume it is installed.
