---
name: agent-compression
description: "Instructions for the upstream inter-agent binary transport: quantized vectors, shared dictionaries, deltas and repeated-section hashes. Use when repeated machine-facing messages need a compact wire format. Not for human-readable payloads, content compression (universal-compressor), memory compression (agent-intel) or report JSON (ultra-compact)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: agent_compression
---
# agent-compression — inter-agent binary transport

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## Purpose

A wire format for messages that agents send to each other. Raw text between
agents is treated as the cost driver: vectors are quantized to 4 bits, frequent
tokens go through a shared dictionary, a message is sent as a delta against the
previous one where possible, and repeated sections are replaced by hashes.

    python -m skills.agent_compression.cli compress "message texte"
    python -m skills.agent_compression.cli delta "ancien" "nouveau"
    python -m skills.agent_compression.cli learn < corpus.txt
    python -m skills.agent_compression.cli stats

## When NOT to use

- A human will read the payload — the format is binary, not meant to be read.
- The payload is a log or a tool output rather than an agent message —
  use universal_compressor.
- You want to compress accumulated agent memory — use agent_intel (mem-compress).
