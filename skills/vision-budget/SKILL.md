---
name: vision-budget
description: "Deterministic preflight for local full-frame versus ROI visual-token budgets, evidence coverage, verifier fallback, privacy, and cache separation."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: vision_budget
---
# vision-budget — local ROI planning preflight

Use this skill to estimate whether a coarse-to-fine local vision pipeline is
worth a real VLM benchmark. It is pure stdlib and does not run a vision model.

## Commands

```text
python -m skills.vision_budget.test_vision_budget
python -m skills.vision_budget.benchmark --json
python -m skills.vision_budget.runtime_benchmark MODEL --json
python -m skills.vision_budget.resolution_benchmark MODEL \
  --trials 3 --sizes 224 168 112 --json
python -m skills.vision_budget.ui_benchmark MODEL --trials 3 --json
python -m skills.vision_budget.timing_benchmark MODEL --trials 3 --json
python -m skills.vision_budget.resource_benchmark snapshot --json
python -m skills.vision_budget.resource_benchmark probe MODEL \
  --min-system-available-mib 2048 --json
python -m skills.vision_budget.candidate_screen \
  --record-load-failure MODEL --placement cpu --json
python -m skills.vision_budget.candidate_screen --json
```

The default report is machine-local:
`.botte-cache/vision-budget-preflight.json`.

## Contract

1. Preserve a low-budget full-frame context pass.
2. Select at most two evidence regions by default.
3. Verify required-region coverage deterministically.
4. On any detector miss, fall back to a local full-frame pass.
5. Never store images, screenshots, OCR text, prompts, or secrets in reports.
6. Key caches by image digest, normalized regions, model/runtime/preprocessing
   versions, prompt class, and visual-token budget.

The built-in 70/280/1120 budgets are planning assumptions, not exact model
token counts. Every report has `activation_authority=false`. A production route
still requires a loaded local multimodal model, exact token evidence, measured
quality, p50/p95 latency, peak VRAM, and same-dataset comparison.

`runtime_benchmark` uses only an already-loaded model through a private LM
Studio endpoint. It generates PNG fixtures in memory, requests a strict
`{"answer": "..."}` schema, stores no image/prompt/answer content, and writes
`.botte-cache/vision-budget-runtime.json`. Exact API input tokens include both
text and vision; they do not by themselves isolate visual-token counts. The
probe compares full frame, multi-image ROI, and a single contact-sheet mosaic.

`resolution_benchmark` keeps the same local/private and privacy-safe contract,
then sweeps bounded 224/168/112 px crop sizes inside the mono-image mosaic. It
writes `.botte-cache/vision-budget-resolution.json`, which remains separate
from runtime routing and always carries `activation_authority=false`.

`ui_benchmark` compares full frame with the 168 px experimental reference on
five deterministic UI/OCR screens: status badge, invoice total, dialog action,
table row, and detector-miss alert. Corpus metadata stores only task classes,
dimensions, digests, and region counts; labels and raster payloads remain local.
The measured CPU probe preserved 15/15 quality and saved 41.32% input tokens,
but failed the p95 latency gate and therefore did not activate routing.

`timing_benchmark` keeps that same corpus and schema but streams the response to
separate PNG/base64/request preprocessing, TTFT/prefill, and decode. It writes
`.botte-cache/vision-budget-ui-ocr-timing.json`, requires final stream usage,
and stores no content. Use `--fresh-load-observed --load-time-ms N` only when
the operator measured the immediately preceding load; the claim fails closed
without a load duration. The report is diagnostic and never activates routing.

`resource_benchmark snapshot` captures a short-lived preload RAM baseline for
the bounded LM Studio process group. After the operator loads a CPU VLM,
`resource_benchmark probe` measures one structured full-frame inference and
writes `.botte-cache/vision-budget-resource.json`. It stores no command line or
content, labels process-group attribution as inexact, requires a baseline no
older than ten minutes, and never substitutes CPU RAM for VRAM. The optional
`--min-system-available-mib` gate is copied into the report and fails closed
when sampled available RAM drops below the declared experiment threshold.

`candidate_screen` inventories only local LM Studio models explicitly marked
vision-capable, then runs CPU and full-GPU `--estimate-only` checks at a bounded
4096-token context. It never loads a model. The default gates retain 2048 MiB
system RAM and 512 MiB VRAM after the estimated load. A recommendation grants
permission for a bounded probe only; quality, tokens, and latency remain
unmeasured and routing remains inactive.

An operator may record an already-observed load failure with
`--record-load-failure`. The machine-local
`.botte-cache/vision-budget-loadability.json` report binds it to the exact
selected LM Studio engine, placement, architecture, and a SHA-256 identity over
bounded model metadata. The screen blocks only that exact pair. A different
runtime or model identity does not inherit the failure. Raw errors and command
lines are excluded; malformed evidence fails closed.

The 2026-08-08 smoke follow-up rejected `ternary-bonsai-27b` before inference:
the selected LM Studio runtime returned `load-error` while loading its `dspark`
GGUF. Estimate-only eligibility and a `vision=true` inventory flag therefore do
not establish runtime loadability. That failure is now applied only to CPU on
`llama.cpp-win-x86_64-nvidia-cuda12-avx2@2.27.1`. No UI/OCR matrix or routing
change followed.
