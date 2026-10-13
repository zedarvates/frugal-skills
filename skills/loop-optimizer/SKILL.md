---
name: loop-optimizer
description: "Instructions for the upstream workflow: Orchestrate a retroactive loop with token economy — a controller that picks the next loop action from extracted features, tracks progress state and stop reasons, and can replay a baseline loop to compare against the optimized one. Use when an iterate-until-done loop must be bounded and its cost measured rather than left to a fixed iteration count. Not for the persistent windows a loop reads — use context-windows; not for distilling what the loop learned — use agent-intel; not for running the loop's sub-agents — use the agent delegation surface."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: loop_optimizer
---
# loop-optimizer — bounded retroactive loops

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Purpose

Decides, from observable features, what the loop should do next and when to
stop, and can replay a recorded baseline to quantify the difference.

    python -m skills.loop_optimizer.cli <action> ...
    python -m skills.loop_optimizer.cli replay
    python -m skills.loop_optimizer.cli stats

## When NOT to use

- You need the context a loop carries between steps — use context_windows.
- You want the loop's knowledge distilled — use agent_intel.
- You want a single task routed — use nn_router or local_router.
