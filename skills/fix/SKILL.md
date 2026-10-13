---
name: fix
description: "Instructions for the upstream workflow: List a project's correctable issues — confirmed dead code, duplication, stale directive references — each with a tokens·model·money·time cost estimate and a total. Plan-only by design (never edits code automatically). Use when the user asks what's worth fixing and what each fix costs."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: fix
---
# fix — correctable issues, each with its cost

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

```bash
python -m skills.fix.cli .            # plan + per-kind cost + total
python -m skills.fix.cli . --save md  # timestamped report
```

Enumerates genuine fixes (dead code ≥0.85 confidence, duplication, stale CLAUDE.md
/AGENTS.md refs) and attaches **tokens · model · money · time** to each via
[[cost-estimator]], plus a grand total. **Plan-only** — it never edits files
(auto-fixers have broken this repo before); apply with review. Exposed via
[[llm-mcp]] as `fix_plan`. Related: [[cost-estimator]], [[fallow-like]], [[checkup]].
