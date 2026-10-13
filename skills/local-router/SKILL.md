---
name: local-router
description: "Instructions for matching tasks to separately configured local text, vision, speech or image capabilities. Verify hardware, models and endpoint availability before routing. Not for choosing a model tier, selecting a tool or performing media extraction."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: local_router
---
# local-router — prefer local over cloud

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Purpose

Classifies a task by type and routes it to the local capability that can serve
it (vision accelerator, local text and voice endpoint, local image endpoint),
keeping the paid path for what actually needs it.

    from skills.local_router import ...

Tasks and hardware are declared as an enum, so an unavailable capability is
visible rather than silently escalated to a cloud call.

## When NOT to use

- The question is which model tier, not which host — use nn_router.
- The question is which tool to call — use tool_router.
- You have raw media to prepare — use media_loader first.
