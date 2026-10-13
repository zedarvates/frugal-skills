---
name: conductor
description: "Guidance for upstream goal-to-plan orchestration through capability selection, layer ordering and command annotations. Use to plan Botte workflows or inspect optional execution modes. Runtime, capabilities and host authority must be verified; execution and confirmation gates belong to the compatible upstream implementation."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: conductor
---
# conductor — goal → ordered plan of capabilities

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The router, generalised: not "which model tier?" but "given this **goal**, which
capabilities, in which order, and what stays local?". The plan is the product —
the upstream planning mode emits it without executing steps. Optional upstream execution modes require their own prerequisites and authority checks.

```bash
python -m skills.conductor.cli "test my desktop app and report crashes"
python -m skills.conductor.cli "reduce token cost and deploy on my project" --json

# Execute the plan (read-only steps run; mutating/cloud steps are gated):
python -m skills.conductor.cli "audit my project and report metrics" --execute
python -m skills.conductor.cli "..." --execute --dry-run      # preview, runs nothing
python -m skills.conductor.cli "..." --execute --confirm      # also run gated steps
```

## How it plans

1. **Curate** — picks the capabilities relevant to the goal ([[capabilities]]
   curator, lexical matching).
2. **Order** — sorts them by the system's layers (SENSE → DECIDE → ACT →
   REMEMBER → GOVERN → DEPLOY): understand → decide → act → remember.
3. **Annotate** — each step gets a concrete command, a local/cloud flag, and the
   reason it's there.
4. **Estimate** — the goal's effort tier ([[auto-router]]) tells you whether any
   step's reasoning will escalate to the cloud.

Expected planning output is an ordered list of annotated steps. Check that the listed commands and capabilities exist in the installed runtime before attempting the plan.

## Executing the plan

The plan can be *run*, not just read. The executor classifies every step:

- **safe** — read-only analysis (`directives_audit`, `metrics`, `infra_advisor`,
  `checkup`, `cluster`, `llm_backends`) → upstream read-only execution category.
- **gated** — mutates state, generates artifacts, or escalates to the cloud →
  runs only with `--confirm` / `confirm=true`.
- **needs_args** — the command still has an unfilled `<placeholder>` → never runs.

`--dry-run` classifies everything and runs nothing (a preview). A failing step
yields a non-zero exit so CI can react. The runner is injectable, so the
upstream implementation can be tested with a substituted runner. No such runtime test evidence is bundled here.

Exposed via [[llm-mcp]] as `conduct` (plan) and `execute_plan` (plan + run safe
steps). Built on [[capabilities]], [[auto-router]]; pairs with the [[control-loop]]
(measure savings → adapt the routing).

Each executor result also emits `agent_state` plus `agent_state_history` using
the backend-neutral `botte-agent-state-v1` contract. Safe work declares a read
scope while queued/working; gated work declares a conservative write scope.
Successful subprocesses become `completed` only after stable Git snapshots
provide revision-bound changed paths and exit validation; incomplete captures
remain `idle`.

Confirmed gated steps acquire one atomic mutation lease per Git root. An active
Botte writer prevents launch and returns `blocked_reason_code=conflict`; safe
read-only steps do not take the write lease.

A custom gated step may declare `mutation_scopes: ["build", "generated"]`.
Those bounded paths are observed directly, including Git-ignored files. An
unsafe or oversized scope blocks before launch or prevents a `completed` claim.
A Git-visible write outside those scopes fails the step even if its command
returns 0; `scope_violations` records the escaped paths without rolling them back.
This includes ignored files: a bounded metadata guard observes all paths outside
the declared scopes. If its initial evidence is incomplete, launch is blocked;
if final evidence is incomplete, the executed step fails without a completion claim.

The default runner also reports `process_containment`. It uses a Windows Job
Object or POSIX process group and closes that boundary before the final workspace
snapshot, preventing ordinary descendants from writing after an apparent success.
Injected test runners remain supported but are explicitly marked unverified.
With `--flow --task-run-id <id>`, the flow reuses the router's opaque task ID
and records a final efficiency verdict. Executed work is eligible for
`passed`/`failed` only when native process containment is attached; injected or
uncontained runners remain `unverified`.
