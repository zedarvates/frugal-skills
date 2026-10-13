---
name: context-slicer
description: "Instructions for upstream typed context slicing by headings and markers, with token estimates, priorities and task-type selection. Use to plan how several agents can consume relevant portions of shared context. Not for explicit-budget selection (context-budget) or permanently pruning unused sections (prefix-pruner)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: context_slicer
---
# context-slicer — typed slices, loaded on demand

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## Purpose

An independent block of context that can be loaded or skipped on its own,
classified by type and priority, and selected per agent and per task type.

## When NOT to use

- The constraint is a token budget rather than a task type — use context_budget.
- You want to delete dead sections permanently — use prefix_pruner.
- Several agents share one large stable prompt prefix — use prefix_tree.

## Usage

```bash
python -m skills.context_slicer.cli --help
```
