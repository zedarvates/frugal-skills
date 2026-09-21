---
name: cache
description: "Cache a project's scan result so the first agent scans and the following agents read the cache instead — get_or_scan, a separate audit report slot, a .botte-cache store and a 24 hour TTL. Use when several agents work on the same project in sequence and the scan is the repeated cost. Not for caching a model response by question — use response-cache; not for caching an agent run whose output is predictable from its input — use agent-cache; not for skipping unchanged files during an audit — use code-fingerprint."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: cache
---
# Project Cache

## When NOT to use

- The cached object is a model answer rather than a project scan — use response_cache.
- The cached object is an agent run — use agent-cache.
- You only want unchanged code skipped inside one audit — use code_fingerprint.
Avoids re-scanning between agents. First agent scans, subsequent agents read cache.

**Trigger:** When multiple agents work on the same project sequentially.

**Usage:**
```python
from skills.cache import ProjectCache
cache = ProjectCache(project_root)
scan = cache.get_or_scan(lambda: scanner.scan())
cache.set_audit_report(report)
```

**Module:** `skills/cache`
**Storage:** `.botte-cache/` directory
**TTL:** 24 hours
**Savings:** -50% re-scan tokens
