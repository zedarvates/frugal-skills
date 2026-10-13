---
name: capabilities
description: "Guidance for the upstream capability registry and lexical curator, organized as SENSE, DECIDE, ACT, REMEMBER, GOVERN and DEPLOY. Use to inspect the toolkit map or plan capability selection. A catalog entry describes a workflow; it does not prove that its runtime is installed or available."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: capabilities
---
# capabilities — the system's map of itself (registry + curator)

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The upstream registry organizes available module descriptions into a layered tree for planning. Inventory entries must be checked against actual installed capabilities.

```bash
python -m skills.capabilities.cli map               # ASCII layered system tree
python -m skills.capabilities.cli list --json       # the registry
python -m skills.capabilities.cli curate "test my desktop app"
```

## Layers (the arborescence)

| Layer | Role |
|-------|------|
| **SENSE** | understand project / cluster / task |
| **DECIDE** | route the work, cheapest capable |
| **ACT** | do the work, local-first |
| **REMEMBER** | capitalise (compounding) |
| **GOVERN** | consistency & cost control |
| **DEPLOY** | wire into projects & measure |

Each skill's layer comes from a `layer:` field in its SKILL.md frontmatter, else
a built-in map, else ACT. The generated `docs/system-map.txt` snapshot belongs to the upstream runtime and is not bundled here.

## The curator

`curate(goal)` ranks the capabilities most relevant to a goal (local lexical
match) — the librarian that hands the Conductor (and you) the right
branches of the tree to use. Built on [[skill-finder]].

This registry is the foundation for the Conductor (goal → decision tree → ordered
plan of capabilities, executed local-first) and the control loop (measure → adapt).
Related: [[skill-finder]], [[auto-router]], [[bootstrap]].
