---
name: ingest
description: "Instructions for fetching and extracting source text, optionally structuring it with a configured model, and storing it through a separately installed Qdrant service. Verify endpoints and embedding mode; hash features are not semantic embeddings. Use for source ingestion and recall."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: ingest
---
# ingest — scrape the web & build a knowledge foundation, locally

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Scraping and ingesting are extraction/transformation — keep them off the cloud.

```bash
python -m skills.ingest.cli scrape  https://example.com --structure   # local summary+entities
python -m skills.ingest.cli ingest  https://example.com --collection foundation
python -m skills.ingest.cli ingest  ./notes.md --file
python -m skills.ingest.cli search  "topic"  --collection foundation
```

- **scrape** — fetch (browser UA) + stdlib HTML→text (drops script/style, keeps
  title). `--structure` asks a LOCAL model for a 3-bullet summary + key entities.
  Verify the selected endpoint and actual model usage.
- **ingest** — scrape (or a file/raw text) → reflect locally → upsert into Qdrant
  (`inference-host.example:6333` by default). Builds the "foundation"/historical store.
- **search** — recall from a collection.

Embeddings: **auto-resolve a local `/v1/embeddings` endpoint** from the backend
registry (any reachable backend exposing an embedding model → real semantic
vectors), falling back to a deterministic hash n-gram (256-dim) when none is
available. This fallback does not establish semantic retrieval quality or service availability. Override with
`--embed-url`/`--embed-model`. The result reports `embed: endpoint|hash`. Check and report failures of Qdrant, source access or extraction; do not infer ingestion success from a successful scrape.

```bash
python -m skills.ingest.cli ingest https://example.com --embed-url http://127.0.0.1:1234/v1/embeddings
```

Exposed via [[llm-mcp]] as `scrape` and `ingest_source`. Related:
[[hermes-second-brain]] (the foundation concept), `media_loader`, [[auto-router]].
