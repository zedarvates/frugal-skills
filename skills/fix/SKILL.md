---
name: fix
description: "List a project's correctable issues — confirmed dead code, duplication, stale directive references — each with a tokens·model·money·time cost estimate and a total. Plan-only by design (never edits code automatically). Use when the user asks what's worth fixing and what each fix costs."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: fix
---
# fix — correctable issues, each with its cost

```bash
python -m skills.fix.cli .            # plan + per-kind cost + total
python -m skills.fix.cli . --save md  # timestamped report
```

Enumerates genuine fixes (dead code ≥0.85 confidence, duplication, stale CLAUDE.md
/AGENTS.md refs) and attaches **tokens · model · money · time** to each via
[[cost-estimator]], plus a grand total. **Plan-only** — it never edits files
(auto-fixers have broken this repo before); apply with review. Exposed via
[[llm-mcp]] as `fix_plan`. Related: [[cost-estimator]], [[fallow-like]], [[checkup]].
