---
name: statusline
description: "One-line summary of the belt's session activity (tokens saved, cache hits, local/cloud split, escalations) for a terminal statusline — Claude Code's statusLine hook, tmux, or any shell prompt. Reads .botte/events.jsonl. Use when the user wants a persistent, passive view of savings while they work, or asks to set up a statusline."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: statusline
---
# statusline — the savings, always visible

```bash
python -m skills.statusline .              # one line, safe to embed anywhere
python -m skills.statusline --compact .    # number only, for narrow surfaces
python -m skills.statusline --json .       # ambient-status-v1 contract
```

```
🧦 botte · 12,480 tok saved (host) · 41 cache hits · 17L/3C · 2 escalated
```

Reads the same scoped `ambient-status-v1` snapshot as [[dashboard]]. Routing
savings come from the host control ledger; route/cache/escalation activity comes
from the selected project's `.botte/events.jsonl`. The scopes stay explicit in
JSON and the human line labels host savings. The statusline is passive, uses 0
tokens, and has no state of its own. Invalid host counters render as
`unavailable`, never zero. `render()` never raises.

## Wiring it into Claude Code's statusline

This module does **not** modify your Claude Code settings — wire it in
yourself (or ask an agent to, via the `update-config` skill) by adding to
`.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "python -m skills.statusline"
  }
}
```

The CLI also accepts a JSON payload on stdin (Claude Code's statusline hook
convention) and best-effort reads `cwd`/`workspace`/`project_dir` from it, so
it works whether invoked with an explicit path or piped session context.

## Design

- **Best-effort, never blocks the prompt** — any failure (missing file,
  malformed JSON, no `.botte` dir) falls back to a plain `🧦 botte` rather
  than raising or hanging.
- **0 network, 0 tokens** — pure local file reads, same guarantee as [[events]].

Related: [[events]] (the data source), [[demo]], [[dashboard]] (the richer views),
[[ambient-hud]] (the passive top-center desktop view).
