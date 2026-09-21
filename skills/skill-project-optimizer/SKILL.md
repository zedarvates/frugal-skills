---
name: skill-project-optimizer
description: "Build a standing per-project skill profile — scan the available skills, profile what a given project actually needs, and emit a .skills-profile splitting skills into always, conditional and disabled, for a reported 73 to 83 percent reduction of the skill-shaped token cost. Deterministic and local, 0 cloud tokens. Use when starting work on a new project, or when the token cost of the loaded skill set is too high and the fix is a project-level decision. Not for picking skills for one specific query — use skill-finder; not for measuring the whole always-on prefix — use context-profiler; not for choosing a subset under an explicit budget — use context-budget."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: skill_project_optimizer
---
# Skill Project Optimizer

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
**Savings:** 73-83% token reduction
