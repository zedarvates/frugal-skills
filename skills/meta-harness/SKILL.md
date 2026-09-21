---
name: meta-harness
description: "Run several skills as one governed pipeline in which every stage executes inside its own sandbox, and nothing is written until an approval gate passes — plan, execute isolated stages, cross-review, then apply with budgets and rollback. Use when the pipeline itself is the object of interest: mechanical isolation between stages, an explicit gate before any write, and a rollback path. Not for the named blue-team pipeline of audit, fix, optimize and consolidate — use mousquetaires; not for a single detector run — use the code detectors directly; not for bounding a retroactive loop and measuring its cost — use loop-optimizer; not for the adversarial challenge alone — use cardinal."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: meta_harness
---
# meta-harness — governed multi-stage orchestration

Un meta-harness qui orchestre les skills Botte (audit, fix, counter-audit, optimize, test)
dans un pipeline gouverné. Chaque étape tourne dans son propre sandbox
(subprocess, workdir isolé). Governance = approval gates + budgets + rollback.

## Concept

```
USER: "audit + fix mon projet"
    │
    ▼
Meta-Harness
    ├── Orchestrator → Plan: [audit] → [review] → [fix] → [test]
    │
    ├── Sandbox 1: Porthos audit (skills/directives_audit)
    ├── Sandbox 2: Rochefort counter-audit (skills/cardinal)
    ├── Sandbox 3: d'Artagnan fix (skills/fix)
    └── Sandbox 4: run tests
    │
    ├── Governance → approval gate avant apply
    │
    └── Report → synthèse multi-agent
```

## Agents disponibles

| Agent | Skill Botte | Rôle |
|-------|-------------|------|
| `porthos` | directives_audit | Audit initial |
| `rochefort` | cardinal | Contre-audit (red team) |
| `d'artagnan` | fix | Correction automatique |
| `aramis` | optimize | Optimisation token |
| `conductor` | conductor | Planification |
| `security` | security_scanner | Scan sécurité |
| `fast_context` | fast_context | Exploration repo |

## Usage

```bash
# Pipeline complet: audit → counter-audit → fix → test
python -m skills.meta_harness.cli run . audit counter-audit fix test

# Voir les pipelines disponibles
python -m skills.meta_harness.cli plans

# Lancement avec approval gate
python -m skills.meta_harness.cli run . audit fix --approval

# Voir l'état d'un pipeline
python -m skills.meta_harness.cli status <session_id>

# Rollback
python -m skills.meta_harness.cli rollback <session_id>
```

## API Python

```python
from skills.meta_harness import MetaHarness, PipelinePlan, Step, Sandbox

# Créer un harness
h = MetaHarness(workdir="/path/to/project")

# Planifier un pipeline
plan = h.plan(["audit", "counter-audit", "fix", "test"])

# Exécuter
session = h.execute(plan, approval=False)

# Voir le rapport
print(session.report())

# État interopérable courant + historique des transitions
print(session.agent_states)
print(session.state_history)
```

Chaque observation suit `botte-agent-state-v1`. Les identifiants sont opaques,
les états viennent de l'adaptateur local, et seul le sandbox actif reçoit une
portée d'écriture déclarée. Un succès devient `completed` seulement si les
captures Git avant/après sont stables; sinon il reste `idle`.
Avant chaque subprocess, un lease atomique sérialise les écritures Botte pour
la racine Git. Un conflit bloque l'étape avant son lancement.
Le sandbox déclaré est aussi photographié directement : ses fichiers ignorés
par Git peuvent donc apparaître dans `completion.changed_paths`. Si une étape
retourne 0 mais qu'une écriture Git-visible sort du sandbox, elle échoue avec
`scope_violations`; le worktree n'est jamais restauré automatiquement.
Une garde metadata bornée couvre aussi les fichiers ignorés hors sandbox. Une
capture initiale incomplète bloque le lancement; une capture finale incomplète
fait échouer l'étape sans produire de preuve de complétion.
Chaque sandbox lance maintenant son processus dans une frontière native et
persiste `process_containment`. Sous Windows, une amorce bloquée garantit que la
commande réelle ne démarre qu'après son rattachement au Job Object.

## Architecture

```
meta_harness/
├── orchestrator.py   — Planification pipeline + dispatch
├── runner.py         — Sandbox subprocess + workdir isolé
├── governance.py     — Garde-fous, budgets, rollback
├── session.py        — Persistance + historique
├── cli.py            — argparse CLI
└── test_meta_harness.py
```
