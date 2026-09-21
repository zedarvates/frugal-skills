---
name: audit-dag
description: "Build one canonical machine-first audit as a DAG of findings, then derive two views from it: an ultra-compact form for LLMs where every node stays addressable and nothing is dropped, and an HTML report for humans (build_dag, to_compact, to_html). The DAG is the single source and the views are derived, so the agent-facing and human-facing reports can never disagree. Use when an audit must stay complete for an agent while remaining readable by a person. Not for the detectors themselves — use code-complexity, code-duplication, code-state and code-wrappers; not for the compact JSON format in isolation — use ultra-compact."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: audit_dag
---
# audit-dag — one canonical audit, two derived views

## Purpose

A single DAG of findings with addressable nodes, rendered twice: ultra-compact
for the model (nothing forgotten, every node reachable) and HTML for review.
Building the DAG once removes the drift between an agent summary and a human
report generated separately.

    from skills.audit_dag import build_dag, to_compact, to_html

## When NOT to use

- You need the findings themselves — this module renders, the detectors detect.
- You only want the compact wire format — use ultra_compact.
