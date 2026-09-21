---
name: token-compressor
description: "Compress the token structure itself, not the content — semantic hashing of repeated patterns, byte-pair pruning, repeated-JSON-schema compression and n-gram dedup, backed by a learned n-gram frequency table. Deterministic, pure stdlib, 0 cloud tokens. Use when the same structural patterns repeat across many payloads and the payload shape is the cost driver. Not for the per-turn verbosity policy — use token-shaper; not for content-type compression of logs or tool output — use universal-compressor; not for the agent-to-agent wire format — use agent-compression."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: token_compressor
---
# token-compressor — compress the structure, not the content

## Purpose

Reduces the *token structure* of repeated payloads: patterns seen often are
replaced by hashes, the most frequent byte pairs are pruned, repeated JSON
schemas are factored, and n-grams are deduplicated using a frequency table
learned from a corpus.

## When NOT to use

- The payload is a log, a tool output or code and you want fewer bytes —
  use universal_compressor (content-type strategies).
- You need to decide compression level, ratio and output length for a turn —
  use token_shaper.
- Two agents exchange messages and you want a binary wire format —
  use agent_compression.

## Usage

```bash
python -m skills.token_compressor.cli --help
```
