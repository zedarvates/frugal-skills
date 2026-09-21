![Frugal Skills](assets/banner.png)

# Frugal Skills

**Deterministic, local-first agent skills that spend zero cloud tokens.**

Most agent tooling pays a model to make decisions a computation can make. Picking
which skill to load, deciding how much context fits in a budget, finding duplicate
function bodies, choosing a model tier — none of that needs a paid call. It needs
an algorithm, and an algorithm costs nothing and returns the same answer twice.

This catalog collects 115 such skills. Each one is either deterministic by
construction, or it declares plainly what it does and what it refuses to do.

## Why this exists

| Decision | Usual approach | Here |
|---|---|---|
| Which skills fit a task under a token budget | ask a model what looks relevant | exact 0/1 knapsack over token cost and relevance |
| Which sibling skill covers a request | let the model read every description | lexical routing, measured at 95.6 percent top-1 with zero cloud tokens |
| Does a codebase duplicate function bodies | model reads the diff | normalized AST hashing, formatting and comments ignored |
| Which model tier does this task need | guess from the prompt | rule-based tier and cost estimate before the call |

The trade is deliberate: these skills are narrower than a model-driven agent, and
they are free, reproducible and auditable.

## Evidence, not promises

Measured on this catalog, reproducible with the commands shown.

| Measure | Result |
|---|---|
| Routing: correct skill ranked first | 43 / 45 cases (95.6 percent) |
| Routing: correct skill in the shortlist | 45 / 45 cases |
| Routing: a forbidden neighbour loaded | 0 |
| Mean reciprocal rank | 0.974 |
| Spec conformance of the generated catalog | 0 errors |
| Cloud tokens spent by routing, compression, audit | 0 |

Every routing case, including the deliberately forbidden ones, is in
skills/skill_finder/evals/evals.json and the result is published as
skills/skill_finder/BENCHMARK.md.

## What is in the catalog

- **Context and budget** — allocate, measure, slice and carry context without guessing
- **Compression** — token structure, content types, output style, agent-to-agent wire format
- **Routing** — skills, tools, model tiers and local hardware
- **Code audit** — complexity, duplication, mutable state, passthrough wrappers, change detection
- **Memory and learning** — a governed memory store, correction rules, distillation
- **Caching** — project scans, agent runs, model answers, each with its own key
- **Orchestration** — blue team, red team, governed pipelines, bounded loops
- **Local and edge inference** — tiny classifiers, media extraction, edge vision
- **Operations and evidence** — checkup, preflight, benchmarks, dashboards, integrity

The full index with one line per skill is in INDEX.md.

## A worked example

Selecting what to load is a 0/1 knapsack, not a judgement call:

    python -m skills.context_budget.cli "optimize slow postgres queries and add tests" --budget 3000

It ranks every skill against the task, solves the knapsack exactly, and reports the
chosen set, the tokens used and the saving against loading the whole catalog. On a
36-skill catalog that is roughly 4 skills and 2k tokens instead of 15k — with no
model call anywhere in the path.

## Install

Through the Agent Skills CLI, which understands the standard layout:

    npx skills add OWNER/frugal-skills --agent codex
    npx skills add OWNER/frugal-skills --list
    npx skills add OWNER/frugal-skills --skill context-budget --yes

Or copy any skill directory into your agent's skills folder. A skill is a directory
containing SKILL.md; nothing else is required.

## What this repository is not

- **Not a Python package.** This catalog ships instructions, not the implementations.
  Where a skill describes a script, the script lives in the upstream project.
- **Not a model.** No weights, no inference server, no bundled runtime.
- **Not a cloud service.** Nothing here calls a hosted API. Skills that need local
  services say which host and port, with a documented placeholder you replace.

## Status

This catalog is being prepared for publication. It is usable today; it is not yet
finished.

- **Licence:** MIT.
- **Provenance:** every skill that draws on external work is recorded in
  THIRD_PARTY_NOTICES.md. A few entries are still being verified, and the affected
  skills will be held back from the published set rather than shipped unresolved.
- **Held back:** three skills are deliberately not in this release, because their
  provenance is not yet resolved. Publishing them would contradict the provenance
  record this repository promises to keep. They are named, with reasons, in
  THIRD_PARTY_NOTICES.md.
- **Language:** English. A few skills still carry French sections from their
  origin; they are usable as they stand and are being translated.
- **Conformance:** validated against the Agent Skills specification; the generated
  catalog reports zero violations.

## Contributing

1. A skill is a directory whose name **equals** its frontmatter name, in lowercase
   with hyphens.
2. The description must say what the skill does and when to reach for it, and it
   must state what it is *not* for when a neighbour covers that ground.
3. Prefer deterministic computation over a model call. If a model is genuinely
   required, say so explicitly.
4. If your skill adopts an idea or copies anything from another project, add the
   entry to THIRD_PARTY_NOTICES.md in the same change.
5. Validate before opening a pull request:

    python -m skills.skill_spec .

## Licence

MIT. See LICENSE. Third-party notices and attributions are in
THIRD_PARTY_NOTICES.md.
