---
name: upstream-audit
description: "Track the reviewed Ponytail and RTK baselines, local RTK version, documentation drift, and optional remote Git changes."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: upstream_audit
---
# Upstream audit

Use `botte upstreams` for a network-free comparison with the reviewed
baselines. Add `--fresh` to query the Ponytail and RTK branch heads. The audit
does not merge or install anything; it reports drift so changes can be reviewed
and tested before adoption. The reviewed RTK baseline is v0.44.2, whose release
fixes owner-only permissions for history, tee, and audit data on supported
platforms.
