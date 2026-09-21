---
name: context-compressor
description: "Compress a large log file before an agent reads it — collapse numeric, timestamp and UUID noise into patterns, count repetitions, keep the top patterns and a sample of unique lines, with a reported 80 percent reduction on log-analysis tasks. CONSOLIDATION PENDING: this overlaps the log strategy of universal-compressor (content_type log, 80 to 98 percent), which is the supported path for new work; this module is kept for existing callers only. Use when a log has to be reduced to its patterns and samples and universal-compressor is not available in the call site. Not for text, JSON, code or tool output — use universal-compressor; not for the token-structure level — use token-compressor."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: context_compressor
---
# context-compressor — log pattern reduction (consolidation pending)

## Purpose

Turns a large log into a compact summary: how many lines became how many unique
patterns, the most frequent patterns with their counts, and a sample of the
distinct lines.

    python -m skills.context_compressor.compress <logfile> [--max-lines 200]

## Status

This is a narrow, single-file module whose only strategy — log pattern dedup —
already exists in universal_compressor under content_type "log", with a larger
reported saving and a reversible mode. The declared direction is consolidation
into universal_compressor; until that happens, this entry exists so the module
is routable rather than invisible.

## When NOT to use

- New work: use universal_compressor with content_type "log".
- The payload is not a log — use universal_compressor.
- You need reversibility — use universal_compressor (reversible store).
