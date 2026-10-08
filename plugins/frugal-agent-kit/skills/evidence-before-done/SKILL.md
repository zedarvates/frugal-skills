---
name: evidence-before-done
description: "Inspect a task-completion claim and identify missing independent evidence before marking it done. Use to review test outputs, commit claims, or deployment claims; not as an execution gate or cryptographic verifier."
---
# Evidence before done (read-only)

1. Extract each specific assertion: changed file, executed command, passed test, security result, publication, or deployment.
2. Pair it with supplied evidence: immutable revision and diff, test name and result, artifact path and checksum, log and run ID, or independent observation.
3. Distinguish **reported** evidence from independently **verified** evidence. An agent saying a test passed is not proof it ran.
4. Assign each claim `supported`, `unsupported`, or `contradicted`, and identify the minimum missing check.
5. Summarize remaining uncertainty. Do not announce completion if critical claims lack evidence.
6. Never execute, upload, expose private data, or alter a repository as part of this review unless separately authorized.

This is a review guide, not a hash authenticator, CI runner, or substitute for an independent test executor.
