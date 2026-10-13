---
name: checkup
description: "Guidance for the upstream project-checkup sequence: policy, directives, metrics, infrastructure, duplication, security, documentation, knowledge integrity and drift. Use after updates or during onboarding. Run only with the compatible runtime and inspect collected evidence; one checkup does not establish completeness or optimality."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: checkup
---
# checkup — the canonical project checkup ("botte doctor")

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The upstream command assembles a documented review sequence and prints a verdict based on the checks that ran. Verify detector availability and evidence; a verdict does not prove complete coverage or an optimal procedure.

```bash
python -m skills.checkup.cli            # current dir
python -m skills.checkup.cli <project> --json
python -m skills.checkup.cli . --pr-comment   # Markdown verdict for a PR comment
python -m skills.checkup.cli . --doctor       # + machine scan + ranked top-3 opportunities
python -m skills.checkup.cli . --doctor --fresh   # re-scan for local LLM backends (not cached)
```

## `--doctor` — the one-verb assembly

`--doctor` is `checkup` plus two things it doesn't otherwise do:

- **machine scan** — is a local LLM backend reachable (LM Studio/Ollama)? via
  [[llm-backends]] `audit()`; reads the cached registry unless `--fresh`.
- **ranked top-3 opportunities** — fixes from [[fix]] `find_fixes()`, ranked by
  estimated token cost (highest first), plus any remaining drift items, capped
  at 3.

Both feed a **one-line verdict**: `✅ sain` when there's no drift and a local
backend is active, or `⚠️ N optimisation(s), ~X tokens d'opportunités`
otherwise. Pure assembly of existing modules — no new skill, no new report format.

## Sequence (cheap → deeper)

1. **policy** — is `.botte/policy.md` committed? (shared rules for devs/agents)
2. **directives** — CLAUDE.md/AGENTS.md health + stale path refs
3. **metrics** — LOC per component + always-on cost + savings framing
4. **infra** — hardware/software/MCP cluster tips (+ ASCII diagram)
5. **duplication** — stdlib AST duplicate-function scan
6. **security** — taint / data-flow scan ([[fallow-like]] `TaintAnalyzer`),
   CWE-tagged; high-severity findings are considered for drift review.
7. **docs review** — recurring Markdown due/current status from
   [[docs-steward]]. Never-reviewed bootstrap files are informational; an
   expired interval or explicitly watched content change becomes drift.
8. **knowledge integrity** — when a Wiki or second brain is detected, verify its
   structural maintenance contract and propose reviewable changes. P1/P2 gaps
   become drift; the audit remains read-only and makes no semantic-cleanliness claim.
9. **drift** — MCP wired? directives stale/oversized? policy missing? security?

Then points at the deep code audit (secrets/dead-code) for when you want it.

## Why

A component update or another dev/agent introduces **drift** — stale directives,
unwired MCP, an oversized CLAUDE.md, a missing policy. `/checkup` catches all of
the configured sequence. Confirm which checks ran and treat any missing evidence or detector as a reported limitation.

## On pull requests

`--pr-comment` prints a verdict-first Markdown comment (carrying a stable marker
so a bot can edit it in place), **including the security section** — so the
taint/data-flow section can be reviewed with the rest of the CI output. The `🧦 Botte Checkup (PR)` GitHub
Action (`.github/workflows/botte-pr-checkup.yml`) runs this on every PR and
can post/update a comment via `gh` when that separate workflow, dependencies, credentials and permissions are configured. The workflow is not included in this catalog; verify its behavior before reuse.

Related: [[preflight]] (enforces prefer-local every turn), [[infra-advisor]],
[[metrics]], [[trends]], [[directives-audit]], [[bootstrap]].
