---
name: pipeline-integrator
description: "Instructions for the upstream workflow: Integration, monitoring and meta-optimisation across the module set — health check, module heal, agent sync, budget optimisation, module registration and an integration report (health, optimize, sync, heal, budget, register, integrate). Use when the question is whether the assembled pipeline is coherent rather than whether one module works. Not for the per-module read-only checkup — use checkup; not for the token cost of one project — use context-profiler or cost-estimator."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: pipeline_integrator
---
# pipeline-integrator — is the assembled pipeline coherent?

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Purpose

Meta-level view over the modules: registers them, checks their health, heals a
module, syncs agents and optimises the aggregate budget.

    python -m skills.pipeline_integrator.cli health
    python -m skills.pipeline_integrator.cli integrate
    python -m skills.pipeline_integrator.cli heal <module>
    python -m skills.pipeline_integrator.cli budget

## When NOT to use

- You want the read-only project checkup — use checkup.
- You want a cost figure for one project — use context_profiler.
