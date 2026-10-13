---
name: call-chains
description: "Instructions for upstream Policy A5 analysis of intra-module passthrough chains deeper than five links. Use before considering call-stack flattening; the upstream design reuses the A3 wrapper predicate and five-field finding contract. Review findings before refactoring."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: call_chains
---
# call-chains — anomaly A5 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The upstream detector is described by A5 of the upstream `docs/local-analysis-policy.md` (not bundled here): a path
`entry -> ... -> target` of depth > 5 where each link is a valueless
passthrough (same definition as A3).

Reuses the separately installed upstream `skills/code_wrappers/audit.py` `_is_passthrough` (A7: do not
reimplement). Resolution is intra-module. A transforming middle link
breaks the chain. Report-only: never auto-flattens.

```bash
python -m skills.call_chains.cli [path]
python -m skills.call_chains.cli skills --json
python -m skills.call_chains.test_call_chains
```

Pairs with code_wrappers (A3).
