---
name: recipes
description: "Observe content-free botte-llm call shapes, review repeated read-only workflows, and run only locally approved declarative recipes."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: recipes
---
# recipes — Verified read-only MCP workflows

Recipes remove repeated LLM orchestration from common `botte-llm` workflows.
They are local declarative data, never generated Python or shell code.

## Safety boundary

- Observation is off by default and covers only calls handled by `botte-llm`.
- Events retain tool names, argument types, verdicts, bounded sizes, timings,
  and fingerprints. They do not retain prompts, argument values, raw results,
  file contents, secrets, identities, or exact paths.
- A candidate requires the same verified sequence in three separate runs.
- Candidates are inert until approved through the CLI.
- V1 permits only the explicit deny-by-default tool registry in
  `tool_policy.py`: read-only, local, no network, no subprocess, no writes.
- Schema, policy, project, or engine drift makes execution fail closed.
- Recipe failure returns control to the caller; it never retries or invokes a
  fallback automatically.

## Enable local observation

Set the environment variable only for the MCP process whose local usage should
be observed:

```powershell
$env:BOTTE_RECIPE_OBSERVE = "1"
python -m skills.llm_mcp.server
```

Project observations are stored in `.botte/recipes/observations-v1.jsonl`.
The file rotates after 2 MiB and keeps the newest half of complete records.
User-approved recipes are stored below
`%LOCALAPPDATA%/BotteSecrete/recipes/`; project overrides remain below
`.botte/recipes/`. Both locations are local and ignored by Git.

## Review lifecycle

```powershell
botte recipes --project C:/project mine --json
botte recipes --project C:/project list --json
botte recipes --project C:/project show <candidate-id> --json
botte recipes --project C:/project approve <candidate-id> --scope user --json
botte recipes --project C:/project reject <candidate-id> --reason not-useful --json
botte recipes --project C:/project disable <recipe-id> --scope user --json
```

Deletion is deliberately explicit:

```powershell
botte recipes --project C:/project delete candidate <candidate-id> --yes --json
botte recipes --project C:/project delete recipe <recipe-id> --scope user --yes --json
botte recipes --project C:/project delete observations --all --yes --json
```

## MCP execution

`recipe_run` is a lazy MCP tool, so its schema is not added to the permanent
tool prefix. It accepts an approved recipe ID, explicit runtime parameters,
project path, and optional `dry_run`. Dry-run validates the complete recipe and
returns only step/tool/argument-field names; it never dispatches a step.

An approved recipe grants no new authority. Each underlying tool must still be
present in the current safe registry and MCP dispatcher.

## V1 exclusions

Third-party MCP interception, network calls, local-model calls, filesystem
writes, subprocesses, installation, deletion outside the recipe store,
publication, semantic matching, automatic approval, automatic retry, and
parallel execution are out of scope.
