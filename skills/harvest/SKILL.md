---
name: harvest
description: "Build a bounded, read-only manifest of explicitly selected local repositories and dispersed Botte deployments before comparing or migrating fixes."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: harvest
---
# Harvest

Use `botte harvest <project>...` before removing, updating, or centralizing a
deployed Botte copy. Scope is explicit: paths passed on the command line and,
only with `--fleet`, paths already registered by the user.

The manifest contains Git ancestry, dirty-state counts, bounded file digests,
Botte deployment markers, and reviewed Ponytail/RTK provenance. It never stores
raw file contents, never runs `git fetch`, and never writes target projects.
`--fresh-upstreams` is the only network-enabled option.

For central links, known Botte config/MCP/hook/policy/directive fragments are
classified without exporting their contents. Nested Git copies get a bounded
history/tree comparison. `repoint_candidate_no_unique_commits` is evidence for
manual migration review, not permission to delete the copy.
