---
name: skill-project-optimizer
description: "Instructions for producing an upstream project skill profile with always, conditional and disabled entries. Measure project needs and context use before changing it; no fixed savings are established here. Not for one-query ranking, global prefix measurement or budget allocation."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: skill_project_optimizer
---
# Skill Project Optimizer

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Per-project skill filtering to reduce token waste.

## When NOT to use

- You need the right skill for one query, right now — use skill_finder.
- You want the full prefix cost, not just the skill part — use context_profiler.
- You have a budget and want an exact optimal subset — use context_budget.

**Trigger:** When starting work on a new project or when tokens are too high.

**Usage:**
```bash
python3 -m skills.skill_project_optimizer.cli scan
python3 -m skills.skill_project_optimizer.cli profile <project>
python3 -m skills.skill_project_optimizer.cli optimize <project>
python3 -m skills.skill_project_optimizer.cli compare <project>
```

**Module:** `skills/skill_project_optimizer`
**Output:** `.skills-profile` (always/conditional/disabled skills)
**Measurement:** compare loaded context and task quality with the original profile; this catalog supplies no fixed reduction.
