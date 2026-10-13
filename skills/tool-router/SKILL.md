---
name: tool-router
description: "Instructions for upstream tool specification, lexical routing, route validation and evaluation before adopting a heavier router. The runtime and fixtures are separate; use measured results rather than assuming token savings. Not for skill selection or model-tier choice."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: tool_router
---
# tool-router — choose a tool, locally

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Purpose

Selection primitives plus the evidence needed to trust them: specs, a lexical
router, a validator, seed evaluation cases and a benchmark that compares a
needle against a local model so a heavier router is only enabled when it wins.

    from skills.tool_router import LexicalToolRouter, ToolSpec, validate_route
    from skills.tool_router.benchmark import benchmark, build_seed_cases
    from skills.tool_router.needle_adapter import needle_activation_allowed

## When NOT to use

- You need a skill rather than a tool — use skill_finder.
- You need a tier — use nn_router.
