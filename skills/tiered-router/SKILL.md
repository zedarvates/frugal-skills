---
name: tiered-router
description: "Instructions for upstream model-tier planning using task requirements, configured endpoints, usage estimates and budgets. Local computation also has hardware and operating costs; measure actual provider usage. Not for micro-model classification or task-type hardware placement."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: tiered_router
---
# Tiered Model Router (P14)

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## When NOT to use

- You want the classifier-driven tier decision rather than the 5-level cost
  ladder — use nn_router.
- You want a task placed on local hardware by its type — use local_router.
5-level intelligent model selection with cost estimation and auto-downgrade.

**Trigger:** When the task calls for model-tier planning; do not override the host's model selection or the user's task scope automatically.

**5 Levels:**
```
L0 COMPUTATION: configured local algorithms or adapters
L1 LOCAL:       configured local model for suitable tasks
L2 CHEAP:       configured small hosted model
L3 STANDARD:    configured general hosted model
L4 PREMIUM:     configured higher-capability hosted model
Actual input/output tokens, quality and costs must be measured.
```

**Features:**
- Cost estimation before call (tokens + $)
- Auto-downgrade when budget exceeded
- Per-project daily/monthly budget limits
- Usage tracking + savings report
- Agent-to-agent delta compression

**Module:** `skills/tiered_router`
**Measurement:** compare actual quality and costs with an explicit baseline; no typical savings are established here.
