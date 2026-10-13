---
name: prompt-improver
description: "Instructions for structuring a prompt as role, context, task, instructions, constraints, output format and success criteria. A local-model execution requires a configured backend; an agent-authored template is not an upstream execution. Not for repeated-prefix detection or skill selection."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: prompt_improver
---
# prompt-improver — pro structured prompts, built locally

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## When NOT to use

- You want to know which prompt or system context is being resent needlessly —
  use prompt_repetition.
- You want to pick the right skill for the improved task — use skill_finder.
- You want to know whether the prompt prefix is the context cost driver —
  use context_profiler.

Improving a prompt is text transformation, not hard reasoning — so it runs on a
**separately configured model backend** (`llm_backends`). Output as structured markdown
or a strict **JSON prompt object**.

## Run it (the /p-amelioration entry point)

```bash
python -m skills.prompt_improver.cli "make my code faster"
python -m skills.prompt_improver.cli "summarize this PR" --json
python -m skills.prompt_improver.cli "..." --no-local        # deterministic scaffold only
```

```python
from skills.prompt_improver import improve
improve("rends mon code plus rapide", as_json=True)["json_prompt"]   # cloud_tokens: 0
```

## The structure (well-established prompt-engineering practice)

| Field | Purpose |
|-------|---------|
| `role` | who the model acts as |
| `context` | only the background that matters |
| `task` | one explicit objective |
| `instructions` | ordered steps |
| `constraints` | hard rules / what NOT to do |
| `output_format` | exact shape of the answer |
| `examples` | optional few-shot `{input, output}` pairs |
| `success_criteria` | machine-checkable "done" conditions |

## How it behaves

- **With a local backend:** the model rewrites the rough prompt into the schema
  (markdown or strict JSON, robustly parsed even through code fences).
- **Without one (or `--no-local`):** returns a deterministic scaffold so the call
  never fails — then suggest installing a local model (see [[llm-backends]]).

Exposed via [[llm-mcp]] as the `improve_prompt` tool. Pairs well with
[[skill-finder]] (find tools for the improved task) and [[auto-router]] (run it
locally). Related global skills: prompt-engineering, prompt-builder, boost-prompt.
