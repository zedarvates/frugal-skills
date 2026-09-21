---
name: token-shaper
description: "Decide the per-turn shaping policy for a query and an agent profile — compression level, compression ratio, output token target and verbosity steer — so the effort matches the task instead of being fixed. Deterministic, 0 cloud tokens. Use when you need to answer how much to compress and how long the answer should be for one specific turn. Not for compressing a payload — use universal-compressor (content) or token-compressor (structure); not for measuring the always-on prefix — use context-profiler."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: token_shaper
---
# token-shaper — per-turn shaping policy

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
