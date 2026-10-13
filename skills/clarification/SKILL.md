---
name: clarification
description: "Guidance for asking up to five targeted questions with explicit defaults when scope is ambiguous or a wrong assumption would be expensive. Explicit auto may accept optional defaults; silence is not approval for a blocking decision. Not for precondition checks (preflight) or choosing known implementation options (decision-ladder)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: clarification
---
# Clarification Proactive

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## When NOT to use

- You need preconditions verified rather than requirements asked — use preflight.
- The decision is a choice between known options — use decision-ladder.
Ask up to five targeted numbered questions when unresolved scope materially affects the work. State a default for optional questions; explicit "auto" accepts those defaults. Silence does not answer a blocking question or authorize an action.

**Trigger:** At the start of an ambiguous workflow when the answer affects scope, correctness or a required decision. Honor established user instructions and avoid repeating resolved questions.

**Pattern:**
```
🤔 [Agent] — Clarifications pour [étape]
1. 🔴 Question bloquante ? (défaut: X)
2. 🟡 Question secondaire ? (défaut: Y)
Réponds avec les numéros ou "auto"
```

**Module:** `skills/clarification`
**Generators:** portos_clarify(), dartagnan_clarify(), aramis_clarify(), etc.
**Rule:** For optional questions, use an authorized default and flag `⚠️ Hypothèse: [valeur]`. Keep required answers or approvals pending; elapsed time is not approval.
