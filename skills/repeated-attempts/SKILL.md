---
name: repeated-attempts
description: "Policy A10 detector (docs/local-analysis-policy.md) — finds identical failed retries in local event logs (same action + same error + same fingerprints, no intermediate context change). Reuses loop-optimizer.failures.failure_signature. Transient errors (timeout/network/429/503) are excluded. Deterministic, 0 cloud tokens. Every finding carries the five mandatory policy fields. Use before rerunning a failed command or during checkup."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: repeated_attempts
---
# repeated-attempts — anomaly A10 detector

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
