---
name: bootstrap
description: "Guidance for deploying a separately installed Botte Secrete runtime into a target project: MCP configuration, directive audit, local configuration and setup report. Use when planning project onboarding. Inspect proposed configuration changes and verify host integration; this catalog does not install services or guarantee savings."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: bootstrap
---
# bootstrap — deploy the toolkit into a project

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

The upstream bootstrap prepares project configuration for a separately installed toolkit. Confirm runtime dependencies and host support, then inspect the resulting configuration and verify the integration before claiming it works.

## Run it

```bash
python -m skills.bootstrap.cli /path/to/project
python -m skills.bootstrap.cli /path/to/project --create-agents-md   # scaffold AGENTS.md if missing
python -m skills.bootstrap.cli /path/to/project --scan-subnet --json
```

## Upstream workflow to verify

1. **Discover local backends** (`llm_backends`) so routing has somewhere to send work.
2. **Wire MCP** — merges the `botte-llm` server into the project's `.mcp.json`
   (the intended merge preserves existing servers; inspect the result). A compatible configured host may expose:
   `auto_route`, `local_chat`, `fusion`, `find_skills`, `audit_local_usage`,
   `route_task`, `discover_backends`, `list_models`.
3. **Audit directives** (`directives_audit`) — reports the CLAUDE.md/AGENTS.md
   health; with `--create-agents-md`, scaffolds a starter `AGENTS.md` when none exists.
4. **Write `.botte/config.json`** — Botte version/baseline commit plus dirty-state evidence, chosen local model, detected cloud keys,
   token budget, routing mode (`auto`).
5. **Write `.botte/setup-report.json`** + print a summary with next steps.

## Result

After setup, verify that the host actually exposes the configured tools and that suitable local backends are reachable. The intended workflow uses local routing for appropriate tasks and configured cloud providers for others; availability, costs and savings require observation in that environment.

`.mcp.json` and `.botte/` hold per-machine absolute paths, so they are gitignored
in this repo — deploy on each machine.

Related: [[llm-mcp]] (the tools wired in), [[auto-router]], [[skill-finder]],
[[directives-audit]], [[llm-backends]].
