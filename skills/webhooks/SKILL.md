---
name: webhooks
description: "Minimal HTTP endpoint that exposes the router to no-code workflows — a POST route that takes a prompt and a task type and returns the routing decision as JSON, on a configurable port. Use to let an external workflow system (n8n and similar) call the router without importing Python. Boundary: the listener binds all interfaces and performs no authentication, so it must stay on a trusted local network and is not a public entry point. Not for the routing decision itself — use auto-router; not for a general HTTP surface — see the module registration pattern in code-rules."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: webhooks
---
# webhooks — expose the router to no-code workflows

## Purpose

A single endpoint so a workflow tool can ask for a routing decision.

    python -m skills.webhooks.n8n_endpoint --port 8769
    POST /auto_route   {"prompt": "...", "task_type": "..."}

## Declared boundary

- Binds 0.0.0.0 by default and has no authentication. Do not expose it beyond a
  trusted local network; prefer an explicit loopback binding when only the local
  machine needs it.
- It is a thin adapter: all logic stays in auto_router.

## When NOT to use

- You are inside Python already — call auto_router directly.
- You need a public or authenticated API — this is not one.
