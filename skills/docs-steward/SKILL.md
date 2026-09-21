---
name: docs-steward
description: "Scoped documentation map for multi-component projects (server + client + tools + …). Detects components, classifies every doc as global vs component-scoped, and produces a per-component index (DOCS.md) listing local docs + links to the relevant global docs — so an LLM coder bounded to one component loads only its scope, not every other component's documentation. Frames token cost (full project docs vs scoped load) and treats .md as LLM-facing, .html as human reference. Use when a project has several components and you want to cut the docs an agent must read, or asks how to organise docs for a monorepo."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: docs_steward
---
# docs-steward — the right docs, at the right scope

A monorepo accumulates docs at several scopes: **global** docs at the root, and
**component** docs inside each component's folder. When an LLM coder is *bounded*
to one component (e.g. the server), loading every other component's docs wastes
tokens every turn. The steward builds a **scoped map** so each bounded coder
loads only its own docs **+ links to the relevant global docs**.

```bash
python -m skills.docs_steward.cli map   .                 # the scoped docs map
python -m skills.docs_steward.cli index . --component server   # preview server/DOCS.md
python -m skills.docs_steward.cli index . --write         # write a DOCS.md per component
python -m skills.docs_steward.cli tasks .                 # lifecycle: finished tasks + report sprawl
python -m skills.docs_steward.cli prune . --write         # strip done tasks (archived, not lost)
python -m skills.docs_steward.cli reports . --keep 5 --archive   # tidy .botte reports
python -m skills.docs_steward.cli review .                # annual review due list (preview)
python -m skills.docs_steward.cli review-prompt . AGENTS.md --tier local
python -m skills.docs_steward.cli review-apply . result.json      # preview verified result
python -m skills.docs_steward.cli audience .              # read-only Markdown/HTML audit
python -m skills.docs_steward.cli knowledge-audit .       # Wiki/second-brain proposals
```

## How it maps

1. **Detect components** — top-level dirs with a manifest (`package.json`,
   `pyproject.toml`, `go.mod`, …), known names (server/client/api/tools/…), or
   code; monorepo containers (`apps/`, `packages/`, `services/`) expand to their
   children. Pure-doc/asset dirs are never components.
2. **Classify docs** — every `.md`/`.mdx`/`.rst`/`.txt`/`.html` is assigned to the
   deepest component it lives under, else it's **global**.
3. **Scope + frame** — each component gets its local docs, links to the global
   (LLM-facing) docs, and a token cost: *scoped load* (local + globals) vs *all
   project docs*. `.md` = load; `.html` = human reference (linked, not loaded).
4. **Index (confirm-gated)** — `index --write` drops a `DOCS.md` in each component
   telling a bounded coder exactly what to load. Preview by default; `--write`
   to commit the files.

Output: a JSON map, 0 cloud tokens to produce. Exposed via [[llm-mcp]] as
`docs_map`. Related: [[directives-audit]] (agent-guidance file health),
[[metrics]] (per-component cost), [[checkup]].

## Docs lifecycle (finished tasks + report sprawl)

Finished work shouldn't keep costing tokens. `lifecycle.py` adds two
confirm-gated jobs (preview by default, act only on `--write`/`--archive`):

- **tasks/plans** — `scan_tasks` finds checkbox markdown (`- [ ]` / `- [x]`) and
  counts open vs done + the token waste of done items still in-file. `prune`
  strips done items (preserving them in `.botte/archive/<name>.done.md` — nothing
  is lost) and moves fully-done plans out of the working tree.
- **reports** — `report_hygiene`/`reports --archive` keep the N most recent of
  each `.botte` report and move the rest to `.botte/reports/archive/`.

Read-only summary via the `docs_lifecycle` MCP tool (`lifecycle_report`); the
prune/archive actions stay CLI-only and confirm-gated.

## Recurring Markdown review

`review.py` turns periodic instruction cleanup into a fail-closed contract:

- **365 days by default** — override with `--interval-days` or copy
  `configs/docs-review.example.json` to the local, Git-ignored
  `.botte/docs-review.json`. The config controls include/exclude/focus globs,
  review-on-change, model hints, and explicit upgrade notes.
- **Local inventory** — `review` computes hashes, due dates, priority, token
  estimates, and evidence-labelled model references. A textual reference is
  never reported as proof that a model is active. No network/model call occurs.
- **Bounded prompt** — `review-prompt` reviews one file. Cloud tier returns full
  `updated_md`; local tier returns exact unique find/replace edits. Both bind the
  result to the source SHA-256 and preserve project facts, preferences, safety,
  architecture, APIs, commands, and provenance.
- **Verified application** — `review-apply` previews by default. `--write`
  rejects stale hashes and unsafe paths, archives the exact prior bytes under
  `.botte/archive/docs-review/<timestamp>/`, writes atomically, then records the
  review in Git-ignored `.botte-cache/docs-review-state-v1.json`.
- **Small-model tolerance** — the result parser accepts raw JSON, one strict
  `botte-llm` provenance line, and one bare `json` fence. Any other surrounding
  prose still fails closed before application.
- **No-change review** — `review-mark` records an explicit human/model review;
  it also requires `--write` to change local state.

The tool never schedules an OS task and never calls a cloud provider. Cron,
Task Scheduler, CI, or an agent may invoke the read-only `review` command at a
user-selected cadence.

`/checkup` now includes due/current counts. Never-reviewed bootstrap files are
informational; only elapsed intervals or explicitly watched content changes
become drift.

`trends snapshot` persists only aggregate review counts (due/current,
overdue/changed, never-reviewed); paths, content, prompts, and model responses
remain outside the historical journal.

## Wiki and second-brain integrity

`knowledge_integrity.py` detects a project Wiki, memory files, daily notes, or
the governed Memory Hub only when one is present. The deterministic audit checks
entry points, authority/precedence, provenance, freshness, state-versus-event
write rules, human approval, project/privacy boundaries, and the declared or
inferred always-loaded surface.

`knowledge-audit` is preview-only and uses 0 LLM tokens. Every gap becomes a
bounded proposal with a priority, target file, and suggested change; it never
rewrites the knowledge base. Use repeatable `--always-loaded <file>` arguments
to replace filename inference with explicit runtime knowledge. `/checkup`
includes the score and turns P1/P2 gaps into an actionable drift item.

The coverage boundary is explicit: this pass verifies mechanisms, not the truth
of every claim. Semantic contradictions still require comparing current-sounding
claims with the freshest evidence. A report with zero proposals is therefore not
a guarantee that no stale fact exists.

## Markdown/HTML audience policy

`audience.py` makes the format boundary enforceable without taking ownership of
the user's publishing workflow:

- **Markdown is canonical for LLMs** — `.md`/`.mdx`/`.markdown` are editable
  sources. `.html` is an optional human rendering or standalone interface.
- **HTML never inflates context budgets** — maps still list HTML as a human
  reference, but global, local, scoped, and total token counts include only
  LLM-facing documents.
- **Freshness needs provenance** — a renderer can embed
  `<!-- botte-docs-source: path=docs/guide.md; sha256=<source-sha256> -->`.
  `audience` then reports `current` or `stale` from content hashes. A same-stem
  pair without the marker stays `unverified`; standalone HTML is informational.
- **Read-only and optional** — `audience` never converts, rewrites, deletes, or
  requires an HTML copy for Markdown. Root `MEMORY.md`, local agent state, and
  symlinked documents are excluded from discovery.
