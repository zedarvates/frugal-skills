---
name: context-slicer
description: "Split one body of context into independent typed slices (code, doc, config, log, result, meta) by markdown headings and section markers, each with a token count, a priority and the task types it serves, then select only the slices relevant to a task type. Deterministic, 0 cloud tokens. Use when the same context must serve several agents or task types without every one loading everything. Not for choosing a subset under an explicit token budget — use context-budget; not for removing sections nobody uses — use prefix-pruner."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: context_slicer
---
# context-slicer — typed slices, loaded on demand

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
