---
name: metrics
description: "Instructions for collecting component-level project metrics and separating estimated context costs from measured provider usage. Use to report LOC, duplicate groups, directive health and routing observations with their scope and evidence; do not infer savings from missing counters."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: metrics
---
# metrics — quantify a project's token/cost profile

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Surfaces the numbers an audit should give you, framed around cost. A multi-stack
project (website + game server + client + tools) has **no single number**, so
everything is broken down per component.

```bash
python -m skills.metrics.cli <project>
python -m skills.metrics.cli <project> --porthos reports/<proj>/audit-report.json --json
```

## What to report

- LOC and duplicate-function candidates, grouped by component.
- Declared instruction sizes and estimated resend costs with tokenizer and turn assumptions.
- Observed backend and routing configuration, not assumed savings.
- Runtime counters with their scope and provenance; they are not a measurement of total host usage.
- Deep-audit summaries only when the underlying report is available and verified.

State which values are measured, estimated, or unavailable. Do not fill missing counters with zero or justify an optimization using an invented baseline.

Exposed via [[llm-mcp]] as the `metrics` tool. Related: [[infra-advisor]]
(auto audit), [[directives-audit]], [[skill-finder]], [[bootstrap]].
