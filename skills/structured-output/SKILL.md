---
name: structured-output
description: "Compact LLM-facing JSON and optionally emit round-trip-verified TOON for beneficial tabular data."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: structured_output
---
# structured-output — adaptive JSON/TOON presentation

Use this module at the boundary between programmatic JSON data and LLM-facing
text. JSON remains canonical for storage, APIs, schemas, JSON-RPC, caches, and
model artifacts.

## Contract

- Default output is strict compact JSON.
- `auto` considers only the implemented TOON v3.3 tabular subset.
- TOON requires a successful encode/decode round-trip.
- TOON requires at least 10% estimated savings and 32 estimated source tokens.
- Unsupported, small, or non-beneficial data falls back to compact JSON.
- Non-JSON text is preserved byte-for-byte.
- The dependency-free estimate is `ceil(characters / 4)` and is never
  activation-eligible.
- MCP TOON requires an active per-model profile by default. The profile requires
  an exact counter, zero fidelity failures, at least 10% aggregate incremental
  savings, and paired JSON/TOON comprehension evidence with no TOON regression.
- Formatting/tokenization p95 must fit both a 50 ms absolute ceiling and 10% of
  the measured JSON TTFT p95 for that model.
- Runtime loading revalidates the current quality report, model fingerprint,
  eligibility, and digest. Replaced or stale evidence disables the profile.

Supported TOON shapes:

- JSON primitives;
- primitive arrays;
- flat objects containing primitives or supported arrays;
- uniform non-empty object arrays with identical keys and primitive values.

Deep objects, mixed arrays, and nested cell values remain JSON.

## Commands

```bash
python -m skills.structured_output.test_structured_output
python -m skills.structured_output.benchmark
python -m skills.structured_output.benchmark --json --repeat 50
python -m skills.structured_output.comprehension MODEL --json
python -m skills.structured_output.candidate_latency MODEL --trials 3 --json
python -m skills.structured_output.candidate_latency MODEL --trials 3 \
  --response-mode structured --json
python -m skills.structured_output.profile MODEL --counter heuristic --json
python -m skills.structured_output.profile MODEL --counter lmstudio_sdk \
  --endpoint localhost:1234 --activate --json
```

Exact counter adapters are available for llama.cpp `/tokenize`, vLLM
`/tokenize`, an explicit tiktoken encoding, a locally cached Hugging Face
tokenizer, and an already-loaded model through the optional LM Studio Python
SDK. HTTP adapters refuse public hosts and redirects.

## MCP opt-in

```text
BOTTE_MCP_OUTPUT_FORMAT=json|toon|auto
BOTTE_MCP_OUTPUT_MODEL=exact-consumer-model-id
BOTTE_MCP_TOON_MIN_SAVINGS=0.10
BOTTE_MCP_TOON_MIN_TOKENS=32
BOTTE_MCP_TOON_REQUIRE_PROFILE=1
BOTTE_MCP_TOON_PROFILE_PATH=.botte-cache/structured-output-profiles.json
BOTTE_MCP_FORMAT_TELEMETRY=0|1
```

`json` is the default. These settings affect only JSON-shaped tool text inside
MCP results. Missing, inactive, stale, inexact, slow, quality-unverified, or
failed profiles select compact JSON. `BOTTE_MCP_TOON_REQUIRE_PROFILE=0` is a
diagnostic override, not a production activation path. The JSON-RPC transport
and tool schemas always remain JSON.

When enabled, telemetry is a machine-local aggregate under `.botte-cache/`.
It stores format/reason counts, total token counts, exact-call count, and
latency totals/maxima. It never stores source text, output text, or raw model
paths.

The paired comprehension report is also machine-local under `.botte-cache/`.
It stores case IDs, correctness, token counts, and latency only; prompts,
payloads, expected answers, and model answers are excluded.

`candidate_latency` measures formatting plus generation only for values that
clear the exact adaptive gates. Its report has `activation_authority=false`;
it diagnoses typical and tail latency but cannot activate a model profile.
`--response-mode final` measures the free `FINAL:` contract, while
`--response-mode structured` uses the LM Studio schema constraint to isolate
bounded answer generation. The modes write separate machine-local reports.

## Safety

- Do not persist auto-selected output as canonical state.
- Do not name a fallback JSON file `.toon`.
- Do not decode arbitrary full TOON with this subset decoder.
- Do not mark tiktoken or Hugging Face tokenization exact unless the selected
  encoding/reference is proven to match the served model.
- Do not activate from the character heuristic.
