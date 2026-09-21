---
name: single-impl
description: "Policy A4 detector (docs/local-analysis-policy.md) — finds ABC, Protocol, and abstract base classes with exactly one concrete implementation across the repository. Pure stdlib AST, 0 cloud tokens. Every finding carries the five mandatory policy fields. Use to identify over-abstraction and unnecessary layer indirections."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: single_impl
---
# single-impl — anomaly A4 detector

Implements A4 of [[../../docs/local-analysis-policy.md]]:

- Scans class hierarchies via static AST.
- Flags abstract interfaces (ABC/Protocol/@abstractmethod) having exactly 1 concrete implementation.
- Skips interfaces used polymorphically via `isinstance`/`issubclass` outside tests.
- Emits standard five policy fields without destructive automatic deletions.

```bash
python -m skills.single_impl.cli [path]
botte interfaces
python -m skills.single_impl.test_single_impl
```

Pure stdlib, 0 cloud tokens, JSON-serialisable.
