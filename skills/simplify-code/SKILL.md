---
name: simplify-code
description: "A three-reviewer parallel pass over a diff — one reviewer on code reuse, one on quality, one on efficiency, each receiving the whole diff and required to cite file:line evidence — then findings are merged, false positives discarded, conflicts resolved by a stated priority order, fixes applied scoped to the diff, and targeted tests and linter run. Use when asked to simplify, clean up or review recent changes. Not for detecting smells across a whole tree — use the code_* detectors; not for the conceptual rules — use code-rules or karpathy-guidelines."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: simplify-code
---
# Simplify Code — parallel three-agent review

> Three narrow reviewers beat one broad reviewer.

## Purpose

A review procedure for a change: identify the diff scope, launch exactly three
reviewers with disjoint concerns and the full diff each, then aggregate,
discard false positives, resolve conflicts, apply scoped fixes and verify.

Triggers: simplify, simplify my changes, review my code, review my recent
changes, clean up my changes.

Read the process and the pitfalls in [RULES.md](RULES.md).

## Boundaries

Reviewers must cite file:line and search rather than guess; the pass improves a
diff, it does not certify it.

## When NOT to use

- You want the whole tree analysed — use the code_* detectors.
- You want the standing rules — use code-rules.
