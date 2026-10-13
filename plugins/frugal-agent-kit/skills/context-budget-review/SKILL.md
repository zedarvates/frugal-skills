---
name: context-budget-review
description: "Review context proposed for a coding or agent task; identify necessary, conditional, and removable sections under a stated budget. Use for context triage, not exact tokenizer measurements or automated retrieval."
---
# Context budget review (read-only)

For a given task and optional context inventory:

1. Write the user task and its acceptance checks in a sentence.
2. Categorize each supplied context item: **required**, **on demand**, **exclude**. Preserve safety rules and required user constraints regardless of compression pressure.
3. State the reason for each category; put repeated or unrelated content on demand.
4. When exact token counts are supplied by a tokenizer, report their sum. If unavailable, mark token numbers **unknown**; do not fabricate counts or an exact optimization result.
5. Give a compact task context packet: objective, relevant files/sources, constraints, evidence to collect, and open questions.
6. Never delete files, alter agent instructions, or claim reduction in billed tokens without before/after provider measurements.

Do not claim to run the upstream knapsack implementation: this package contains no Python solver. For that, users must separately install and validate the public upstream source.
