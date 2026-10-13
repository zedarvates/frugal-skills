---
name: upstream-audit
description: "Instructions for the upstream workflow: Track the reviewed Ponytail and RTK baselines, local RTK version, documentation drift, and optional remote Git changes."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: upstream_audit
---
# Upstream audit

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Use `botte upstreams` for a network-free comparison with the reviewed
baselines. Add `--fresh` to query the Ponytail and RTK branch heads. The audit
does not merge or install anything; it reports drift so changes can be reviewed
and tested before adoption. The reviewed RTK baseline is v0.44.2, whose release
fixes owner-only permissions for history, tee, and audit data on supported
platforms.
