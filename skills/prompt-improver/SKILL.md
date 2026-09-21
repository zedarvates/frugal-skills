---
name: prompt-improver
description: "Rewrite a rough prompt into a professional, structured prompt (role, context, task, instructions, constraints, output format, success criteria) using a LOCAL model — 0 cloud tokens — with markdown or strict JSON prompt output. Use when the user wants to improve/boost/structure a prompt, mentions '/p-amelioration', 'prompt pro', 'JSON prompt', prompt engineering, or wants a reusable prompt template built locally. Not for finding repeated prefixes that waste tokens in the logs — use prompt-repetition; not for choosing which skill to run — use skill-finder."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: prompt_improver
---
# prompt-improver — pro structured prompts, built locally

## When NOT to use

- You want to know which prompt or system context is being resent needlessly —
  use prompt_repetition.
- You want to pick the right skill for the improved task — use skill_finder.
- You want to know whether the prompt prefix is the context cost driver —
  use context_profiler.

Improving a prompt is text transformation, not hard reasoning — so it runs on a
**local model for 0 cloud tokens** (`llm_backends`). Output as structured markdown
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
