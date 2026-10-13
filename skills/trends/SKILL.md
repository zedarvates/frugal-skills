---
name: trends
description: "Instructions for the upstream workflow: Track a project's audit metrics over time (directive score, duplication, LOC, always-on cost, fix count, recurring Markdown review state) and show the change since the previous run. Use to see whether the project is getting healthier/cheaper across audits."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: trends
---
# trends — the project's metrics over time

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

```bash
python -m skills.trends.cli snapshot .   # record current metrics
python -m skills.trends.cli show .        # series + Δ since previous run
```

Each `snapshot` appends to `.botte/trends.jsonl`; `show` reports the series and
the delta (e.g. "duplicate_groups 35 ▼ 12"). Markdown history is aggregate-only:
due, current, overdue/changed, and never-reviewed counts. It persists no paths,
document content, prompts, or model responses. Run it after each `checkup` to
watch the project improve. Exposed via [[llm-mcp]] as `trends_show`. Related:
[[checkup]], [[docs-steward]], [[metrics]], [[report]].
