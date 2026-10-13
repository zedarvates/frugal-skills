---
name: solvers
description: "Instructions for upstream task assignment, bin packing and dependency scheduling. LPT and FFD are heuristics rather than general optimality guarantees; validate capacities, dependencies and algorithm assumptions. Not a bundled solver runtime."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: solvers
---
# solvers — assignment, bin-packing, precedence scheduling

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

The OR-Tools family, in stdlib. The structured decisions the system makes —
*spread work across the cluster*, *pack items under a capacity*, *order a plan's
steps under dependencies* — are classic combinatorial problems with exact or
well-known algorithms. Their computation need not invoke a model, but that does not measure host-agent usage or guarantee the runtime's availability.

```bash
python -m skills.solvers.cli assign w1,w2,w3 audit:5 build:8 test:3 deploy:2
python -m skills.solvers.cli pack 10 a:4 b:7 c:3 d:6
python -m skills.solvers.cli schedule build test:build lint:build deploy:test,lint
```

- **assign_balanced(tasks, workers)** — Longest-Processing-Time-first greedy:
  heuristic load balancing under its declared assumptions; it does not solve every assignment optimally. Spreads cluster
  work across [[cluster]] backends.
- **bin_pack(items, capacity)** — First-Fit-Decreasing: heuristic packing into bins of a given
  capacity; oversized items flagged.
- **schedule(steps, deps)** — topological order of a DAG **+ parallel waves**
  (each wave's steps have their prerequisites satisfied, so they run in parallel),
  with cycle detection. Generalises the [[conductor]]'s layer-sort into real
  precedence scheduling.

Exposed via [[llm-mcp]] as `schedule_plan` and `assign_work`. For very large
instances, evaluate a separately installed `ortools` CP-SAT integration. The implementations described here are not bundled, and compatibility must be checked.

Completes the deterministic-hybridization program (alongside [[context-budget]]
knapsack and [[nlp-deterministic]]): exact computation replacing LLM reasoning
for structured decisions.
