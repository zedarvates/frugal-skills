---
name: vector-protocol
description: "Instructions for an experimental upstream fixed-width finding-vector codec and in-memory store. It encodes severity, type, file-reference hash, line and action; it is not a learned embedding or a Qdrant integration and cannot reconstruct original paths or descriptions. Retain the original findings for human reports."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: vector_protocol
---
# vector-protocol — experimental structured finding codec

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Current upstream behavior

The upstream `skills.vector_protocol` prototype encodes a finding into 24 numeric positions: severity, finding type, four bytes of a file-reference hash, a line number and an action. These are structured features, not learned semantic embeddings. The included `VectorStore` is in memory; comments about swapping it for Qdrant describe a possible integration rather than an implemented persistent backend.

`decode_vector()` returns fields such as `s`, `t`, `fh`, `l` and `a`. It cannot recover an original path from its hash or reconstruct the finding's description. Keep the original finding payload and evidence alongside the vector so a reviewer can recover the full human-readable report. Do not claim an end-to-end embedding pipeline or lossless reconstruction from vectors alone.

## Conditional upstream example

```python
from skills.vector_protocol import encode_finding, decode_vector

original = {"f": "file.py:42", "s": "err", "t": "dead", "a": "review", "d": "Check the unused function"}
vector = encode_finding(original)
summary = decode_vector(vector)
# Preserve original: summary contains fh, not the original file reference or d.
```

Measure encoded sizes and quality on actual findings before using the prototype. No token reduction, durable storage or semantic retrieval result is established here.

## When NOT to use

- For a binary message transport, consider agent-compression with its own contract.
- For durable inspectable memory, consider memory-hub.
- For complete human reports, use the original finding payload rather than the vector summary.
