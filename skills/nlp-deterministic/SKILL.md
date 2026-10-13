---
name: nlp-deterministic
description: "Instructions for upstream rule-based intent classification, regex entity extraction and keyword frequency. The classifier can use hash-derived numeric features without a model; this does not measure the host agent consumption. Not for generative reasoning or learned semantic embeddings."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: nlp_deterministic
---
# nlp-deterministic — classify & extract without a model

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Many "ask the model to classify / extract" calls don't need a model: a rule +
gazetteer and hash-derived numeric features can provide rule-based candidates without invoking a generative model. Evaluate accuracy and actual runtime costs.
This is the NLP half of the determinism program (alongside the combinatorial
solvers): replace LLM reasoning for structured language decisions with exact,
repeatable computation.

```bash
python -m skills.nlp_deterministic.cli classify "speed up my SQL" perf=fast,optimize,slow auth=login,token
python -m skills.nlp_deterministic.cli entities "GET https://x.io from 203.0.113.1 with $TOKEN --json"
python -m skills.nlp_deterministic.cli keywords "cache the cache so queries stay fast"
```

- **classify(text, intents)** — `intents = {label: [keywords]}`. Score = keyword
  recall blended with a local hash-embedding cosine ([[ingest]] embedding +
  [[vector-protocol]] cosine, offline). Returns the best label + per-label scores.
- **extract_entities(text)** — regexes for urls, emails, IPs, file paths, env
  vars (`$VAR`/`%VAR%`), CLI flags (`--flag`), and numbers.
- **keywords(text)** — stopword-filtered (EN+FR) frequency keyphrases.

Exposed via [[llm-mcp]] as `nlp_classify` and `nlp_extract`. Pairs with
[[auto-router]] (effort/intent before routing) and [[skill-finder]]. Deterministic
classification is one candidate routing/triage method. Its result depends on the rules, inputs and installed version; host token usage remains separate.
