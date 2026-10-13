---
name: agent-intel
description: "Guidance for upstream learning across loops: distillation, skill retrieval, fix-cost and route estimates, memory compression and aggregate statistics. Use for questions spanning runs or sessions. Not for recurring-failure correction (botte-learn), local hardware placement (local-router) or tool selection (tool-router)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: agent_intel
---
# agent-intel — loop distillation, skill RAG, predictive routing

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## Purpose

Aggregates what individual runs learned: loops are recorded and distilled,
skills are selected for a task by retrieval, fix cost and agent route are
predicted from history, and agent memory is compressed.

    python -m skills.agent_intel.cli loop-distill
    python -m skills.agent_intel.cli skill-rag
    python -m skills.agent_intel.cli predict-fix
    python -m skills.agent_intel.cli predict-route
    python -m skills.agent_intel.cli distill
    python -m skills.agent_intel.cli stats

## When NOT to use

- You want failure patterns turned into correction rules — use botte_learn.
- You want to send a task to local hardware — use local_router.
- You want a tool chosen for one call — use tool_router or skill_finder.
