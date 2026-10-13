---
name: context-windows
description: "Guidance for upstream named context windows and loop deltas (step, merge, stats). Use to plan context reuse across iterations; verify the separately installed store and its invalidation rules. Not for per-agent prompt-prefix differences (prefix-tree) or file-analysis caching (code-fingerprint)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: context_windows
---
# context-windows — load the delta, not the loop

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## Purpose

Keeps named windows of context alive across the steps of a retroactive loop, so
a turn loads the changed deltas or a merged window rather than the full body.

## When NOT to use

- The prefix is stable per agent and you want agent-to-agent diffing —
  use prefix_tree.
- The repeated cost is re-analyzing unchanged code — use code_fingerprint.
- The wasted cost is a repeated prompt in event logs — use prompt_repetition.

## Usage

```bash
python -m skills.context_windows.cli --help
```
