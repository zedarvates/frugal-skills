---
name: agent-compression
description: "Compress inter-agent messages into a binary wire format — 4-bit quantized vectors, a shared token dictionary learned from a corpus, delta-diff between an old and a new message, and hashing of repeated sections, with a dictionary store under ~/.botte. Deterministic, local, 0 cloud tokens. Use when two or more agents exchange structured messages repeatedly and transmission volume matters more than human readability. Not for one-shot content compression of logs or tool output — use universal-compressor; not for compressing an agent's memory — use agent-intel (mem-compress); not for the report JSON format — use ultra-compact."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: agent_compression
---
# agent-compression — inter-agent binary transport

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
