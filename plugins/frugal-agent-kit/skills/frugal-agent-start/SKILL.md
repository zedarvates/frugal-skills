---
name: frugal-agent-start
description: "Introduce Frugal Agent Kit and help a user select a bounded, read-only review workflow. Use after installation or when the user asks how to start. Never claim an external tool was run."
---
# Frugal Agent Kit — start

This is a skills-only review assistant, not the complete executable Frugal Skills Python catalog.

1. Ask for one task, workflow, or completion report, if the user has not already provided one.
2. Choose exactly one of `context-budget-review`, `tool-route-review`, or `evidence-before-done`, based on the request.
3. State the inputs needed and perform a bounded analysis of the supplied information.
4. Label any estimate or missing evidence. Never invent tokens, monetary savings, latency, tests, executed tools, or real-world access.
5. Obtain explicit authorization before any write, publish, merge, purchase, external message, or execution.

The upstream implementation catalog is documented at https://github.com/zedarvates/frugal-skills . No upstream scripts or models are bundled or automatically installed.
