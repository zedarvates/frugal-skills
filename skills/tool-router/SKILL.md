---
name: tool-router
description: "Local-first tool routing primitives — tool specifications, a lexical router, a route validator, an evaluation harness with seed cases and a gate that activates a heavier router only when the needle actually beats the local model, plus a token estimator. Use when an agent must choose among many tools without spending cloud tokens on the choice, or when you want to benchmark a router before adopting it. Not for choosing a skill rather than a tool — use skill-finder; not for a model tier decision — use nn-router."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: tool_router
---
# tool-router — choose a tool, locally

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
