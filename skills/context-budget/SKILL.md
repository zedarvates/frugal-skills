---
name: context-budget
description: "Pick the optimal set of skills/docs to load for a task under a token budget — an exact 0/1 knapsack (maximize relevance while summed token cost stays under budget), not an LLM 'decide what's relevant' call. Deterministic, stdlib, 0 cloud tokens. Cuts the always-on context cost (loading the whole skill catalog every turn). Use when you want to load only the most relevant context within a budget, or to decide which skills/docs an agent should read for a task. Not for measuring how much the prefix already costs — use context-profiler; not for splitting one body of context into reusable typed slices — use context-slicer; not for ranking a single query without a budget — use skill-finder."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: context_budget
---
# context-budget — optimal context under a token budget

## When NOT to use

- You want to measure the always-on cost, not allocate it — use context_profiler.
- One large body of context must serve several agents or task types — use context_slicer.
- You only need a ranked shortlist and have no budget constraint — use skill_finder.

The OR-Tools principle applied to the agent's always-on cost: choosing *which*
skills/docs to load is a **0/1 knapsack** — maximize total relevance while the
summed token cost stays under a budget. That's an exact deterministic solver
(stdlib DP), so it costs **0 tokens** and beats the greedy "take the top matches
until full" heuristic.

```bash
python -m skills.context_budget.cli "optimize slow postgres queries and add tests" --budget 3000
python -m skills.context_budget.cli "<task>" --budget 4000 --json
```

## How it selects

1. **Rank** — score every skill against the task lexically ([[skill-finder]],
   0 tokens), with each skill's token cost.
2. **Knapsack** — `knapsack(items, budget)` finds the subset that maximizes
   summed relevance subject to `Σ tokens ≤ budget` (exact DP, token costs scaled
   to bound the table). Optimal, not greedy.
3. **Frame** — report the chosen set, tokens used, relevance captured, and the
   saving vs loading the whole catalog.

On this repo a typical task loads ~4 skills (~2k tok) instead of the whole
~36-skill catalog (~15k tok) — an ~85% cut in always-on context for that task.

The `knapsack(items, budget)` engine is generic (takes `Item(name, kind, tokens,
relevance)`), so docs ([[docs-steward]]) or any context source plug in the same
way. Exposed via [[llm-mcp]] as `context_budget`. Related: [[skill-finder]]
(ranking), [[metrics]] (measures the always-on cost this cuts).

First of the deterministic "solver" hybridizations (OR-Tools-inspired): exact
combinatorial optimization replacing LLM reasoning for structured decisions.
