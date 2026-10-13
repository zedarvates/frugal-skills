---
name: demo
description: "Instructions for displaying an upstream routing dashboard from a scripted scenario or project event log. The runtime is installed separately, and scripted fixture output is not evidence of live routing or savings."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: demo
---
# demo — watch the belt decide, live

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Four panels, refreshed as decisions happen: **ROUTING**, **SAVINGS**,
**MICRO-NN**, **ESCALATIONS**. Reads from [[events]] — same data source as
`dashboard --watch` and session replay.

```bash
python -m skills.demo.cli scripted                    # built-in scenario, ~4s total
python -m skills.demo.cli scripted --speed 0 --no-clear # dump all frames, no timing
python -m skills.demo.cli live .                       # tail a real project while an agent works
python -m skills.demo.cli live . --only route,escalate  # filter specific event kinds
python -m skills.demo.cli replay .botte/events.jsonl --speed 0.3   # the "black box" — replay a real session
```

## Three modes, same renderer

- **`scripted`** — 6 fixed steps (`scenario.py`) covering every filter of the
  belt: micro-NN routing, a deterministic classifier, a cache hit, a cloud
  escalation, a verification-failure escalation, an anomaly-detector output.
  Deterministic, no dependency on a running LLM or `.botte/events.jsonl` —
  this is the mode for a README GIF or a cold-machine walkthrough.
- **`live`** — tails a real project's `.botte/events.jsonl` (written by
  [[auto-router]], [[cache]], …) while an agent works. Genuine decisions,
  genuine numbers.
- **`replay`** — the "black box": replays a captured event log at real or
  sped-up pace. Accepts a raw `.botte/events.jsonl` (JSONL, exactly what
  `events`/`auto_router` write) or a JSON array (e.g. from `events tail
  --json`) via `load_events_file()`, which auto-detects the shape. Useful for
  debugging a real routing session after the fact, demoing with real data
  without a live agent running, or as raw material for the active-learning
  loop.

All three funnel through `build_panels(events) -> list[Panel]` and
`render_grid(panels) -> str`.

## Design

- Pure stdlib ANSI (`render.py`) — no `rich`/`textual` dependency, degrades to
  plain text when `NO_COLOR` is set or stdout isn't a TTY.
- Panels trim to a fixed width so the layout never breaks on a long task
  description.
- `--no-clear` disables the screen-clear escape codes — use it for piping
  frames into a file (recording) or in this test harness.

Related: [[events]] (the data source), [[dashboard]] (the report counterpart).
