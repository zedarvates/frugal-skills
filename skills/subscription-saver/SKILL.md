---
name: subscription-saver
description: "Fail-closed evidence and planning contracts for self-hosting decisions — a validated catalogue with digest, capability coverage evaluation, inventory import and export, upstream source auditing, recommendation carrying its own evidence, deployment profiles and states, install plans and TCO scenarios. Use when a self-hosting or subscription decision must be justified by evidence rather than asserted. A recommendation fails closed when coverage or provenance is missing. Not for auditing code structure — use the code_* detectors; not for the token cost of a project — use context-profiler or cost-estimator."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: subscription_saver
---
# subscription-saver — evidence, not assertion

## Purpose

Produces a plan whose every step is traceable: what capability is required,
what the catalogue covers, what the source audit found, what the deployment
profile assumes, and what the resulting cost range is. Missing evidence blocks
the recommendation instead of defaulting to a favourable answer.

    from skills.subscription_saver import (
        catalog_digest, load_catalog, validate_catalog,
        evaluate_coverage, audit_source, recommend, ...
    )

## When NOT to use

- You want static code analysis — use the code_* detectors.
- You want a project token cost — use context_profiler.
