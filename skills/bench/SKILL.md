---
name: bench
description: "Instructions for the upstream routing benchmark and its fixed decision corpus. Use to inspect estimated routing costs against a declared baseline, or to plan reproducible evidence. Decision estimates are not measured provider bills, production savings or validation of this instruction catalog."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: bench
---
# bench — routing benchmark methodology

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

```bash
python -m skills.bench.cli            # table + totals
python -m skills.bench.cli --json
python -m skills.bench.cli --save md  # timestamped report under .botte/reports/
```

The upstream benchmark runs its fixed task corpus through `auto_router.decide()` and compares decision-based cost estimates with a declared Tier.STANDARD baseline. This is a routing simulation, not an execution of every provider call or measurement of actual bills. Record the installed corpus, cost-model version and baseline before interpreting the output.

## Why this exists

A reproducible benchmark needs a versioned corpus, explicit baseline and recorded controls. Use the separately installed upstream benchmark to compare estimates across changes, and actual measured replay evidence for claims about production usage or savings. Upstream integration proposals under `docs/plans/` are not included here.

## Reading the result

- **`local_pct`** — the share of the simulated corpus assigned to a local backend; this is not measured provider usage.
- **`totals.token_savings_pct` / `usd_savings_pct`** — belt cost vs. the fixed
  baseline.
- **Caveat, stated plainly**: the corpus prompts are short (they're meant to
  be reproducible and fast, not exhaustive), so the effort estimator's
  length-based signal under-weights them relative to real production
  prompts — which carry full stack traces, diffs, multi-file context. On a
  machine with a local backend running, this bench tends to read *higher*
  local% than a real session would. Treat it as a limited diagnostic estimate, not a bound on production savings or a substitute for verified historical measurements.

Related: [[auto-router]] (what's being measured), [[control-loop]] (the real,
historical counterpart), [[cost-estimator]] (the cost model reused here).
