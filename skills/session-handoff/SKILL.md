---
name: session-handoff
description: "Create, validate, and render a bounded provider-neutral session brief without storing raw transcripts or secrets. Use before switching model, agent, host, or context window."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: session_handoff
---
# session-handoff — portable continuation without hidden state

`session_handoff` captures the minimum verified state needed by another coding
agent. It is local, stdlib-only, and explicit that the receiving agent gets a
**brief**, not the original provider session.

```powershell
python -m skills.session_handoff.cli create `
  --goal "Finish the targeted change" `
  --summary "Implementation is present; targeted tests remain" `
  --completed "Added the bounded contract" `
  --next-step "Run the targeted tests" `
  --evidence "file=skills/session_handoff/handoff.py" `
  --source-agent codex `
  --output .botte/handoff.json

python -m skills.session_handoff.cli validate .botte/handoff.json
python -m skills.session_handoff.cli render .botte/handoff.json
```

The same contract is available through the lazy `session_handoff` MCP tool.
Its `create`, `validate`, and `render` actions exchange JSON objects only; MCP
does not read or write handoff files. Use `find_tool("session handoff")` to load
the schema without adding it to the always-on tool prefix.

## Contract

- Schema: `botte-session-handoff-v1`.
- Default maximum: 16 KiB, measured on the emitted UTF-8 JSON.
- Continuation mode: always `brief_only`; no cross-provider resume claim.
- Git capture: branch, full object id, dirty flag, and relative changed paths;
  inspection is read-only and no absolute workspace path is stored.
- Privacy: unknown fields, probable secrets, and raw transcript fields fail
  validation. Prompts, responses, environment variables, and terminal history
  are never collected automatically.
- Safety: an active brief needs a next step; a blocked brief needs a blocker.

The implementation is conceptually informed by Traycer's durable agent metadata
and no-transcript separation, but was written from scratch for Botte Secrète's
local-first, dependency-free architecture. See
`docs/plans/2026-08-06_traycer-inspired-session-handoff.md` for provenance.
