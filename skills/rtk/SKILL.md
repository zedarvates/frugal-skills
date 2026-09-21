---
name: rtk
description: "Compact command output before it reaches the model — prefix a shell command with the wrapper and it returns a filtered, smaller form (test failures only, build errors grouped, compact diff, compact status), with meta commands for savings statistics, missed-usages discovery and an unfiltered proxy mode. Use on the verbose and repetitive commands: tests, builds, git, package managers, containers and file listings. Not for compressing model input in general — use universal-compressor; not for the per-turn compression policy — use token-shaper."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: rtk
---
# RTK — compact shell output

> A terminal wrapper that compacts command output to cut token usage.

## Purpose

Prefix a command with the wrapper; if it has a dedicated filter the output is
compacted, otherwise it passes through unchanged. Categories with the largest
savings are tests, builds, package managers, containers and git.

    rtk <command>            # filtered output
    rtk gain                 # savings statistics
    rtk discover             # find missed usages in past sessions
    rtk proxy <command>      # run WITHOUT filtering (debugging)
    rtk --version

## Provenance and boundaries

- Upstream is an external project; this repository pins and reviews a specific
  stable version. Check the local version and keep it current — the tool ships
  fixes frequently, including Windows shell detection and exit-code visibility.
- Filtering can hide detail. Use proxy mode whenever the compacted view is not
  enough to understand a failure.
- Known local limitation on Windows: some builtins are not wrapped, so reading a
  file directly through it fails; use proxy mode for those.

Read the full command table in [README.md](README.md).

## When NOT to use

- You want model input compressed rather than shell output — use universal_compressor.
- You want the per-turn compression decision — use token_shaper.
