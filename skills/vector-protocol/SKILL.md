---
name: vector-protocol
description: "An inter-agent protocol where agents exchange quantized embedding vectors rather than text — each agent operates on low-dimensional vectors pushed to the local vector store and only the final orchestrator decodes back to user language, for a reported 70 percent reduction across the pipeline. Use inside a fixed multi-agent pipeline where the intermediate text would never be read by a human. Not for the binary message wire format — use agent-compression; not for durable agent memory — use memory-hub."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: vector_protocol
---
# Vector Agent Protocol (P11)

## When NOT to use

- You want a message-level binary transport rather than embedding exchange —
  use agent_compression.
- You want the vectors indexed as durable, inspectable memory — use memory_hub.
Agents communicate via quantized embedding vectors, not human language.

**Trigger:** When multiple agents run in pipeline — use vectors for inter-agent comm.

**Principle:** Agents don't need to "understand" each other's text output.
They operate on 24-dimension vectors. Only the final orchestrator decodes to user language.

**Pipeline:**
```
Porthos → vectors (24 floats/finding) → Qdrant → d'Artagnan query vectors → Aramis → Athos (decode to French)
```

**Token savings:** -70% pipeline (no inter-agent text interpretation)

**Module:** `skills/vector_protocol`
**Vectors:** 24-dimension, quantized [0.0, 1.0]
**Backend:** Qdrant on the inference host:6333
