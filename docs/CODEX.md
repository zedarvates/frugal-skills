# Frugal Skills for Codex

Version 1.0.0 packages the existing 115 instruction workflows. It installs no MCP
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
of `main`. A version in the manifest is not a Git tag. Version 1.0.0 is the first
plugin package; use the commit containing these manifests until a release tag
exists.

For an unpinned source, refresh and reinstall:

```sh
codex plugin marketplace upgrade frugal-skills-marketplace
codex plugin add frugal-skills@frugal-skills-marketplace
```

Open a new Codex session after refreshing. A pinned Git ref stays pinned until
the marketplace source is changed. To change that source, remove its registration
with `codex plugin marketplace remove frugal-skills-marketplace`, then add the
desired Git ref and install again. To uninstall the plugin:

```sh
codex plugin remove frugal-skills@frugal-skills-marketplace
```

Choose either whole-catalog plugin installation or individual skills with
`npx skills add`; installing both may give the host duplicate instruction entries.

## Test a checkout

```sh
python3 scripts/package_plugin.py --check
python3 -m unittest discover -s tests
python3 scripts/package_plugin.py --check --smoke-codex
codex plugin marketplace add /absolute/path/to/frugal-skills
codex plugin add frugal-skills@frugal-skills-marketplace
```

The smoke check uses a temporary Codex configuration and cache. It registers the
local marketplace, discovers version 1.0.0, installs and reinstalls the plugin, and
compares all packaged files with the installed files. It does not change your
existing Codex installation. It was verified with Codex CLI 0.159.2.

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

The deterministic ZIP is written to `dist/frugal-skills-1.0.0.zip`. Its single
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
