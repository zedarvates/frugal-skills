---
name: media-loader
description: "Instructions for assessing the upstream media-loader prototype. Its current video, audio, image and PDF paths include simulated or placeholder extraction results, not a working media pipeline. Use to plan and verify real adapters; never present placeholder text or detections as extracted evidence."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: media_loader
---
# media-loader — prototype adapter planning

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Current upstream limitations

The inspected upstream `skills.media_loader` implementation contains simulated video-frame metadata, placeholder speech transcripts, mock image detections/OCR and PDF text placeholders. These outputs are scaffolding, not evidence extracted from a user's media. Installing the runtime or naming a Hailo/local service does not by itself connect working extraction adapters.

Use this skill to plan and validate a real extraction integration. Report that the prototype is incomplete before any requested extraction. Do not present a placeholder transcript, frame classification, detection or OCR string as a measured result. If no verified adapter is available, use a separately available extraction tool within the task scope or explain the missing prerequisite.

## Adapter verification

1. Inspect the installed implementation and identify the actual video, audio, image or PDF adapter.
2. Confirm supported formats, models, hardware and service endpoints; determine whether media is sent to a local or remote model.
3. Run a known fixture through the real adapter and compare its result with expected evidence.
4. Preserve provenance, failures and uncertainty in any extracted text summary.
5. Measure input sizes, quality and actual model usage. This catalog establishes no reduction percentage or guarantee that raw media avoids every model.

## When NOT to use

- For generating media, use an available generation workflow.
- For an existing verified media-extraction tool, use that tool directly rather than the prototype's placeholders.
- For plain text input, no media adapter is needed.
