---
name: dynamic-workflows
description: "Orchestration patterns for efficient agents — classify and act, fan out and synthesize, adversarial verification, generate and filter, tournament — each addressing one of three failure modes: agent laziness (declares more than it does), self-preference (judging its own work) and goal drift (losing the objective in a long session). Use when designing or debugging a multi-agent workflow rather than a single call. Not for the retroactive-loop controller — use loop-optimizer; not for the parallel review of one diff — use simplify-code; not for delegating a task — use the agent delegation surface."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: dynamic-workflows
---
# Dynamic Workflows — patterns for efficient agents

## Purpose

A catalogue of composition patterns, each mapped to the failure mode it fixes.
The underlying idea is a harness per task: the shape of the orchestration should
match the task, not be fixed for everything.

Read the full set in [PATTERNS.md](PATTERNS.md).

## When NOT to use

- You need the loop controller and its stop reasons — use loop_optimizer.
- You need one diff reviewed by several narrow reviewers — use simplify-code.
