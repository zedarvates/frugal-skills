---
name: auto-router
description: "Instructions for upstream effort-based local/cloud routing and model fusion (cascade, draft-refine, vote). Use to plan routing, configured providers or model collaboration. Check compatible backends, credentials, budgets and measured capability before execution; this catalog does not route calls or guarantee a fallback."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: auto_router
---
# auto-router — effort-based local↔cloud routing + fusion

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The upstream workflow estimates task effort and selects among configured backends. Selection depends on available capability, budgets and compatible provider configuration; verify those inputs before routing. Extends
`tiered_router` (cost tiers) and `llm_backends` (local discovery) with a cloud
catalog and ensemble strategies.

## When to use

- "Pick local or cloud automatically based on how hard the task is."
- "Use DeepSeek / GLM / Nemotron / Grok / Gemma alongside my local models."
- "Have a local model draft and a stronger model refine" (fusion).
- The user mentions effort routing, model fusion/ensemble, OpenRouter, or any of
  the cloud providers above.

## Auto-decision

```bash
python -m skills.auto_router.cli route "classify: bug or feature?"   # example routing query
python -m skills.auto_router.cli route "design a distributed cache and prove correctness"
python -m skills.auto_router.cli run   "summarize this PR in 2 lines" --max-tokens 200
python -m skills.auto_router.cli dry-run .                          # simulate adaptations from session events
python -m skills.auto_router.cli dry-run . --json
```

Effort is scored from prompt signals (length, code, stack traces, reasoning vs
trivial vocabulary, multi-file scope) → a `Tier`. `Tier ≤ LOCAL` with a local
backend is a candidate for local execution; higher tiers consider configured cloud models and budget settings. Check actual provider access and local capacity. If no compatible backend is available, report the prerequisite instead of assuming a successful fallback.

## Cloud providers

```bash
python -m skills.auto_router.cli providers   # catalog + which are available now
```

Data-driven catalog in `providers.py` — DeepSeek (chat/reasoner), Zhipu GLM,
NVIDIA Nemotron, xAI Grok, Google Gemma. Reach them two ways:

- **OpenRouter** — set `OPENROUTER_API_KEY`, every model by slug, one endpoint.
- **Native** — set the provider's own key (`DEEPSEEK_API_KEY`, `XAI_API_KEY`,
  `ZHIPUAI_API_KEY`, `NVIDIA_API_KEY`), used in preference to OpenRouter.

The upstream configuration uses keys and catalog entries to identify candidate providers. A configured key does not prove authorization or availability; confirm access and compatible model identifiers before execution.

## Fusion (models collaborating)

```bash
python -m skills.auto_router.cli fusion cascade "is 17 prime?"            # cheap→escalate
python -m skills.auto_router.cli fusion draft   "explain the CAP theorem" # local drafts, cloud refines
python -m skills.auto_router.cli fusion vote    "capital of France, one word?"  # consensus
```

- **cascade** — local/cheap first; escalate to a stronger model only if the
  answer looks low-confidence.
- **draft_refine** — local model drafts, a stronger cloud model polishes.
  This is the "local + cloud together" mode.
- **vote** — several models answer; return the consensus (great for classification).

Fusion requires compatible configured backends. With no cloud access, inspect whether the installed implementation supports a suitable local-only path; otherwise report the missing prerequisite.

## MCP

Exposed via [[llm-mcp]] as tools `auto_route` and `fusion`, so an agent can route
and fuse on its own. Related: `tiered_router`, `llm_backends`, `response_cache`.
