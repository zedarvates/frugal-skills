---
name: repeated-attempts
description: "Instructions for reviewing identical failed retries in upstream event logs, accounting for context and fingerprint changes and excluding declared transient errors. Verify the installed detector and evidence before treating a retry as redundant."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: repeated_attempts
---
# repeated-attempts — anomaly A10 detector

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Implements A10 of [[../../docs/local-analysis-policy.md]]: two or more
consecutive failed attempts with the same signature are an anomaly.

Signature reused from [[../loop_optimizer/failures.py]] (A7: do not
reimplement). A streak resets on a different error, a successful attempt, or
a transient error (timeout / network / 429 / 503).

```bash
python -m skills.repeated_attempts.cli [.botte/events.jsonl]
python -m skills.repeated_attempts.cli .botte --json
python -m skills.repeated_attempts.test_repeated_attempts
```

Report-only: never fails the build. Pairs with completion_proof (A11).
