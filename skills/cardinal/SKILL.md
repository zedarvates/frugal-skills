---
name: cardinal
description: "Adversarial red team that challenges the blue team's output — a counter-auditor, a counter-developer and a counter-optimizer run in parallel and an orchestrator issues the verdict, used after the blue team pipeline on critical code or when health is low. Use to attack a result before trusting it. Not for producing the first audit, fixes or optimizations — use mousquetaires; not for the mechanical review of one diff — use simplify-code."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: cardinal
---
# Les Mousquetaires du Cardinal — Red Team

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
**Pre-prompts:** `skills/cardinal/prompts/` + `skills/core-agent.md`
