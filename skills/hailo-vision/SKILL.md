---
name: hailo-vision
description: "Edge vision inference on the Hailo-8 accelerator — object detection, image classification and OCR through compiled .hef models, with the available model table, the Python API (detect, classify, ocr) and the MCP tools when the accelerator host is reachable. Use when an image or a video frame must be detected, classified or read locally at edge power. Not for extracting text from video or audio — use media-loader, which composes this; not for generating an image — use comfyui; not for the local endpoint routing decision — use local-router."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: hailo-vision
---
# Hailo-8 Vision Pipeline

> Edge AI vision — zero cloud API costs, low TDP.

## Purpose

Which model serves which task (detection, classification, OCR), and how to call
it: the Python helpers and, when the accelerator host is reachable, the MCP
tools.

Read the model table, the API and the MCP usage in [PIPELINE.md](PIPELINE.md).

## When NOT to use

- The media is video or audio and needs text extraction — use media_loader.
- You need an image produced — use comfyui.
- The task needs routing first — use local_router.
