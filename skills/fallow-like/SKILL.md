---
name: fallow-like
description: "Instructions for the upstream workflow: A bundle of nine local static analyzers — dead code, duplication, complexity, secrets, taint and data-flow security, boundaries, feature flags, hot paths and blast radius — with a health score and grade and compact JSON, SARIF or markdown output. Use for the broad, one-pass view of a codebase. Not for the five-field policy findings of A1, A2, A3 and A6 — use code-complexity, code-duplication, code-state and code-wrappers; not for the JS/TS external analyser — use fallow."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: fallow_like
---
# Fallow-Like Static Analyzers

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## When NOT to use

- You need the repo policy findings with their five mandatory fields — use the
  code_* detectors (A1, A2, A3, A6).
- The tree is JS/TS and the external analyser is available — use fallow.
9 code analyzers: dead code, duplication, complexity, secrets, **taint (data-flow security)**, boundaries, feature flags, hot paths, blast radius.

**Trigger:** Code audit, quality/security checks, pre-commit analysis.

**Analyzers:**
- DeadCodeAnalyzer, DuplicationAnalyzer, ComplexityAnalyzer
- SecretsAnalyzer, **TaintAnalyzer**, BoundaryAnalyzer, FeatureFlagAnalyzer
- HotPathAnalyzer, BlastRadiusAnalyzer

**Module:** `skills/fallow_like`
**Health:** `calculate_health()` → score 0-100 + grade A-F
**Output:** JSON (compact), SARIF, or markdown (verbose)

## Taint / data-flow security (neuro-symbolic, local-first)

Inspired by RepoAudit/DeepAudit, in botte's local-first shape:

- **symbolic analysis** — Python `ast` traces attacker-controlled *sources*
  (`sys.argv`, `os.environ`/`getenv`, `input`, framework `request.*`) into
  dangerous *sinks* (`subprocess`/`os.system`/`eval`/`exec`, SQL `execute`,
  `pickle`/`yaml.load`/`marshal`, `urlopen`/`requests`) and flags
  insecure-by-default calls (`shell=True` + dynamic, `yaml.load` without a safe
  Loader). Each finding is **CWE-tagged** (78/89/94/502/918). No compilation.
- **optional model-assisted analysis** — `--judge` asks a LOCAL model to confirm
  each candidate (exploitable vs sanitized); it only annotates/adjusts confidence.

```bash
python -m skills.fallow_like.cli taint .            # data-flow security scan
python -m skills.fallow_like.cli taint . --judge    # + local-model confirmation
```

Exposed via [[llm-mcp]] as `security_scan`. v1 does intra-procedural data flow
for Python (botte's primary language); other languages are the next iteration.
