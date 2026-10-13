![Frugal Skills](assets/banner.png)

# Frugal Skills

**115 instruction workflows for deterministic, local-first agent tooling.**

Most agent tooling pays a model to make decisions a computation can make. Picking
which skill to load, deciding how much context fits in a budget, finding duplicate
function bodies, choosing a model tier — none of that needs a paid call. It needs
an algorithm, and an algorithm costs nothing and returns the same answer twice.

This catalog collects 115 skill instruction files. The implementations described
by these files live in the upstream [Botte Secrète project](https://github.com/zedarvates/botte-secrete).
Installing the catalog adds instructions to an agent; it does not install those
implementations, external tools, local services, or model weights. The agent host
may consume model tokens while following the instructions.

## Why this exists

| Decision | Usual approach | Here |
|---|---|---|
| Which skills fit a task under a token budget | ask a model what looks relevant | exact 0/1 knapsack over token cost and relevance |
| Which sibling skill covers a request | let the model read every description | lexical routing implemented upstream |
| Does a codebase duplicate function bodies | model reads the diff | normalized AST hashing, formatting and comments ignored |
| Which model tier does this task need | guess from the prompt | rule-based tier and cost estimate before the call |

These are design choices of the upstream tooling. Check each skill's prerequisites
and the installed implementation before expecting an executable workflow.

## What is validated here

The repository validates plugin metadata, the 115-skill inventory, provenance
exclusions, and the distributable archive. With Codex installed, the optional
smoke check installs the actual package in an isolated configuration directory
and compares the installed skill files and notices with the source.

Routing benchmarks and runtime tests belong to Botte Secrète. Their Python modules
and benchmark artifacts are not included in this instruction catalog, so this
release does not claim to reproduce their results.

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

## An upstream runtime example

After installing the compatible Botte Secrète implementation and its dependencies,
the context-budget skill describes this command:

    python -m skills.context_budget.cli "optimize slow postgres queries and add tests" --budget 3000

That module is not supplied by this repository. Run it from the upstream runtime
environment, not from a clone of this catalog.

## Install

As a Codex plugin (the whole catalog):

    codex plugin marketplace add zedarvates/frugal-skills --ref main
    codex plugin add frugal-skills@frugal-skills-marketplace

For an upstream release whose manifests declare a new plugin version, refresh
the marketplace and install that version:

    codex plugin marketplace upgrade frugal-skills-marketplace
    codex plugin add frugal-skills@frugal-skills-marketplace

Start a new Codex session after installation or update. See
[Codex installation, release packaging and limitations](docs/CODEX.md) for local
testing, cachebusters, version pinning and public directory submission. Keep the
two manifest versions aligned and use a new version for changed published content.
This Git marketplace
does not imply publication in the universal ChatGPT/Codex plugin directory.

Through the Agent Skills CLI, which understands the standard layout:

    npx skills add zedarvates/frugal-skills --agent codex
    npx skills add zedarvates/frugal-skills --list
    npx skills add zedarvates/frugal-skills --skill context-budget --yes

Or copy any skill directory into your agent's skills folder. A skill is a directory
containing SKILL.md; nothing else is required.

## What this repository is not

- **Not a Python package.** This catalog ships instructions, not the implementations.
  Where a skill describes a script, the script lives in the upstream project.
- **Not a model.** No weights, no inference server, no bundled runtime.
- **Not a cloud service.** Nothing here calls a hosted API. Skills that need local
  services say which host and port, with a documented placeholder you replace.

## Status

This catalog is published, and still being completed.

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
- **Plugin version:** 1.0.0, the first Codex plugin package of this catalog.
- **Validation:** package checks run in this repository. Runtime checks remain
  upstream; they are not implied by a successful instructions-only installation.

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

    python3 scripts/package_plugin.py --check

With Codex CLI available, also verify discovery, installation and file integrity:

    python3 scripts/package_plugin.py --check --smoke-codex

## Licence

MIT. See LICENSE. Third-party notices and attributions are in
THIRD_PARTY_NOTICES.md.
