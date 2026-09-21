---
name: clarification
description: "Ask up to five numbered questions before starting work, with a declared default per question so silence auto-fills and the assumption is flagged rather than hidden — one blocking question and secondary ones, answered by number or with auto. Use at the start of a workflow whose scope is ambiguous or where a wrong assumption would be expensive. Not for checking preconditions before acting — use preflight; not for choosing between two implementation paths — use decision-ladder."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: clarification
---
# Clarification Proactive

## When NOT to use

- You need preconditions verified rather than requirements asked — use preflight.
- The decision is a choice between known options — use decision-ladder.
Up to 5 numbered questions before starting work. Silence = auto-fill with defaults.

**Trigger:** At the START of every agent's workflow (OBLIGATOIRE).

**Pattern:**
```
🤔 [Agent] — Clarifications pour [étape]
1. 🔴 Question bloquante ? (défaut: X)
2. 🟡 Question secondaire ? (défaut: Y)
Réponds avec les numéros ou "auto"
```

**Module:** `skills/clarification`
**Generators:** portos_clarify(), dartagnan_clarify(), aramis_clarify(), etc.
**Rule:** Silence = auto → fill defaults → flag `⚠️ Hypothèse: [valeur]`
