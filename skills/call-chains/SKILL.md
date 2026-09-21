---
name: call-chains
description: "Policy A5 detector (docs/local-analysis-policy.md) — finds intra-module passthrough adapter chains of depth > 5 where every link forwards arguments without transformation. Reuses code-wrappers._is_passthrough. Deterministic, 0 cloud tokens. Every finding carries the five mandatory policy fields. Use before flattening call stacks or during checkup."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: call_chains
---
# call-chains — anomaly A5 detector

Implements A5 of [[../../docs/local-analysis-policy.md]]: a path
`entry -> ... -> target` of depth > 5 where each link is a valueless
passthrough (same definition as A3).

Reuses [[../code_wrappers/audit.py]] `_is_passthrough` (A7: do not
reimplement). Resolution is intra-module. A transforming middle link
breaks the chain. Report-only: never auto-flattens.

```bash
python -m skills.call_chains.cli [path]
python -m skills.call_chains.cli skills --json
python -m skills.call_chains.test_call_chains
```

Pairs with code_wrappers (A3).
