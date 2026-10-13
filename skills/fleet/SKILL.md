---
name: fleet
description: "Instructions for the upstream workflow: Aggregate status across the fleet, sortable by project tokens saved, lines of code or number of fixes — a read-only view over the canonical fleet registry that the dashboard writes. Use when you need a portfolio-level roll-up across projects. This module deliberately reads the dashboard registry instead of keeping its own, so the two can no longer diverge. Not for editing the registry — use dashboard (fleet add); not for measuring one project's context cost — use context-profiler."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: fleet
---
# fleet — portfolio roll-up, read-only

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Purpose

A single view over the fleet registry, sorted on demand. It used to keep its own
registry under ~/.botte/fleet, which silently diverged from the one dashboard
wrote; it now reads the canonical source.

    python -m skills.fleet.status --sort project_tokens_saved
    python -m skills.fleet.status --sort loc
    python -m skills.fleet.status --sort fixes

## When NOT to use

- You need to add or change a fleet entry — use dashboard.
- You need one project's prefix cost — use context_profiler.
