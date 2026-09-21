---
name: media-loader
description: "Extract text from media before any model sees it — video keyframes through the local vision accelerator, audio through local speech to text, image detection/classification/OCR, and PDF or scanned document OCR — so the model receives a text summary instead of raw bytes, for a reported 90 to 99 percent saving on media-heavy tasks. Use whenever a task involves video, audio, image or scanned document input. Raw media is never sent to a model: this module is that extraction step. Not for generating images — use the local image endpoint through local-router; not for choosing which local endpoint exists — use local-router."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: media_loader
---
# media-loader — never send raw media to a model

## Purpose

Step 1 is local extraction, step 2 is the model reading text. Video becomes a
keyframe summary, audio becomes a transcript, images become structured JSON,
documents become text.

    Video  -> local keyframe extraction + classification -> text summary
    Audio  -> local speech to text -> transcript
    Image  -> local detect / classify / OCR -> structured JSON
    PDF    -> local OCR -> text

## When NOT to use

- You want an image produced, not read — use local_router's image endpoint.
- You want to know which local capability is available — use local_router.
- The input is already text — no extraction is needed.
