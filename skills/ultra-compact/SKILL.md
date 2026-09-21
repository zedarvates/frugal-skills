---
name: ultra-compact
description: "Compact JSON report wire format for agent-facing reports — three levels: single-char keys (about -30 percent versus compact JSON), keyless array format, and delta-only patches for iterative reports (about -90 percent), plus a size comparison helper. Use when emitting audit, checkup or telemetry JSON that an agent or a local model will read back. Not for logs, free text or code — use universal-compressor; not for the agent-to-agent wire format — use agent-compression."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: ultra_compact
---
# Ultra-Compact JSON (P12)
Three compression levels: single-char keys, array format, delta-only.

**Trigger:** When generating JSON reports — always use the most compact format.

**Levels:**
1. Single-char keys: -30% vs standard compact
2. Array format (no keys): -38% vs compact
3. Delta-only (send changes): -90% for iterative reports

**Module:** `skills/ultra_compact`
**Functions:** to_ultra(), to_array(), delta_only(), compare_sizes()
