---
name: cache
description: "Instructions for upstream project-scan caching with get_or_scan, an audit-report slot and a documented 24-hour TTL. Use when sequential agents may reuse a compatible scan; validate freshness and analysis inputs. Not for model-answer caching, agent-run caching or per-file fingerprint gates."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: cache
---
# Project Cache

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

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
