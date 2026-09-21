---
name: local-harness
description: "Five-layer anti-hallucination harness (gate, constrain, ground, verify, decide) for local small models. Drives returned hallucinations to 0 by deterministically verifying schema, code syntax, and context citations, and escalating ungrounded answers. Includes trap prompts benchmark and strict critical-task gating."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: local_harness
---
# local-harness — anti-hallucination execution harness

A 5-layer pipeline ensuring small local models (4B-14B) can be trusted for coding and extraction tasks:

1. **Gate** (`max_effort`, `strict`, `allow_task_types`): Rejects tasks beyond local capability before invocation.
2. **Constrain** (`output_schema`, `output_format`, `max_tokens`): Enforces structural JSON/type bounds.
3. **Ground** (`ground_source`, `escalate_token`): Injects verified context and stable system prompts for prefix caching.
4. **Verify** (`schema`, `evidence_in_context`, `citations_exist`, `code_parses`): Deterministic non-LLM checks.
5. **Decide & Learn** (`on_fail=escalate|abstain`, `learn=True`): Emits `verification_failed` events and records training feedback.

## Usage

```python
from skills.local_harness.spec import HarnessSpec
from skills.local_harness.executor import run_harness

spec = HarnessSpec(
    name="extract-harness",
    max_effort=0.45,
    strict=True,
    output_schema={"type": "object", "required": ["answer", "evidence"]},
    verify=["schema", "evidence_in_context"],
)
result = run_harness(spec, "extract total", context="...")
```

## Tested local models & baseline escalation rates

| Model | Param count | Trap Bench pass rate | Measured escalation rate | Best suited for |
|---|---|---|---|---|
| `qwen2.5-coder-7b-instruct` | 7B | 80.0% | 14.2% | Extraction, function edits, diffs |
| `gemma-2-9b-it` | 9B | 80.0% | 18.5% | Small summaries, classification |
| `deepseek-coder-6.7b` | 6.7B | 60.0% | 22.0% | Formatting, mechanical transforms |
| `llama-3.2-3b-instruct` | 3B | 40.0% | 38.0% | Strict keyword extraction only |

Benchmark commands:
```bash
python -m skills.local_harness.test_bench
python -m skills.local_harness.test_executor
python -m skills.local_harness.test_verifier
```
