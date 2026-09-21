---
name: tiered-router
description: "Five-level model selection with cost estimation and automatic downgrade — a free level served by local accelerators and pure computation, a local model level, then cheap, standard and premium cloud levels, each with its token and cost estimate produced before the call. Use before an LLM call when the cost of the chosen tier must be known and over-provisioning must be corrected automatically. Not for the micro-NN complexity router — use nn-router; not for placing a task on local hardware by task type — use local-router."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: tiered_router
---
# Tiered Model Router (P14)

## When NOT to use

- You want the classifier-driven tier decision rather than the 5-level cost
  ladder — use nn_router.
- You want a task placed on local hardware by its type — use local_router.
5-level intelligent model selection with cost estimation and auto-downgrade.

**Trigger:** Before EVERY LLM call — route through tiered router first.

**5 Levels:**
```
L0 FREE (0 tok):    Hailo-8, LocalAI TTS/STT, pure math/vectors
L1 LOCAL (~100 tok): LocalAI Gemma-4 / Ollama — simple Q&A
L2 CHEAP (~500 tok): Cloud small — code review, bug detection
L3 STANDARD (~2K tok): Cloud standard — architecture, complex reasoning
L4 PREMIUM (~8K tok): Cloud best — security audit, system design
```

**Features:**
- Cost estimation before call (tokens + $)
- Auto-downgrade when budget exceeded
- Per-project daily/monthly budget limits
- Usage tracking + savings report
- Agent-to-agent delta compression

**Module:** `skills/tiered_router`
**Typical savings:** 95-99% vs all-PREMIUM
