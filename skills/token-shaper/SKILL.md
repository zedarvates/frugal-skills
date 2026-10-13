---
name: token-shaper
description: "Instructions for selecting an upstream per-turn shaping policy: compression level, output target and verbosity. Verify the runtime and measure task quality and costs. Not for actually compressing a payload or measuring the always-on prefix."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: token_shaper
---
# token-shaper — per-turn shaping policy

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Purpose

Maps a query and an agent profile to a shaping configuration: level,
compression ratio, output token target and verbosity steering. The decision is
rule-based and local, so choosing the effort costs no cloud tokens.

## When NOT to use

- You actually want the compressed bytes — use universal_compressor.
- You want to know how much context is already spent before work starts —
  use context_profiler.

## Usage

```bash
python -m skills.token_shaper.cli --help
```
