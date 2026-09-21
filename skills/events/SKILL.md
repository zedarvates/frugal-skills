---
name: events
description: "Append-only JSONL decision log (.botte/events.jsonl) that every filter in the belt writes to — routing, cache hits, escalations, micro-NN outputs. The single source of truth demo mode, the live dashboard, and session replay all read from. Use when you want to see or emit a live feed of routing/cache/escalation decisions, or when building a tool that needs to watch the belt work in real time."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: events
---
# events — the unified decision log

One append-only file per project, one JSON line per decision. Nothing else in
the pipeline needs to change what it does — it just also calls `log_event`.

```bash
python -m skills.events.cli tail .           # last 20 events
python -m skills.events.cli tail . -n 50 --json
python -m skills.events.cli stats .          # summary of kinds, savings, tool calls
python -m skills.events.cli export . -o events.csv # CSV export for offline analysis
python -m skills.events.cli log route . --field out=local --field tokens_saved=210
python -m skills.events.cli clear .
```

```python
from skills.events import log_event, read_events, tail_events, follow_events

log_event("route", project_root=".", filter=1, out="local", tokens_saved=210)
tail_events(".", n=20)
for rec in follow_events("."):   # blocking generator, for --live tools
    ...
```

## Event kinds

| kind | typical fields | emitted by |
|------|-----------------|------------|
| `route` | filter, out (local/cloud), tokens_saved, reason | `auto_router.AutoRouter.decide` |
| `cache` | hit (bool), key, tokens_saved | `cache.ProjectCache` |
| `escalate` | from, to, reason | `auto_router.AutoRouter.run` |
| `tool_call` | tool, output_chars, output_tokens, elapsed_ms | agent harness / tracking |
| `nn_out` | model, probs/class | `botte_nn` predictors |
| `fusion` | strategy, models | `auto_router.fusion` |

`kind` is free-form — any skill can log its own label; the table above is
just what the showcase tools (demo mode, dashboard `--watch`, replay) render
by default.

## Design

- **Best-effort, never raises.** A logging failure must never break the
  caller — same contract as `control_loop.record`.
- **Rotation** at 5 MB, keeps the newest half — same spirit as `.botte-cache/`.
- **0 tokens, 0 network.** Pure stdlib, local file only — consistent with the
  project's "no telemetry" guarantee: this file never leaves the machine.
- **Project-scoped** (`.botte/events.jsonl`), unlike `control_loop`'s
  `~/.botte/control-ledger.jsonl` which is machine-wide — events are about
  *this* project's live activity, the ledger is about tuning the router
  globally over time.

Related: [[control-loop]] (the other ledger), [[dashboard]], [[cache]].
