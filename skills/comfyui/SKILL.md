---
name: comfyui
description: "Instructions for a separately installed ComfyUI HTTP workflow: prompt-node configuration, queueing, model inspection and workflow templates. Use to plan image generation with a configured local instance. The host, models, templates and upstream INTEGRATION.md are not supplied here. Not for image reading or local endpoint routing."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: comfyui
---
# ComfyUI Integration — local image generation

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

Use only an explicitly configured compatible local ComfyUI instance; this catalog provides no image-generation runtime or cost measurements.

## Purpose

The upstream workflow points a ComfyUI graph at a prompt node and queues it through HTTP. Confirm the configured instance, installed models and reviewed workflow before sending a request; no templates are shipped in this catalog.

Templates referenced: text-to-image basic, text-to-image with hires fix,
image-to-image, inpainting.

The upstream `INTEGRATION.md` and workflow templates are separate resources, not bundled here. Obtain the compatible integration text and the user's actual configured host before making an API call; do not invent an endpoint or a template.

## When NOT to use

- You need to read, classify or OCR an image — use hailo-vision via media_loader.
- You need the task routed to the right local endpoint — use local_router.
- The instance is unreachable: this is local-only, there is no cloud fallback.
