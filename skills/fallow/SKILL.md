---
name: fallow
description: "Static analysis for JS/TS codebases through the external Fallow CLI — health score with hotspots, dead code, semantic duplication, circular dependencies, PR risk from a diff, and JSON export, plus the Python companion and the combined audit script. Use when auditing a JS/TS project. Fallow is a third-party Rust binary: treat its report as an input to an audit, not as a proof on its own. Not for Python structural analysis — use the code_* detectors; not for the coding rules themselves — use code-rules."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: fallow
---
# Fallow — JS/TS codebase intelligence

> Static analysis for JS/TS projects. External CLI, zero runtime dependencies.

## Purpose

How to run the external analyser on a JS/TS tree and how to read its score bands
(A healthy through F critical), for the same family of questions the local
code_* detectors answer for Python.

Read the commands, the score table and the pitfalls in [RULES.md](RULES.md).

## Boundaries

- It is a third-party binary installed separately; its availability is not
  guaranteed by this repository.
- Its findings have the same status as any detector output: an input to review,
  never a substitute for the evidence a change actually works.

## When NOT to use

- The tree is Python — use code_complexity, code_duplication, code_state and
  code_wrappers.
- You want the coding standards — use code-rules.
