---
name: ultra-compact
description: "Instructions for upstream compact JSON report formats: short keys, arrays and deltas. Use only with a compatible decoder and retained baseline, and verify round-trip data and measured size. Not for prose compression or binary inter-agent transport."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: ultra_compact
---
# Ultra-Compact JSON (P12)

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.
Three compression levels: single-char keys, array format, delta-only.

**Trigger:** When the consumer supports the chosen format and the original data can be reconstructed. Prefer normal JSON when compatibility or a baseline is unavailable.

**Levels:**
1. Single-character keys with a shared field map.
2. Array format with an agreed field order.
3. Delta-only updates with an available baseline.

Compare actual sizes and verify round-trip data; these forms do not guarantee smaller model-token usage.

**Module:** `skills/ultra_compact`
**Functions:** to_ultra(), to_array(), delta_only(), compare_sizes()
