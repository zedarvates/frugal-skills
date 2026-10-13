---
name: nn-router
description: "Instructions for the upstream workflow: Estimate a task's complexity and route it to the right model tier, with batch routing and routing statistics (route, batch_route, routing_stats, estimate_complexity). Use when the question is which tier a task deserves. Not for choosing the local host that will serve it — use local-router; not for choosing among tools — use tool-router or skill-finder; not for running a trained classifier on numeric features — use botte-nn."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: nn_router
---
# nn-router — complexity to tier

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Purpose

Scores a task's complexity and returns the model tier to use, with helpers for
batches and for aggregate statistics over a set of routing decisions.

    from skills.nn_router import route, batch_route, routing_stats, estimate_complexity

## When NOT to use

- You need local versus cloud placement — use local_router.
- You need one tool chosen — use tool_router.
- You have a trained model and numeric features — use botte_nn.
