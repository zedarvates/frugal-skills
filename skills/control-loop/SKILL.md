---
name: control-loop
description: "Instructions for upstream routing-outcome analysis and bounded threshold adaptation. Use to inspect local/cloud rates, escalation, verified success and measured usage before proposing updates or resets. Threshold policies are described here; improvement or savings require evidence from actual runs."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: control_loop
---
# control-loop — the router that learns

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The final systemic loop: every routing decision + outcome is recorded, and the
effort→tier thresholds (read live by [[auto-router]]) are nudged from the data —
keep more work local when local is reliable, escalate sooner when it isn't.

```bash
python -m skills.control_loop.cli analyze            # local %, savings, escalation/success
python -m skills.control_loop.cli adapt              # proposed threshold change + why
python -m skills.control_loop.cli adapt --apply      # write it; the router uses it next time
python -m skills.control_loop.cli reset              # back to defaults
```

## How the loop closes

1. **Measure** — `auto_router.run` records each call to `~/.botte/control-ledger.jsonl`
   (effort, tier, local/cloud, tokens saved, escalated, success).
2. **Analyze** — aggregate: local %, escalation rate, success rate, tokens saved.
3. **Adapt** — conservative rule, needs ≥10 samples, small steps, clamped:
   - local reliable (success ≥85%, escalation <15%) → **raise** the LOCAL boundary
     (consider more work for local execution).
   - local insufficient (escalation >30%) → **lower** it (escalate borderline sooner).
4. **Apply** — write `~/.botte/routing-thresholds.json`; `auto_router.effort` reads
   it live, so the next decisions reflect what actually worked.

This is an outcome-based routing adaptation pattern. A threshold change is a proposal, not proof of improved quality or savings; compare subsequent verified outcomes before retaining it. Exposed via [[llm-mcp]] as `routing_stats`.
Related: [[auto-router]], [[conductor]], [[metrics]].
