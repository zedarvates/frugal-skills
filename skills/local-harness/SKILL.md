---
name: local-harness
description: "Instructions for designing an upstream local-model harness with task gates, output constraints, grounding, verification and escalation. These checks can detect some invalid outputs but do not guarantee factual accuracy. Evaluate the installed model and verifier on representative tasks."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: local_harness
---
# local-harness — anti-hallucination execution harness

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

An upstream five-layer design for checking selected local-model outputs. Passing syntax or schema checks does not establish factual accuracy or coding correctness:

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

## Evaluate the installed model

No model accuracy or escalation benchmark is bundled with this catalog. Evaluate the configured model and verifier on representative tasks, and report observed errors and abstentions. The following commands refer to separately installed upstream tests:
```bash
python -m skills.local_harness.test_bench
python -m skills.local_harness.test_executor
python -m skills.local_harness.test_verifier
```
