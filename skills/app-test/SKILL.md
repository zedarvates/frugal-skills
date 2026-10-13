---
name: app-test
description: "Guidance for upstream image-matching GUI tests with OculiX/SikuliX: prepare a JSON scenario, button images, runner and evidence checks. Use for local desktop, game or web UI testing. Runtime, Java, screenshots and optional local vision hardware are separate prerequisites; an installation is not proof of a passed test."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: app_test
---
# app-test — test apps locally by clicking their buttons

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

With supplied button images, the upstream image-matching workflow can generate a SikuliX script from a JSON scenario. Image files, the generator and the GUI runner must be available separately.

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

Verify a generated bundle against your installed OculiX/SikuliX version. This catalog includes no end-to-end runner evidence; a nominal runner exit code alone is not proof that all scenario checks passed.

## Why local / economical

Image matching can operate without a vision model. Richer semantic checks require a separately configured vision backend, such as a compatible NPU or local model through [[llm-backends]]. Measure usage and validate the generated script and GUI run; this catalog supplies no generator tests or executed-run evidence.

Every executed run also emits `*-evidence.json`. The manifest binds the scenario
to per-step screenshot SHA-256 digests without embedding raw pixels, paths, or
typed text. A nominal exit code cannot produce `passed` when the result marker or
an expected valid PNG screenshot is missing; the verdict is `unverified` instead.
CLI exit codes are `0=passed`, `1=failed`, and `2=unverified/not run`.
When an AutoRouter execution supplied a `task_run_id`, pass it with
`--task-run-id` and `--efficiency-root`. The deterministic manifest then records
the final ledger verdict; runner exit or non-empty output alone never does.

Related: [[llm-backends]] (local vision backends), [[metrics]].
