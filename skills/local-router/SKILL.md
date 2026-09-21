---
name: local-router
description: "Route a task to a local model when the hardware can serve it — a task-type taxonomy (simple text, complex reasoning, vision classify/detect/OCR, speech to text, text to speech, image generation) mapped onto the local endpoints already present, for a reported 40 to 60 percent of cloud tokens moved local. Use when a task is cheap enough to run on local hardware. Not for deciding the model tier from task complexity — use nn-router; not for selecting a tool — use tool-router; not for the extraction step that turns media into text before a model sees it — use media-loader."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: local_router
---
# local-router — prefer local over cloud

## Purpose

Classifies a task by type and routes it to the local capability that can serve
it (vision accelerator, local text and voice endpoint, local image endpoint),
keeping the paid path for what actually needs it.

    from skills.local_router import ...

Tasks and hardware are declared as an enum, so an unavailable capability is
visible rather than silently escalated to a cloud call.

## When NOT to use

- The question is which model tier, not which host — use nn_router.
- The question is which tool to call — use tool_router.
- You have raw media to prepare — use media_loader first.
