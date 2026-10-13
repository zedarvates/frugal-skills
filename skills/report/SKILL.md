---
name: report
description: "Instructions for the upstream workflow: Persist any audit as a timestamped Markdown and/or HTML file (name + date + time) under .botte/reports/, browsable at any time, and list saved reports. Use when the user wants audits saved to consultable files, a history of audits, or to export a checkup/metrics/infra report as .md or .html."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: report
---
# report — audits saved as timestamped, consultable files

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Audits print to the console; this keeps them. Any report dict → a self-contained
`<name>_<YYYY-MM-DD_HHMMSS>.md` and/or `.html` under `.botte/reports/`.

## Save an audit

The audit CLIs take `--save [md|html|both]`:

```bash
python -m skills.checkup.cli .        --save both   # checkup_2026-06-20_142838.md/.html
python -m skills.metrics.cli .        --save html
python -m skills.infra_advisor.cli auto . --save md
```

## Browse them any time

```bash
python -m skills.report.cli list                # most recent first
python -m skills.report.cli list --json
```

## Programmatic

```python
from skills.report import save, list_reports
save("audit", report_dict, fmt="both", out_dir=project/".botte"/"reports")
list_reports(project/".botte"/"reports")
```

The renderer handles scalars, lists, list-of-dicts → tables, nested dicts, and
ASCII `diagram` fields as code blocks. `.botte/` is gitignored, so reports stay
local per machine/project. Exposed via [[llm-mcp]] as `list_reports`. Related:
[[checkup]], [[metrics]], [[infra-advisor]], [[app-test]] (its own HTML report).
