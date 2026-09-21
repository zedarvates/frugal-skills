---
name: botte-learn
description: "Analyse recorded sessions for recurring failure patterns and turn them into correction rules that can be applied back, with a status view (scan, apply, status). Use when the same mistake keeps coming back and you want a learned, repeatable correction rather than another one-off fix. Not for distilling a whole loop into reusable knowledge — use agent-intel (loop-distill); not for detecting structural code smells — use the code_* detectors; not for governed long-term memory — use memory-hub."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: botte_learn
---
# botte-learn — from repeated failures to correction rules

## Purpose

Scans session logs, extracts observed failure patterns, and proposes learned
rules that can then be applied, so a recurring error is fixed once as a rule
instead of once per occurrence.

    python -m skills.botte_learn.cli scan
    python -m skills.botte_learn.cli apply
    python -m skills.botte_learn.cli status

## When NOT to use

- You want the loop distilled rather than the failures corrected — use agent_intel.
- The smell is in the code structure, not in a session — use the code_* detectors.
- You want durable, revocable memory — use memory_hub.
