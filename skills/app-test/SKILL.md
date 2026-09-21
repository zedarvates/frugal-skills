---
name: app-test
description: "Local-first GUI/app testing by image matching (SikuliX) — turn a small JSON spec referencing your button images into a runnable SikuliX script and run it locally, using a vision NPU (Hailo-8/10) or local vision model instead of cloud vision. Use when the user wants to test a desktop/game/web app 'for real' by clicking buttons, has button images already, or mentions SikuliX, image-matching tests, or local UI tests."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: app_test
---
# app-test — test apps locally by clicking their buttons

When you build a UI you already have the button images, so an image-matching bot
can drive it — no cloud vision tokens needed. A tiny JSON spec → a runnable
SikuliX script.

## Spec → script → run

```bash
python -m skills.app_test.cli gen tests/login_flow.json     # print the SikuliX script
python -m skills.app_test.cli run tests/login_flow.json --out build
python -m skills.app_test.cli verify tests/login_flow.json \
  --runner-output build/runner.log --runner-exit 0 \
  --artifacts build/login_flow.sikuli/artifacts \
  --out build/login_flow-evidence.json \
  --report build/login_flow-report.html
```

```json
{
  "name": "login_flow",
  "image_dir": "tests/images",
  "similarity": 0.8,
  "steps": [
    {"do": "wait",           "image": "login_btn.png", "timeout": 10},
    {"do": "click",          "image": "login_btn.png"},
    {"do": "type",           "text": "user@example.com"},
    {"do": "click",          "image": "submit.png"},
    {"do": "assert_visible", "image": "welcome.png", "timeout": 8},
    {"do": "assert_absent",  "image": "error.png"}
  ]
}
```

Actions: `wait · click · double_click · right_click · type · sleep ·
assert_visible · assert_absent`.

## Running it

Uses **OculiX** (the maintained SikuliX fork: OpenCV matching + embedded
Tesseract OCR, Java) — or any SikuliX. The generated `-r <bundle>` scripts are
drop-in compatible with both.

Install OculiX (Java 11+ required): download the platform "ide" jar from
https://github.com/oculix-org/Oculix/releases and place it at
`~/.oculix/oculixide.jar` (auto-detected), or set `OCULIX_JAR=/path/to/jar`.
`runsikulix`/`oculix` on PATH also work. `run` always generates the `.sikuli`
bundle; it executes it via `java -jar <jar> -r <bundle> -c` when a runner is
found, else it reports how to install one.

Verified: a generated bundle runs end-to-end on OculiX 3.0.4
(`oculixide-3.0.4-windows.jar`) — Jython executes the steps and returns the exit
code (0 = pass).

## Why local / economical

Image matching is CPU-cheap and needs no model. For richer checks (is this screen
*semantically* right?), point verification at a **Hailo-8/10 NPU** or a local
vision model via [[llm-backends]] instead of a paid cloud vision API — 0 cloud
tokens. The generator is deterministic and unit-tested; the GUI run is local.

Every executed run also emits `*-evidence.json`. The manifest binds the scenario
to per-step screenshot SHA-256 digests without embedding raw pixels, paths, or
typed text. A nominal exit code cannot produce `passed` when the result marker or
an expected valid PNG screenshot is missing; the verdict is `unverified` instead.
CLI exit codes are `0=passed`, `1=failed`, and `2=unverified/not run`.
When an AutoRouter execution supplied a `task_run_id`, pass it with
`--task-run-id` and `--efficiency-root`. The deterministic manifest then records
the final ledger verdict; runner exit or non-empty output alone never does.

Related: [[llm-backends]] (local vision backends), [[metrics]].
