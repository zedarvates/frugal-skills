---
name: pipeline-integrator
description: "Integration, monitoring and meta-optimisation across the module set — health check, module heal, agent sync, budget optimisation, module registration and an integration report (health, optimize, sync, heal, budget, register, integrate). Use when the question is whether the assembled pipeline is coherent rather than whether one module works. Not for the per-module read-only checkup — use checkup; not for the token cost of one project — use context-profiler or cost-estimator."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: pipeline_integrator
---
# pipeline-integrator — is the assembled pipeline coherent?

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
