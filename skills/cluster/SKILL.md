---
name: cluster
description: "Instructions for upstream cluster discovery, configured-backend selection and task delegation. Use to plan work across a trusted homelab or inspect its declared capacity. Verify endpoints, receiver policy and capability before sending tasks; this catalog does not deploy a receiver or guarantee backend availability."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: cluster
---
# cluster — the homelab as one schedulable resource

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

Idle local capacity is recovered cost. Instead of always hitting the same backend
(or the cloud), spread work across every reachable machine.

```bash
python -m skills.cluster.cli status --subnet      # all machines + recommended target
python -m skills.cluster.cli pick --strategy lru  # spread to the idlest machine
python -m skills.cluster.cli pick --strategy latency
python -m skills.cluster.cli delegate node-b.example "restart the model server"
```

## How it routes

- **status** groups discovered backends (LM Studio, Ollama, LocalAI, ComfyUI,
  Qdrant…) by host → the cluster view, with latency and the recommended target.
- **pick `lru`** chooses the *least-recently-used* capable chat backend, so the
  next task lands on an under-used box — work spreads across the cluster.
- **pick `latency`** chooses the most responsive backend.

## Delegation (hand-off only)

`delegate(host, task)` POSTs `{"task": …}` to a machine's agent endpoint
(`BOTTE_AGENT_<host>` env or `--url`). The endpoint host must match `host`;
non-loopback delegation requires HTTPS and a token from
`BOTTE_AGENT_TOKEN_<host>` or `BOTTE_AGENT_TOKEN`. The delegation client hands
off the task; execution authority belongs to the configured receiver. Inspect
that receiver's allowed actions before delegation. If no endpoint is configured,
report the missing prerequisite instead of claiming that the task ran.

> Security: privileged maintenance requires an explicitly configured receiver
> policy. The separately installed upstream HTTP receiver is intended for
> loopback use; LAN exposure requires a trusted HTTPS reverse proxy and
> authentication appropriate to the deployment.


## Reference machine-agent (deploy on each box)

Until your agent (Hermes) exposes an endpoint, inspect and configure the upstream receiver. Its documented boundary is a whitelist of *named* read-only actions
(`ping`, `machine_status`, `disk`, `local_backends`), **never arbitrary shell**,
loopback by default, token-gated for any non-loopback bind. Privileged
maintenance is a separate explicitly configured mode, described below.

```bash
python -m skills.cluster.agent serve --token "$BOTTE_AGENT_TOKEN"
# then from the cluster:
python -m skills.cluster.cli delegate 127.0.0.1 machine_status --url http://127.0.0.1:8799/task
```


### Privileged maintenance (operator-approved, confirm-gated)

To let the cluster trigger real maintenance (restart a model server, pull/update
a model, clear a cache), the **operator** pre-approves a named whitelist on each
machine — the remote caller can only trigger commands **by name** and must pass
`confirm: true`. There is no arbitrary shell from the network.

```bash
# operator, on the machine (example: examples/cluster/maintenance-commands.json)
python -m skills.cluster.agent serve --host 0.0.0.0 --token "$BOTTE_AGENT_TOKEN"        --commands examples/cluster/maintenance-commands.json
# caller: list what's permitted, then run with confirmation
#   {"task":"list_commands"}
#   {"task":{"action":"run","args":{"name":"restart_ollama","confirm":true}}}
```

The documented upstream default without a `--commands` file permits only named read-only actions. Confirm that the installed receiver enforces this boundary and that non-loopback maintenance uses the required authentication and transport configuration.

Exposed via [[llm-mcp]] as `cluster_status`. Related: [[llm-backends]]
(discovery), [[infra-advisor]] (per-machine tips), [[auto-router]].
