---
name: hailo-vision
description: "Instructions for the upstream workflow: Edge vision inference on the Hailo-8 accelerator — object detection, image classification and OCR through compiled .hef models, with the available model table, the Python API (detect, classify, ocr) and the MCP tools when the accelerator host is reachable. Use when an image or a video frame must be detected, classified or read locally at edge power. Not for extracting text from video or audio — use media-loader, which composes this; not for generating an image — use comfyui; not for the local endpoint routing decision — use local-router."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: hailo-vision
---
# Hailo-8 Vision Pipeline

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

> Instructions for evaluating a separately installed edge-vision adapter and its hardware, model and operating costs.

## Purpose

Which model serves which task (detection, classification, OCR), and how to call
it: the Python helpers and, when the accelerator host is reachable, the MCP
tools.

The full upstream model table, API and MCP usage depend on `PIPELINE.md`, which is not included here. Obtain compatible documentation and verify the installed adapter and model before inferring extraction capability.

## When NOT to use

- The media is video or audio and needs text extraction — use media_loader.
- You need an image produced — use comfyui.
- The task needs routing first — use local_router.
