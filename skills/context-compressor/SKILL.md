---
name: context-compressor
description: "Instructions for the legacy upstream log-pattern compressor: repetitions, common patterns and sampled distinct lines. Use only for existing callers while consolidation is pending; universal-compressor with log content is the suggested path for new work. No measured reduction is established by this catalog."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: context_compressor
---
# context-compressor — log pattern reduction (consolidation pending)

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## Purpose

Turns a large log into a compact summary: how many lines became how many unique
patterns, the most frequent patterns with their counts, and a sample of the
distinct lines.

    python -m skills.context_compressor.compress <logfile> [--max-lines 200]

## Status

This is a narrow, single-file module whose only strategy — log pattern dedup —
is also described by universal_compressor under content_type "log", including an optional reversible mode. Verify the installed implementation and any claimed reduction with representative input. The declared direction is consolidation
into universal_compressor; until that happens, this entry exists so the module
is routable rather than invisible.

## When NOT to use

- New work: use universal_compressor with content_type "log".
- The payload is not a log — use universal_compressor.
- You need reversibility — use universal_compressor (reversible store).
