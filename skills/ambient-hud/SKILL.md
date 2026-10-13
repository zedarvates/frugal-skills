---
name: ambient-hud
description: "Instructions for the upstream ambient-status-v1 Windows overlay and its scoped metrics. Use to plan passive token and routing visibility outside the terminal. Requires a separately installed compatible runtime and valid local ledgers; missing measurements stay unavailable."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: ambient_hud
---
# Ambient HUD

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

Open the read-only top-center overlay manually:

```powershell
python -m skills.ambient_hud .
```

The collapsed line shows host token savings beside project-local/cloud routes.
Click the bar or title to expand the rich dark card with model tier chips,
local/cloud ratio bar, detailed metric tiles (`LOCAL`, `CLOUD`, `CACHE`, `ESCALATE`),
and success/escalation rates.

Drag anywhere on the header or title bar to reposition the floating widget anywhere
on your screen. Click `📊 Full Report` (or press `R` / `D`) to generate and view
the complete project dashboard in your browser. Press `Escape` or click `×` to close it.

```powershell
python -m skills.ambient_hud --interval 10 .  # slower local refresh
python -m skills.ambient_hud --monitor cursor .  # monitor under mouse (default)
python -m skills.ambient_hud --monitor primary . # explicit primary fallback
python -m skills.ambient_hud --print .        # headless one-line preview
```

## Boundaries

- The upstream overlay uses `tkinter`; opening its full report may launch a browser. Check the separately installed runtime and its dependencies.
- Reads `ambient-status-v1` directly; it never parses prompts or session text.
- Consumes only snapshots accepted by the upstream contract validator.
- Never exposes project paths in the window.
- Missing measurements remain `unavailable`; they are not rendered as zero.
- Partial or invalid local ledgers degrade one scope without hiding the other.
- No launch-at-login or automatic startup. Opening the HUD is always explicit.
- On Windows, stdlib `ctypes` reads the native monitor work area through
  `GetCursorPos`, `MonitorFromPoint`, and `GetMonitorInfoW`. Virtual desktop
  coordinates may be negative. Other systems and API failures fall back to the
  primary Tk screen.
- Monitor selection happens once at launch; the HUD does not follow the mouse.

Related: [[statusline]], [[dashboard]], [[events]], [[control-loop]].
