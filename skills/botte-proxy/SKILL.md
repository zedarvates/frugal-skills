---
name: botte-proxy
description: "Instructions for the upstream HTTP compression proxy between an agent and its configured LLM endpoint. Use to plan proxy integration and inspect compression behavior. Runtime and target endpoints are separate prerequisites; remote or cloud targets receive forwarded data, and savings require measurement."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: botte_proxy
---
# Botte Proxy

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

Transparent HTTP proxy that compresses LLM API requests before forwarding them. Inspired by Headroom's proxy mode.

## Features

- **Transparent** — sits between any OpenAI-compatible agent and its LLM API
- **Universal compression** — uses Universal Compressor's smart routing (JSON, code, logs, tool output)
- **No proxy restoration** — the current proxy calls compression with `reversible=False` and exposes no restore route. The universal-compressor's separate in-process restoration API is not a proxy recovery guarantee.
- **Dashboard** — real-time savings dashboard at `http://localhost:PORT/dashboard`
- **Stats API** — JSON stats at `http://localhost:PORT/stats`
- **Destination-dependent privacy** — a loopback target keeps forwarding on this machine; a remote target sends requests to that host, and a cloud target sends them to the provider. Inspect the configured target and its data-handling policy before sending content.

## Usage

```bash
# Start proxy (default target: http://localhost:11434/v1 for Ollama/LocalAI)
python -m skills.botte_proxy.cli proxy --port 8787

# With specific target
python -m skills.botte_proxy.cli proxy --target http://inference-host.example:11434/v1 --port 8787

# With OpenAI
python -m skills.botte_proxy.cli proxy --target https://api.openai.com/v1 --api-key $OPENAI_API_KEY

# View stats
python -m skills.botte_proxy.cli stats

# View dashboard
open http://localhost:8787/dashboard
```

## Agent Integration

Point any OpenAI-compatible agent at the proxy:

```bash
# Claude Code
CLAUDECODE_API_BASE=http://localhost:8787 claude

# Any OpenAI client
export OPENAI_BASE_URL=http://localhost:8787/v1

# Generic
export OPENAI_API_BASE=http://localhost:8787/v1
```

## Architecture

```
Agent → Proxy (port 8787) → Compress messages → Forward → LLM API
         ↓
      Dashboard (/dashboard)
      Stats (/stats)
```
