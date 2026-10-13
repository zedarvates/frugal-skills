---
name: audit-dag
description: "Guidance for the upstream audit DAG and its derived machine-facing and HTML views. Use to plan one canonical findings representation with addressable nodes; verify that derived views preserve it. Not for generating detector findings or choosing a compact JSON format alone (ultra-compact)."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: audit_dag
---
# audit-dag — one canonical audit, two derived views

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## Purpose

A single DAG of findings with addressable nodes, with proposed compact
machine-facing and HTML review views.
Deriving both views from the same DAG is intended to reduce drift. Verify that the installed renderers preserve every required finding and field.

    from skills.audit_dag import build_dag, to_compact, to_html

## When NOT to use

- You need the findings themselves — this module renders, the detectors detect.
- You only want the compact wire format — use ultra_compact.
