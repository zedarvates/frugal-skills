---
name: diff-language
description: "A compact, agent-native notation for describing code changes and findings, with severity markers and operation markers in one line, lossless round-trip parsing and serialization, and a reported 47 to 55 percent saving over verbose markdown. Use when emitting fix reports, diffs or audit findings for a model to read. Not for compacting structured report JSON — use ultra-compact; not for reducing free text — use universal-compressor."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: diff_language
---
# Diff Language

## When NOT to use

- The payload is a structured report object — use ultra_compact.
- The payload is free text, a log or code — use universal_compressor.
Compact agent-native diff format for token-efficient code change descriptions.

**Trigger:** When generating diffs, fix reports, or audit findings.

**Format:** `!!+f:file.py:42:symbol:detail`
- Severity: !! (crit), ! (err), ~ (warn), . (info)
- Ops: +f (fix), -f (skip), +d (dead), +s (secret), +p (dup), +c (complex)

**Module:** `skills/diff_language`

**Savings:** 47-55% vs verbose markdown
**Roundtrip:** lossless parse + serialize
