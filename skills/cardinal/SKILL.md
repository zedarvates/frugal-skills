---
name: cardinal
description: "Instructions for an upstream adversarial review workflow with counter-auditor, counter-developer, counter-optimizer and verdict orchestration. Use to challenge an existing result on critical work. Not for producing the first audit or fixes (mousquetaires), or mechanically reviewing one diff (simplify-code)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: cardinal
---
# Les Mousquetaires du Cardinal — Red Team

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## When NOT to use

- You need the first pass that produces the work being challenged — use mousquetaires.
- You need one diff reviewed and simplified — use simplify-code.
- You need static findings rather than a challenge — use code_* or fallow_like.
Adversarial agents that challenge the Blue Team's work.

**Trigger:** After Blue Team pipeline, for critical code or health < 70.

**Agents:**
- 🗡️ Rochefort: Counter-auditor (finds what Porthos missed)
- 🔪 Milady: Counter-developer (finds what d'Artagnan broke)
- 🕯️ Comte de Wardes: Counter-optimizer (finds over-optimizations)
- 👑 Le Cardinal: Orchestrator (coordinates, verdict)

**Workflow:** `rochefort ∥ milady ∥ comte_de_wardes → cardinal`

**Module:** `skills/cardinal`
**Upstream pre-prompts:** `skills/cardinal/prompts/` + `skills/core-agent.md`; these resources are not bundled in this catalog. Obtain and review a compatible upstream version before attempting the named pipeline.
