---
name: docgen
description: "Instructions for drafting documentation or session notes with separately configured model backends. Confirm the selected local and cloud endpoints, data handling and costs before invocation. Use for documentation and session summaries; not for prompt-prefix analysis."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: docgen
---
# docgen — local-drafted docs (cloud-refined) + session review

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Documentation is verbose, so the LOCAL model writes the first draft and the cloud
model is spent only on a final polish — the video's "pre-write local, correct
with cloud" pattern, built on [[auto-router]]'s `draft_refine` fusion.

```bash
python -m skills.docgen.cli draft "deploy the service" --kind guide
python -m skills.docgen.cli draft "auth module" --kind module
python -m skills.docgen.cli session ~/.claude/projects/.../transcript.jsonl
python -m skills.docgen.cli session "user: did X\nassistant: built Y" --text
```

- **draft** — local model drafts (`readme|module|changelog|guide|adr`); cloud
  refines **only if a key is set** (otherwise you keep the local draft, marked
  un-refined). Verify backend choice, configured forwarding and provider usage.
- **session** — reads a transcript (Claude Code `.jsonl`, markdown, or raw text)
  and a configured model may return `done / decisions / learnings / next`. Measure the actual call.

Exposed via [[llm-mcp]] as `draft_doc` and `session_review`. Pairs with
[[ingest]] (pull sources to document) and [[checkup]] (what changed this session).
