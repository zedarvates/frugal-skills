---
name: diff-language
description: "Instructions for a compact notation for code changes and findings with severity and operation markers. Verify the installed parser and round-trip behavior before using it as a report format. Not for JSON report compaction or general content compression."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: diff_language
---
# Diff Language

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## When NOT to use

- The payload is a structured report object — use ultra_compact.
- The payload is free text, a log or code — use universal_compressor.
Compact agent-native diff format for token-efficient code change descriptions.

**Trigger:** When generating diffs, fix reports, or audit findings.

**Format:** `!!+f:file.py:42:symbol:detail`
- Severity: !! (crit), ! (err), ~ (warn), . (info)
- Ops: +f (fix), -f (skip), +d (dead), +s (secret), +p (dup), +c (complex)

**Module:** `skills/diff_language`

**Measurement:** compare actual encoded sizes and verify the installed parser round-trip; no fixed reduction is established here.
**Roundtrip:** lossless parse + serialize
