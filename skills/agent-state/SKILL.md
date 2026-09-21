---
name: agent-state
description: "Validate and reconcile backend-neutral agent lifecycle state, explicit capability support, and repo-relative mutation scopes. Use before routing, resuming, messaging, or running concurrent mutating agents."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: agent_state
---
# agent-state — explicit authority and capability negotiation

`agent_state` prevents an orchestrator from guessing that every provider can
resume, fork, read transcripts, send messages, switch models, or mutate a
workspace. Every envelope carries a complete capability matrix; undeclared
capabilities become `unknown` and therefore do not satisfy a requirement.

The contract also records backend-neutral lifecycle state, its authority, task
scope, revision, and an optional structured completion result. Authority is
ordered `native > adapter > terminal > unknown`. Write scopes must not overlap
between active agents.

Python API:

```python
from skills.agent_state import build_agent_state, eligible_agents, scope_conflicts

state = build_agent_state(
    agent_id="builder",
    backend="codex",
    task_id="task-1",
    state="working",
    state_source="native",
    scopes=[{"path": "skills/agent_state", "access": "write"}],
    capabilities={"send_message": "native", "mutate_workspace": "native"},
)
```

The lazy MCP tool `agent_state` exposes `create`, `validate`, `reconcile`,
`eligible`, and `conflicts`. It exchanges JSON objects only and uses zero cloud
tokens. The JSON contract is `docs/schemas/agent-state-v1.schema.json`.

`meta_harness` persists queued/working/final observations in each session, and
`conductor.execute` returns the observation history beside every step result.
Both use adapter authority and opaque local identifiers. A successful legacy
subprocess becomes `completed` only when the local Git observer captures stable
before/after revisions, Git-visible changed paths, and a successful exit code.
If Git is unavailable, the snapshot races, or the path limit is exceeded, the
success remains `idle`.

Confirmed writers also acquire an atomic `botte-mutation-lease-v1` in the local
temporary directory. The lease is conservative: one Botte writer per Git root,
including callers launched from different subdirectories. Conflicts become a
`blocked/conflict` state before the command starts. Crash-stale leases are not
silently removed.

Declared mutation scopes can additionally use a bounded filesystem snapshot to
include Git-ignored outputs. The observer allows at most 20 scopes, 1,000 files,
and 64 MiB, never follows symlinks, and never scans `.git`. Exceeding a bound
keeps the result out of `completed`. Any Git-visible change observed outside
every declared scope is reported as a scope violation and prevents completion,
even when the subprocess exits successfully. Enforcement is detection-only:
it never rolls back a dirty worktree.

For explicit scopes, a repository-wide metadata guard also watches every file
outside those scopes, including ignored files. It excludes the allowed trees,
is capped at 20,000 paths, and fails closed on I/O errors or snapshot races.
It detects create, delete, rename, mode, size, and timestamp changes without
hashing the whole repository. A same-size rewrite whose timestamp is deliberately
restored remains a documented residual risk.

Controlled subprocesses use `run_contained_process`. On Windows, the real
command is held behind an inherited event until its bootstrap has joined a Job
Object configured with `KILL_ON_JOB_CLOSE`; descendants cannot outlive the
observation window. On POSIX, a new process group is terminated after the root
exits or times out. Attachment failure prevents the real command from starting.
Each result exposes structured containment evidence.
