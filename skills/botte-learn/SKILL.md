---
name: botte-learn
description: "Guidance for upstream recorded-session analysis and proposed correction rules (scan, apply, status). Use to investigate recurring failure patterns; validate each proposed rule before applying it. Not for loop distillation (agent-intel), structural code detection or governed long-term memory (memory-hub)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: botte_learn
---
# botte-learn — from repeated failures to correction rules

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## Purpose

Scans session logs, extracts observed failure patterns, and proposes learned
rules for review and possible application. A proposed rule is not proof that the recurring error is fixed; validate its effect against observed cases.

    python -m skills.botte_learn.cli scan
    python -m skills.botte_learn.cli apply
    python -m skills.botte_learn.cli status

## When NOT to use

- You want the loop distilled rather than the failures corrected — use agent_intel.
- The smell is in the code structure, not in a session — use the code_* detectors.
- You want durable, revocable memory — use memory_hub.
