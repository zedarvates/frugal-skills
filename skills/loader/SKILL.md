---
name: loader
description: "Assemble the context a delegated sub-agent needs — the shared core agent file plus the agent's own delta — with single and batch loading and a helper that suggests which agents fit a task. Use when spawning named agents that must share one contract. Not for choosing among tools — use tool-router or skill-finder; not for loading skills into the context under a budget — use context-budget."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: loader
---
# Pre-Prompt Loader

## When NOT to use

- You need a tool selected, not an agent's context assembled — use tool_router.
- You need a subset of skills loaded under a budget — use context_budget.
Loads core-agent.md + agent delta for delegate_task subagents.

**Trigger:** When using delegate_task to spawn Mousquetaires or Cardinal agents.

**Usage:**
```python
from skills.loader import load_agent, load_agents_batch, suggest_agents
ctx = load_agent("porthos", project_root="/path/to/project")
tasks = load_agents_batch([("porthos","Audit",None), ("aramis","Optimize",None)])
suggestions = suggest_agents("reassess inherited architecture assumptions")
```

**Module:** `skills/loader`
**Agents:** 9 (porthos, dartagnan, aramis, athos, rochefort, milady, comte_de_wardes, cardinal, monte_cristo)

`monte_cristo` is neither blue nor red. It uses the canonical read-only agent
definition in `agents/monte-cristo.md` and receives no terminal toolset.
`suggest_agents(goal)` performs deterministic, zero-token special-agent routing.
It fails closed unless Monte-Cristo's tracked trigger-evaluation gate passes.
