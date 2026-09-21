---
name: agent-intel
description: "The cross-cutting learning layer — record a retroactive loop for distillation, select the skills a task needs (skill RAG), predict the cost of a fix, compress accumulated agent memory, predict the agent route, and distill knowledge across loops, with aggregate stats (loop-distill, skill-rag, predict-fix, mem-compress, predict-route, distill, stats). Use when the question spans several loops or sessions rather than one run. Not for scanning session logs for recurring failures and correcting them — use botte-learn; not for routing one task to local hardware — use local-router; not for choosing among tools — use tool-router."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: agent_intel
---
# agent-intel — loop distillation, skill RAG, predictive routing

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
