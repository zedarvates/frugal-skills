---
name: nn-router
description: "Estimate a task's complexity and route it to the right model tier, with batch routing and routing statistics (route, batch_route, routing_stats, estimate_complexity). Use when the question is which tier a task deserves. Not for choosing the local host that will serve it — use local-router; not for choosing among tools — use tool-router or skill-finder; not for running a trained classifier on numeric features — use botte-nn."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: nn_router
---
# nn-router — complexity to tier

## Purpose

Scores a task's complexity and returns the model tier to use, with helpers for
batches and for aggregate statistics over a set of routing decisions.

    from skills.nn_router import route, batch_route, routing_stats, estimate_complexity

## When NOT to use

- You need local versus cloud placement — use local_router.
- You need one tool chosen — use tool_router.
- You have a trained model and numeric features — use botte_nn.
