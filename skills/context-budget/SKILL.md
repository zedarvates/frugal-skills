---
name: context-budget
description: "Instructions for upstream context allocation under a token budget using a 0/1 knapsack model over relevance and token cost. Use to plan which skills or documents to load; verify the installed solver, cost estimates and scaling before interpreting optimality. Not for prefix measurement (context-profiler), typed slicing (context-slicer) or ranking without a budget (skill-finder)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: context_budget
---
# context-budget — context allocation under a token budget

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## When NOT to use

- You want to measure the always-on cost, not allocate it — use context_profiler.
- One large body of context must serve several agents or task types — use context_slicer.
- You only need a ranked shortlist and have no budget constraint — use skill_finder.

The OR-Tools principle applied to the agent's always-on cost: choosing *which*
skills/docs to load is a **0/1 knapsack** — maximize total relevance while the
summed token cost stays under a budget. The upstream design uses dynamic programming for this 0/1 model. Verify the installed solver, relevance inputs, token estimates and any scaling before interpreting the result as optimal for the original inputs.

```bash
python -m skills.context_budget.cli "optimize slow postgres queries and add tests" --budget 3000
python -m skills.context_budget.cli "<task>" --budget 4000 --json
```

## How it selects

1. **Rank** — score every skill against the task lexically ([[skill-finder]],
   matching), with each skill's token cost.
2. **Knapsack** — `knapsack(items, budget)` finds the subset that maximizes
   summed relevance subject to `Σ tokens ≤ budget` (exact DP, token costs scaled
   to bound the table). Inspect how scaling affects the original budget and objective.
3. **Frame** — report the chosen set, tokens used, relevance captured, and the
   saving vs loading the whole catalog.

No typical subset size or savings is established by this catalog. Report the actual chosen inventory, budget and measured or estimated costs from the compatible installed runtime.

The `knapsack(items, budget)` engine is generic (takes `Item(name, kind, tokens,
relevance)`), so docs ([[docs-steward]]) or any context source plug in the same
way. Exposed via [[llm-mcp]] as `context_budget`. Related: [[skill-finder]]
(ranking), [[metrics]] (measures the always-on cost this cuts).

First of the deterministic "solver" hybridizations (OR-Tools-inspired): exact
combinatorial optimization replacing LLM reasoning for structured decisions.
