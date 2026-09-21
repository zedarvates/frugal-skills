---
name: universal-compressor
description: "Compress content by type — text, JSON, logs, tool output and code — through dedup, truncation and pattern sampling, with 40 to 90 percent typical savings, reversible in memory or through an explicit bounded store with atomic writes, integrity checks, TTL and size limits; usable as a library, a CLI or an MCP server. Use when a large payload must fit a context window before an agent reads it. Not for the agent-to-agent binary wire format — use agent-compression; not for repeated-structure hashing — use token-compressor; not for deciding the per-turn policy — use token-shaper."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: universal_compressor
---
# Universal Compressor

Headroom-inspired multi-type compression for botte-secrete. Reduces token usage by 40-90% depending on content type. Works as library, CLI, or MCP server.

## Strategies

| Content Type | Strategy | Typical Savings |
|---|---|---|
| `text` | Dedup lines, collapse blanks | 0-30% |
| `json` | Compact + truncate large arrays | 20-60% |
| `log` | Pattern dedup + sampling | 80-98% |
| `tool_output` | Head+tail, strip ANSI | 50-90% |
| `code` | Strip comments, collapse imports | 20-40% |
| `auto` | Auto-detect content type | Best effort |

## Usage

```python
from skills.universal_compressor import compress, restore

# Compress with auto-detection
result = compress(content)
print(f"{result.original_size} → {result.compressed_size} ({result.ratio:.0%})")

# Compress with type hint + reversibility
result = compress(big_log, content_type="log", reversible=True)

# Restore original
original = restore(result.reversible_key)

# Durable restoration is opt-in because originals may contain secrets.
result = compress(big_log, content_type="log", reversible=True,
                  reversible_store=".botte-private/compressor", ttl_seconds=3600)
original = restore(result.reversible_key, store_path=".botte-private/compressor")
```

Sizes are UTF-8 bytes. Reversible keys are full-content SHA-256 hashes. Durable
entries use atomic writes, integrity checks, a 1-hour default TTL (maximum 7
days), and an 8 MiB default size limit. No original is written to disk unless
`reversible_store` is supplied explicitly.
