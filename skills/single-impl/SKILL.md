---
name: single-impl
description: "Instructions for the upstream single-implementation abstraction detector. Confirm the compatible runtime and analysis policy; review ABC, Protocol and abstract-base findings as candidates, with evidence, rather than automatic refactoring authority."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: single_impl
---
# single-impl — anomaly A4 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

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

The upstream detector describes a JSON-serialisable result; validate it against the installed policy and evidence.
