# Frugal Skills for Codex

Version 1.0.1 packages the existing 115 instruction workflows. It installs no MCP
server, lifecycle hook, executable runtime, model, external service, or credential.
Some workflows require Botte Secrète or tools such as Java/OculiX, rtk, fallow,
ComfyUI, Ollama, LM Studio or LocalAI. Read the selected skill's prerequisites;
when a referenced module or tool is unavailable, report that prerequisite before
attempting the command. Instructions also mention resources such as RULES.md that
belong to the upstream workflow, not this package.

## Install and update

With a Codex CLI that provides `codex plugin`:

```sh
codex plugin marketplace add zedarvates/frugal-skills --ref main
codex plugin add frugal-skills@frugal-skills-marketplace
codex plugin list --marketplace frugal-skills-marketplace --json
```

To pin a release, supply its published commit SHA or tag through `--ref` instead
of `main`. A version in the manifest is not a Git tag. Version 1.0.0 was the first
plugin package; 1.0.1 corrects skill-level claims and runtime prerequisites. Use
the commit containing the chosen version until its release tag exists.

For an upstream release from an unpinned Git source, first confirm that the
updated `plugin.json` and `.codex-plugin/plugin.json` declare the same **new**
semantic version. Maintainers must change that version when publishing changed
plugin content. Then refresh the marketplace snapshot and install the new version:

```sh
codex plugin marketplace upgrade frugal-skills-marketplace
codex plugin add frugal-skills@frugal-skills-marketplace
```

`marketplace upgrade` refreshes the Git source; it does not by itself replace
the installed plugin's versioned cache. Published content changes need a new
manifest version; the local cachebuster flow below gives development iterations
a distinct version identifier for clients loading the plugin cache. The direct
local `plugin add` command in CLI 0.159.2 recopied an edited skill at the same
version in our smoke test; this test does not demonstrate a stale-cache CLI bug.
Confirm the installed version with `codex plugin list --marketplace
frugal-skills-marketplace --json`, then open a new Codex session.

A pinned Git ref stays pinned until
the marketplace source is changed. To change that source, remove its registration
with `codex plugin marketplace remove frugal-skills-marketplace`, then add the
desired Git ref and install again. To uninstall the plugin:

```sh
codex plugin remove frugal-skills@frugal-skills-marketplace
```

Choose either whole-catalog plugin installation or individual skills with
`npx skills add`; installing both may give the host duplicate instruction entries.

### Updating an edited local checkout

Confirm that the configured marketplace points to the checkout you are editing.
For a new distributable release, set a new semantic version in **both** manifests
before reinstalling. For routine local iteration, preserve the base version and
replace its existing build suffix with one unique `+codex.<cachebuster>` suffix
in both manifests, for example `1.0.1+codex.local-20261013-184516`. The UTC timestamp
must change for the next edit; do not append multiple cachebuster suffixes or
increment the numeric release just to refresh a development cache.

The official plugin-creator skill provides `scripts/update_plugin_cachebuster.py`
for its own plugin layout. This repository has a portable manifest and a Codex
compatibility manifest, so keep their versions aligned when changing either.
After validating the edited package, reinstall from the existing local marketplace:

```sh
python3 scripts/package_plugin.py --check
codex plugin add frugal-skills@frugal-skills-marketplace
codex plugin list --marketplace frugal-skills-marketplace --json
```

Open a new Codex thread to load the changed instructions. `marketplace upgrade`
is for Git-backed sources; it does not update a configured local checkout.

## Test a checkout

```sh
python3 scripts/package_plugin.py --check
python3 -m unittest discover -s tests
python3 scripts/package_plugin.py --check --smoke-codex
codex plugin marketplace add /absolute/path/to/frugal-skills
codex plugin add frugal-skills@frugal-skills-marketplace
```

The smoke check uses a temporary Codex configuration and cache. It registers the
local marketplace from a temporary copy, discovers and installs the package, and
compares all packaged files with the installed files. It then edits one copied
skill, aligns both copied manifests to a new patch version, reinstalls, and checks
that the versioned cache contains the changed instructions and all package files.
It also reports whether reinstalling the initial version retained the old skill.
The real checkout, release version and your existing Codex installation are not
changed. This update test was verified with Codex CLI 0.159.2.

The marketplace uses `source.path: "./"`: Codex resolves it relative to the
marketplace root (the repository), not the `.agents/plugins/` folder. Both the
portable root `plugin.json` and the `.codex-plugin/plugin.json` compatibility
manifest describe the same identity and version. The portable manifest deliberately
omits `extensions.com.openai` so Codex can use the compatibility manifest's listing
and skill path.

The compatibility manifest also includes descriptive `interface.capabilities`
and a starter prompt in `interface.defaultPrompt`. Capabilities are a string list;
plugin starter prompts use camelCase `defaultPrompt` (a string or string list).
This package uses the documented camelCase plugin field; optional skill-level
`agents/openai.yaml` uses snake_case `default_prompt`. The package guard checks the
stricter final listing lengths, including a 30-character short description and
128-character prompts. Passing this local check or installing with the CLI does
not complete the portal's safety scans, identity checks or publication review.
The package also includes original SVG composer and listing icons. Both referenced
assets are square, at least 48 by 48, under 5 MiB, and validated as UTF-8 SVG with
numeric dimensions. The guard rejects missing assets and paths outside the plugin.

## Build the release archive

```sh
python3 scripts/package_plugin.py
```

The deterministic ZIP is written to `dist/frugal-skills-1.0.1.zip`. Its single
top-level `frugal-skills/` directory contains the manifests, LICENSE,
THIRD_PARTY_NOTICES.md, this installation guide, both SVG branding assets, and all
115 SKILL.md files. It
contains no Git metadata, personal configuration, development helpers or MCP
configuration. Preserve THIRD_PARTY_NOTICES.md; MIT applies to this repository,
and it does not relicense external dependencies or upstream copied material.

The three unresolved skills `caveman`, `karpathy-guidelines` and `cwe-kb` remain
excluded. Some available instructions mention them as upstream neighbours; those
references do not install or redistribute the excluded skills. Other TO CHECK
entries remain identified in THIRD_PARTY_NOTICES.md; packaging does not change
their review status.

## Git distribution and the public directory

Publishing these files to the public Git repository makes the Git marketplace
installable. Listing in the universal public ChatGPT/Codex plugin directory is a
separate submission and review through the OpenAI plugin submission portal. Use
the skills-only path with the ZIP, test the imported skills, complete the required
listing and review information, and submit. A Git commit or ZIP alone is not a
completed public directory publication.

Format and distribution references, verified 2026-10-13:

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission)
- [Plugin submission errors](https://developers.openai.com/plugins/deploy/submission-errors)
- [Codex local update and cachebuster reference](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/installing-and-updating.md)
