---
name: cost-estimator
description: "Instructions for estimating task resources and provider costs with a separately installed runtime. Use estimates for planning, then compare them with measured usage, hardware costs and current provider prices; estimates are not billed-cost guarantees."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: cost_estimator
---
# cost-estimator — tokens · model · money · time

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

```python
from skills.cost_estimator import estimate, estimate_fix
estimate("code_review", 4000).human()    # "2000 tok · Haiku/Flash (cloud) · $0.0001 · ~16s"
estimate_fix("dead_code", count=11)       # estimated resource use; measure the actual run
```

Reuses `tiered_router`'s token+$ model and adds a throughput model for time.
Local and cloud tiers have different provider, hardware and operating costs. Check current prices and observed latency. The upstream estimator informs the
`fix` plan and any "what will this cost?" question. Exposed via [[llm-mcp]] as
`estimate_cost`. Related: [[fix]], [[auto-router]], [[metrics]].
