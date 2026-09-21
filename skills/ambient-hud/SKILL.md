---
name: ambient-hud
description: "Show the scoped ambient-status-v1 metrics in a local, top-center Windows overlay. Use when the user wants passive token/routing visibility outside the terminal."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: ambient_hud
---
# Ambient HUD

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

- Pure stdlib (`tkinter`), with no service, browser, network, or dependency.
- Reads `ambient-status-v1` directly; it never parses prompts or session text.
- Consumes only snapshots accepted by the bundled stdlib contract validator.
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
