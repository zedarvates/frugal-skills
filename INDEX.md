# Skill catalog

115 skills, generated from the canonical tree. Do not edit here — edit the source skill and regenerate.

## Context and budget

- **context-budget** — Pick the optimal set of skills/docs to load for a task under a token budget — an exact 0/1 knapsack (maximize relevance while summed token cost stays under budget), not an LLM 'dec
- **context-profiler** — Measure a project's always-on prefix (agent directives + core rules + MCP tool schemas + skill catalogue) in tokens and as a % of small local-model windows (64k/128k/256k), with a 
- **context-slicer** — Split one body of context into independent typed slices (code, doc, config, log, result, meta) by markdown headings and section markers, each with a token count, a priority and the
- **context-windows** — Persistent context windows for feedback loops — register a window per loop step, then load only the deltas or a merged window instead of resending the whole context on every turn (
- **fast-context** — Deterministic repository exploration that separates context gathering from reasoning — turn an exploration request into targeted READ, GLOB and GREP operations and return a compact
- **prefix-pruner** — Prune context sections the agent never actually uses — a prefix tree plus usage tracking, with three strategies (auto, aggressive drops anything below 0.3 usefulness, conservative 
- **prefix-tree** — Registry of each agent's stable prompt prefix in one compressed trie, so feedback loops and multi-agent exchanges send only the diff instead of the full prompt (register, diff, com
- **vision-budget** — Deterministic preflight for local full-frame versus ROI visual-token budgets, evidence coverage, verifier fallback, privacy, and cache separation.

## Compression

- **agent-compression** — Compress inter-agent messages into a binary wire format — 4-bit quantized vectors, a shared token dictionary learned from a corpus, delta-diff between an old and a new message, and
- **context-compressor** — Compress a large log file before an agent reads it — collapse numeric, timestamp and UUID noise into patterns, count repetitions, keep the top patterns and a sample of unique lines
- **diff-language** — A compact, agent-native notation for describing code changes and findings, with severity markers and operation markers in one line, lossless round-trip parsing and serialization, a
- **structured-output** — Compact LLM-facing JSON and optionally emit round-trip-verified TOON for beneficial tabular data.
- **token-compressor** — Compress the token structure itself, not the content — semantic hashing of repeated patterns, byte-pair pruning, repeated-JSON-schema compression and n-gram dedup, backed by a lear
- **token-shaper** — Decide the per-turn shaping policy for a query and an agent profile — compression level, compression ratio, output token target and verbosity steer — so the effort matches the task
- **ultra-compact** — Compact JSON report wire format for agent-facing reports — three levels: single-char keys (about -30 percent versus compact JSON), keyless array format, and delta-only patches for 
- **universal-compressor** — Compress content by type — text, JSON, logs, tool output and code — through dedup, truncation and pattern sampling, with 40 to 90 percent typical savings, reversible in memory or t

## Routing and skills

- **auto-router** — Auto-decide whether a task runs on a LOCAL model or a CLOUD model (DeepSeek, GLM, Nemotron, Grok, Gemma, …) from an automatic effort estimate, and run multi-model fusion (cascade, 
- **cluster** — Treat the homelab/micro-cluster as one schedulable resource — discover every reachable machine and spread cheap work across them (least-recently-used first) so idle boxes get the n
- **conductor** — Route a high-level goal to an ordered, local-first plan of capabilities — the generalised router — and optionally EXECUTE the plan's read-only steps
- **loader** — Assemble the context a delegated sub-agent needs — the shared core agent file plus the agent's own delta — with single and batch loading and a helper that suggests which agents fit
- **local-router** — Route a task to a local model when the hardware can serve it — a task-type taxonomy (simple text, complex reasoning, vision classify/detect/OCR, speech to text, text to speech, ima
- **nn-router** — Estimate a task's complexity and route it to the right model tier, with batch routing and routing statistics (route, batch_route, routing_stats, estimate_complexity)
- **skill-finder** — Find which skills, tools or MCP are relevant to a task by searching SKILL.md files locally — zero cloud tokens (lexical/fuzzy match, optional local-LLM rerank)
- **skill-project-optimizer** — Build a standing per-project skill profile — scan the available skills, profile what a given project actually needs, and emit a .skills-profile splitting skills into always, condit
- **tiered-router** — Five-level model selection with cost estimation and automatic downgrade — a free level served by local accelerators and pure computation, a local model level, then cheap, standard 
- **tool-router** — Local-first tool routing primitives — tool specifications, a lexical router, a route validator, an evaluation harness with seed cases and a gate that activates a heavier router onl

## Code audit

- **agent-overlap** — Policy A9 detector (docs/local-analysis-policy.md) — finds redundant concurrent agent missions with >=70% objective overlap in event logs (.botte/events.jsonl)
- **code-complexity** — Policy A1 detector (docs/local-analysis-policy.md) — finds over-complex (cyclomatic > 10) and over-long (> 50 AST statements) functions via pure stdlib ast parsing
- **code-duplication** — Policy A6 detector (docs/local-analysis-policy.md) — finds duplicated function bodies and near-duplicate functions across a tree, exactly and semantically (same AST shape with rena
- **code-fingerprint** — Hash every function, method, class and module (SHA-256 over normalized source) so a re-analysis only touches what actually changed, with a persistent cache under .botte-cache/finge
- **code-state** — Policy A2 detector (docs/local-analysis-policy.md) — finds mutable module-level state (dict/list/set assignments) and circular imports via a static AST import graph
- **code-wrappers** — Policy A3 detector (docs/local-analysis-policy.md) — finds passthrough functions whose body is exactly return f(*args, **kwargs) (or 1:1 argument forwarding) with no transformation
- **completion-proof** — Policy A11 detector (docs/local-analysis-policy.md) — finds reports that claim done/complete/termine/fixed without an associated proof (test_id OR cmd_output_ref OR artifact_hash O
- **directives-audit** — Audit a project's AI-agent guidance files — CLAUDE.md, AGENTS.md, .cursorrules, copilot-instructions.md, GEMINI.md, intent docs and specs, in markdown, text or HTML
- **fallow** — Static analysis for JS/TS codebases through the external Fallow CLI — health score with hotspots, dead code, semantic duplication, circular dependencies, PR risk from a diff, and J
- **fallow-like** — A bundle of nine local static analyzers — dead code, duplication, complexity, secrets, taint and data-flow security, boundaries, feature flags, hot paths and blast radius — with a 
- **prompt-repetition** — Policy A8 detector (docs/local-analysis-policy.md) — finds repeated prompts and system contexts (>500 tokens, repeated >=3 times) in event logs (.botte/events.jsonl)
- **repeated-attempts** — Policy A10 detector (docs/local-analysis-policy.md) — finds identical failed retries in local event logs (same action + same error + same fingerprints, no intermediate context chan
- **security-scanner** — Scan Python skills and MCP servers for malicious code — dangerous imports, network exfiltration, filesystem abuse, subprocess injection, obfuscation, crypto weakness, environment l
- **single-impl** — Policy A4 detector (docs/local-analysis-policy.md) — finds ABC, Protocol, and abstract base classes with exactly one concrete implementation across the repository

## Memory and learning

- **agent-intel** — The cross-cutting learning layer — record a retroactive loop for distillation, select the skills a task needs (skill RAG), predict the cost of a fix, compress accumulated agent mem
- **auto-distill** — Distillation automatique cloud → micro-NN.
- **auto-memory** — Memory as a learnable skill — store, recall, compress, and consolidate agent memories
- **botte-learn** — Analyse recorded sessions for recurring failure patterns and turn them into correction rules that can be applied back, with a status view (scan, apply, status)
- **hermes-second-brain** — A compounding knowledge layer for sessions — a goal layer, a retrieved knowledge layer and a history layer filter every response, and a harvest step writes the session's learnings 
- **hermes-bridge** — Expose auto_route/local_chat/fusion/find_skills/infra_tips to Hermes-Agent (or any framework that expects OpenAI-function-calling tool specs instead of MCP) — plus a one-call MCP c
- **ingest** — Local-first web scraping and source ingestion — fetch a URL, extract clean text locally (0 cloud tokens), optionally structure it with a local model, and store it in a Qdrant colle
- **memory-hub** — The governed agent memory store — searchable entries with context bundles and an explicit propose, promote and forget lifecycle, typed assets, sensitivity levels and visibility, ex

## Caching

- **agent-cache** — Skip an agent run whose result can be predicted instead of executing it again — three matching strategies: exact hash (same input, same output), code fingerprint (unchanged code, u
- **cache** — Cache a project's scan result so the first agent scans and the following agents read the cache instead — get_or_scan, a separate audit report slot, a .botte-cache store and a 24 ho
- **response-cache** — Cache model responses so a repeated or similar query does not pay for a full call again — an exact hash check first, then semantic similarity through the local vector service, then

## Agents and orchestration

- **agent-state** — Validate and reconcile backend-neutral agent lifecycle state, explicit capability support, and repo-relative mutation scopes
- **cardinal** — Adversarial red team that challenges the blue team's output — a counter-auditor, a counter-developer and a counter-optimizer run in parallel and an orchestrator issues the verdict,
- **control-loop** — Close the system into a self-improving loop — measure routing outcomes (local %, token savings, escalation/success rates) and adapt the effort→tier thresholds the auto-router reads
- **harness-delta** — Vérification différentielle — ne vérifie que les sections modifiées.
- **local-harness** — Five-layer anti-hallucination harness (gate, constrain, ground, verify, decide) for local small models
- **loop-optimizer** — Orchestrate a retroactive loop with token economy — a controller that picks the next loop action from extracted features, tracks progress state and stop reasons, and can replay a b
- **meta-harness** — Run several skills as one governed pipeline in which every stage executes inside its own sandbox, and nothing is written until an approval gate passes — plan, execute isolated stag
- **monte-cristo** — Independent strategic outsider above the blue and red teams
- **mousquetaires** — The blue team pipeline — audit, fix, optimize, consolidate — with an auditor agent, a developer agent, an optimizer agent and an orchestrator, exposed as a CLI over a project
- **pipeline-integrator** — Integration, monitoring and meta-optimisation across the module set — health check, module heal, agent sync, budget optimisation, module registration and an integration report (hea
- **trajectory** — Trajectory Learning for Botte Secrète — stores solver trajectories and searches similar past optimizations to inform future decisions
- **vector-protocol** — An inter-agent protocol where agents exchange quantized embedding vectors rather than text — each agent operates on low-dimensional vectors pushed to the local vector store and onl

## Local and edge inference

- **botte-nn** — Run inference with tiny feedforward classifiers and maintain their learning loop — predict with one model, classify across all models, list available models, plus active learning, 
- **comfyui** — Local image generation through the ComfyUI HTTP API — queue a workflow, set the prompt node, read system stats and available models, with reusable workflow templates for text-to-im
- **hailo-vision** — Edge vision inference on the Hailo-8 accelerator — object detection, image classification and OCR through compiled .hef models, with the available model table, the Python API (dete
- **llm-backends** — Discover, audit and use local LLM servers (LM Studio, Ollama, LocalAI, vLLM, llama.cpp) on this machine or the network to offload work from the cloud and save tokens
- **llm-mcp** — MCP server that lets Claude Code (or any MCP client) discover and call local LLM servers (LM Studio, Ollama, …) as tools, to offload cheap tasks off the cloud
- **mcp-gateway** — MCP Gateway — expose toutes les skills Botte comme outils MCP
- **media-loader** — Extract text from media before any model sees it — video keyframes through the local vision accelerator, audio through local speech to text, image detection/classification/OCR, and

## Prompt and output

- **ambient-hud** — Show the scoped ambient-status-v1 metrics in a local, top-center Windows overlay
- **docgen** — Generate documentation with a local model drafting and the cloud only refining (0 cloud tokens for the draft), plus a local session review that summarises what a work session did
- **docs-steward** — Scoped documentation map for multi-component projects (server + client + tools + …)
- **prompt-improver** — Rewrite a rough prompt into a professional, structured prompt (role, context, task, instructions, constraints, output format, success criteria) using a LOCAL model — 0 cloud tokens
- **report** — Persist any audit as a timestamped Markdown and/or HTML file (name + date + time) under .botte/reports/, browsable at any time, and list saved reports
- **statusline** — One-line summary of the belt's session activity (tokens saved, cache hits, local/cloud split, escalations) for a terminal statusline — Claude Code's statusLine hook, tmux, or any s

## Operations and evidence

- **app-test** — Local-first GUI/app testing by image matching (SikuliX) — turn a small JSON spec referencing your button images into a runnable SikuliX script and run it locally, using a vision NP
- **bench** — Reproducible token/cost benchmark — runs a fixed task corpus through the real auto-router decision logic and compares it against a 'no routing, everything to cloud STANDARD' baseli
- **checkup** — Run the canonical, already-optimal project checkup in one command — policy presence, directives health, per-component metrics, infra tips, duplication, recurring Markdown review, W
- **cost-estimator** — Estimate what a task or a fix will cost — tokens, model/tier, money ($), and wall-time — using the tiered cost model
- **dashboard** — Generate one self-contained, timestamped HTML dashboard of the system's cost picture — routing savings (control loop), metric trends, current metrics, and the cost of outstanding f
- **efficiency** — Measure tokens, cloud calls, money, latency and local energy per verified task without storing task content.
- **events** — Append-only JSONL decision log (.botte/events.jsonl) that every filter in the belt writes to — routing, cache hits, escalations, micro-NN outputs
- **fleet** — Aggregate status across the fleet, sortable by project tokens saved, lines of code or number of fixes — a read-only view over the canonical fleet registry that the dashboard writes
- **harvest** — Build a bounded, read-only manifest of explicitly selected local repositories and dispersed Botte deployments before comparing or migrating fixes.
- **infra-advisor** — Audit the local cluster's hardware/software/MCP setup and recommend changes that cut token cost — GPU upgrades, Hailo NPU for vision, moving the inference node to Linux, running Qd
- **metrics** — Cost-focused project metrics, broken down per component — LOC by language and component, duplicate-function groups, directive health, always-on context cost (CLAUDE.md tokens × tur
- **plugins** — Install cross-agent MCP plugins into supported coding agents through one installer with a declared list of supported tools, so several agents get the same server without per-agent 
- **preflight** — Make the token-saving optimizations automatic instead of opt-in — a committed project policy plus a UserPromptSubmit hook that injects the prefer-local rules and suggested skills o
- **rtk** — Compact command output before it reaches the model — prefix a shell command with the wrapper and it returns a filtered, smaller form (test failures only, build errors grouped, comp
- **sbom** — Lightweight SBOM scanner for Python/Rust/Node dependencies
- **self-budget** — Agents autobudgétaires — gèrent leur propre budget token.
- **subscription-saver** — Fail-closed evidence and planning contracts for self-hosting decisions — a validated catalogue with digest, capability coverage evaluation, inventory import and export, upstream so
- **upstream-audit** — Track the reviewed Ponytail and RTK baselines, local RTK version, documentation drift, and optional remote Git changes.
- **webhooks** — Minimal HTTP endpoint that exposes the router to no-code workflows — a POST route that takes a prompt and a task type and returns the routing decision as JSON, on a configurable po

## Standards and knowledge

- **code-rules** — Token-efficient coding standards — the three taxes to weigh before adding any dependency (latency, security surface, cold start), stdlib-first choices, flat architecture, data-orie
- **dynamic-workflows** — Orchestration patterns for efficient agents — classify and act, fan out and synthesize, adversarial verification, generate and filter, tournament — each addressing one of three fai
- **simplify-code** — A three-reviewer parallel pass over a diff — one reviewer on code reuse, one on quality, one on efficiency, each receiving the whole diff and required to cite file:line evidence — 

## Utilities

- **bootstrap** — Deploy Botte Secrète's token-saving stack into a target project — wire the botte-llm MCP server into .mcp.json, audit the project's agent directives, and write a .botte config + se
- **call-chains** — Policy A5 detector (docs/local-analysis-policy.md) — finds intra-module passthrough adapter chains of depth > 5 where every link forwards arguments without transformation
- **demo** — Live ANSI dashboard of the belt's decisions — routing, token savings, micro-NN outputs, escalations, cache hits — either a built-in scripted scenario (no LLM, no network, works on 
- **fix** — List a project's correctable issues — confirmed dead code, duplication, stale directive references — each with a tokens·model·money·time cost estimate and a total
- **nlp-deterministic** — Classify and extract from text WITHOUT an LLM — intent classification (lexical overlap + local embedding), entity extraction (regex/gazetteers for urls/emails/ips/paths/env vars/fl
- **recipes** — Observe content-free botte-llm call shapes, review repeated read-only workflows, and run only locally approved declarative recipes.
- **solvers** — Deterministic combinatorial solvers in stdlib — balance work across workers/backends (assignment, LPT), pack items under a capacity (bin-packing, FFD), and order plan steps under d
- **trends** — Track a project's audit metrics over time (directive score, duplication, LOC, always-on cost, fix count, recurring Markdown review state) and show the change since the previous run

## Other

- **audit-dag**
- **botte-proxy**
- **botte-wrap**
- **capabilities**
- **clarification**
- **dag-optimizer**
- **decision-ladder**
- **nn-audit**
- **session-handoff**
