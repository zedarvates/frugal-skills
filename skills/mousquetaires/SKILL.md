---
name: mousquetaires
description: "Instructions for the upstream workflow: The blue team pipeline — audit, fix, optimize, consolidate — with an auditor agent, a developer agent, an optimizer agent and an orchestrator, exposed as a CLI over a project. Use when the user wants a code audit, automated fixes or token optimization across a project. Not for challenging an existing result — use cardinal; not for the five-field policy findings alone — use the code_* detectors."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: mousquetaires
---
# Les Quatre Mousquetaires — Blue Team

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## When NOT to use

- You want the produced work attacked before it is trusted — use cardinal.
- You want only the policy findings — use the code_* detectors.
Multi-agent pipeline: Audit → Fix → Optimize → Consolidate.

**Trigger:** When the user wants code audit, automated fixes, or token optimization.

**Agents:**
- 🥊 Porthos: Auditor (fallow-like analyzers)
- ⚔️ d'Artagnan: Developer (auto-fix)
- 📿 Aramis: Optimizer (token reduction)
- 👑 Athos: Orchestrator (pipeline coordination)

**Workflow:** `porthos ∥ aramis → dartagnan → athos`

**Module:** `skills/mousquetaires`
**CLI:** `python3 -m skills.mousquetaires.cli run <project> --output <dir>`
**Pre-prompts:** `skills/mousquetaires/prompts/` + `skills/core-agent.md`
