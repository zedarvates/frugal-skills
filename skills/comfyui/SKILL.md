---
name: comfyui
description: "Local image generation through the ComfyUI HTTP API — queue a workflow, set the prompt node, read system stats and available models, with reusable workflow templates for text-to-image, hires fix, image-to-image and inpainting. Use when an image must be generated without a paid image API. Requires the local ComfyUI instance to be reachable; the host is configured in the integration doc. Not for reading or describing an image — use hailo-vision or media-loader; not for routing a task to a local endpoint — use local-router."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: comfyui
---
# ComfyUI Integration — local image generation

> Zero cloud API costs for image generation.

## Purpose

How to call the local ComfyUI instance from this project: point a workflow at the
prompt node, POST it, and reuse the templates shipped with the project.

Templates referenced: text-to-image basic, text-to-image with hires fix,
image-to-image, inpainting.

The full integration text, including the exact host and the API call, is in
[INTEGRATION.md](INTEGRATION.md).

## When NOT to use

- You need to read, classify or OCR an image — use hailo-vision via media_loader.
- You need the task routed to the right local endpoint — use local_router.
- The instance is unreachable: this is local-only, there is no cloud fallback.
