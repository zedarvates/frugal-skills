---
name: skill-finder
description: "Find which skills, tools or MCP are relevant to a task by searching SKILL.md files locally — zero cloud tokens (lexical/fuzzy match, optional local-LLM rerank). This is the declared entry point for skill routing in this repository — use it first whenever a request could be served by more than one skill, and consult its cluster arbitration table before loading a neighbour. Use when you need to pick tools for a project or task and want to avoid spending a paid cloud model on the search step, when the user mentions skill search or tool selection, or when several local skills look interchangeable. Not for building a standing per-project skill profile — use skill-project-optimizer; not for choosing a subset under an explicit token budget — use context-budget."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: skill_finder
---
# skill-finder — local, zero-token skill & tool search

## Cluster arbitration — when two local skills look interchangeable

This table is authoritative for the clusters below. Load the named skill, not
its neighbour, and treat the listed skill as out of scope for the other cases.

| Cluster | Use | Not for |
|---|---|---|
| compression | token_compressor for repeated token structure; universal_compressor for content types (text, JSON, logs, tool output, code); agent_compression for inter-agent wire format; ultra_compact for report JSON; token_shaper to choose the per-turn policy | any of these for deciding which skill to load |
| context | context_budget to allocate under a token budget; context_profiler to measure the prefix; context_slicer to split into typed slices; context_windows to carry loop deltas | prefix_pruner or prefix_tree for the same jobs |
| code audits | code_complexity (A1); code_duplication (A6); code_state (A2); code_wrappers (A3); code_fingerprint as the skip gate in front of them | code_fingerprint for findings — it only decides what to re-run |
| prompt | prompt_improver to rewrite a prompt; prompt_repetition (A8) to find wasted repeated prefixes | prompt_repetition for rewriting |
| prefix | prefix_pruner to delete never-used sections; prefix_tree to keep per-agent prefixes and diff | context_windows when the reuse unit is a loop step |
| skills | skill_finder for one query; skill_project_optimizer for a standing per-project profile | either for deleting dead context sections |
| cache | cache for a project scan reused by later agents; response_cache for a model answer keyed by question; agent-cache for a predictable agent run | code_fingerprint for the same job — it only skips unchanged files inside one audit |
| model routing | tiered_router for the 5-level cost ladder with auto-downgrade; nn_router for the complexity-driven tier; local_router for placing a task on local hardware by type | any of the three for choosing a tool — use tool_router |
| inter-agent transport | vector_protocol for embedding exchange inside a fixed pipeline; agent_compression for a binary message format with deltas | either for durable memory — use memory_hub |
| audit | code_complexity, code_duplication, code_state, code_wrappers for the five-field policy findings; fallow_like for the broad 9-analyzer pass; fallow for JS/TS | mousquetaires for producing the work, cardinal for attacking it |
| output style | caveman for telegraphic output levels; diff_language for change and finding notation; ultra_compact for report JSON | token_shaper for the per-turn policy decision |

Before adding a skill to a cluster, check that no listed member already covers
the same trigger; if one does, extend that skill or its bounds instead.

Picking the right skill/tool for a task is **retrieval, not reasoning** — so it
should not cost paid cloud tokens. This module does the search locally and leaves
the cloud model free for the actual work.

## Two tiers

- **Tier 0 — free (0 tokens total):** lexical + fuzzy match over each skill's
  name, description, tags, triggers and full SKILL.md body. Deterministic.
- **Tier 1 — local (0 cloud tokens):** for ambiguous queries, a local model
  (via [[llm-backends]]) re-ranks the shortlist. Still no cloud spend.

## Use it

```bash
python -m skills.skill_finder.cli "optimize slow postgres queries"
python -m skills.skill_finder.cli "set up an A/B test" --local      # local-LLM rerank
python -m skills.skill_finder.cli "audit dead code" --roots ~/.claude/skills --json
```

```python
from skills.skill_finder import find
r = find("decide local vs cloud routing", top_k=5)
r["cloud_tokens"]   # 0
r["matches"]        # [{name, score, why, description, path, tokens_est}, …]
```

`--roots` points at any directory tree containing `SKILL.md` files (your global
skill library, a project's skills, etc.); defaults to this repo's `skills/`.
Works whether or not a SKILL.md has YAML frontmatter — the body is always indexed.

## Why it saves money

A coding agent normally burns expensive context having the cloud model read every
skill description to decide what to load. `find_skills` returns a ranked shortlist
for **0 cloud tokens**, so the cloud model only sees the few skills that matter —
or none, when the local rerank is decisive.

Exposed via [[llm-mcp]] as the `find_skills` tool. Related:
`skill_project_optimizer` (rule-based per-project filtering), `auto_router`.
