---
name: llm-backends
description: "Discover, audit and use local LLM servers (LM Studio, Ollama, LocalAI, vLLM, llama.cpp) on this machine or the network to offload work from the cloud and save tokens. Use when the user mentions local models, LM Studio, Ollama, 'run it locally', token savings via local hardware, or wants to know what models their machine can run."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: llm_backends
---
# llm-backends — Local LLM discovery, audit & routing

Turn idle local hardware into a token-saving tier. Every task served by a local
model is a task **not** billed to the cloud.

## When to use

- The user mentions **LM Studio, Ollama, LocalAI, vLLM, llama.cpp**, "local model",
  "run it locally", or "use my GPU".
- You need to know **what models are reachable** (this machine or the network).
- A task is cheap/local-suitable (classification, extraction, short summary,
  routing, spell-check, simple Q&A) and could skip the cloud entirely.
- The user has **no** local model yet and wants step-by-step, hardware-aware setup.

## Quick commands

```bash
# Discover + register backends (writes configs/llm-endpoints.json)
python -m skills.llm_backends.cli scan                 # localhost only
python -m skills.llm_backends.cli scan --subnet        # sweep local /24
python -m skills.llm_backends.cli scan inference-host.example    # specific host(s)

# What's registered?
python -m skills.llm_backends.cli list

# Audit: are local models used? what can this machine run? next steps?
python -m skills.llm_backends.cli audit --fresh

# Run a prompt locally (0 cloud tokens)
python -m skills.llm_backends.cli chat "classify: bug or feature?" --max-tokens 128

# Suggest a local model for a project (adaptive per project type)
python -m skills.llm_backends.cli profile ~/my-project

# Compare CPU / 50% hybrid / GPU memory estimates without loading a model
python -m skills.auto_router.cli profiles --model MODEL --context-tokens 4096

# Dry-run a measured placement benchmark; refuses while any model is resident
python -m skills.auto_router.cli profiles-benchmark MODEL

# Explicit mutation authority, still subject to empty-runtime/resource gates
python -m skills.auto_router.cli profiles-benchmark MODEL --execute
```

## Programmatic use

```python
from skills.llm_backends import registry, quick_chat, audit

registry.refresh()                       # discover + persist
best = registry.best_chat_backend()      # lowest-latency chat backend
model = registry.preferred_model(best)   # coder/instruct over voice/reasoning

res = quick_chat("summarize in 1 line: ...", max_tokens=200)
print(res.text, res.total_tokens)        # all local — no cloud cost
```

## Supported backends

| Backend | Default port | API |
|---------|-------------|-----|
| LM Studio | 1234 | OpenAI `/v1` |
| Ollama | 11434 | native `/api/tags` + OpenAI `/v1` |
| LocalAI | 8080 | OpenAI `/v1` |
| vLLM | 8000 | OpenAI `/v1` |
| Jan / KoboldCpp / text-gen-webui | 1337 / 5001 / 5000 | OpenAI `/v1` |
| ComfyUI | 8188 | image gen |
| Qdrant | 6333 | vector search |

## How it saves tokens

1. **Audit** finds reachable local backends and profiles RAM/VRAM/GPU.
2. **Route** sends local-suitable tasks (see `tiered_router` L0/L1) to a local model.
3. **Call** runs them via the OpenAI-compatible client — zero cloud tokens.
4. **Onboard** users with no local model, recommending the largest model their
   hardware can run and the right server to install.

The `auto_router profiles` diagnostic uses LM Studio `--estimate-only` for CPU,
50% hybrid, and full-GPU placements. It reports live RAM/VRAM headroom but does
not select or activate an execution profile until quality, TTFT p95, and
throughput have been measured separately. Every diagnostic report carries
`activation_authority=false` and `models_loaded=false`.

`profiles-benchmark` is dry-run by default. Execution requires `--execute`, an
empty LM Studio runtime, an exclusive host lock, and sufficient headroom. It
uses a temporary identifier, unloads only that identifier, and fails closed if
the final runtime state is not empty. Its result still cannot activate routing.

Related: [[llm-mcp]] (MCP tools for agents), `tiered_router` (cost tiers),
`local_router` (task→backend mapping), `response_cache` (skip repeated calls).
```
