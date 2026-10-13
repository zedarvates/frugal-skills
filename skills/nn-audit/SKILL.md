---
name: nn-audit
description: "Instructions for reviewing the upstream micro-model audit's heuristic labels. Training-script keywords, metadata fields and test-text matches are inspection clues, not verified provenance or measured accuracy. Inspect the underlying data and real assertions before treating a grounded label as evidence."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: nn_audit
---
# nn-audit — grounded NNs, or synthetic copies of rules?

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Review whether a learned component provides useful evidence or merely approximates
hand-coded labels. Compare it with the rule on representative tasks, cost and
errors rather than assuming either implementation is always better. The upstream
audit uses source-text heuristics; it does not establish which models are accurate
or trained on verified real-world data.

```bash
python -m skills.nn_audit.cli                 # audit skills/botte_nn
python -m skills.nn_audit.cli <dir> --json
```

Per model it reports:
- **data_source** — `real` | `synthetic` | `unknown`, inferred from training-script
  keywords (such as distill/corpus/labelled or `np.random`). This heuristic is not
  proof of the actual dataset, labels, licence or collection provenance.
- **wired** — does any *production* file (not tests/training/registry) consume it,
  and which (`usage`)? Tells **synthetic-but-driving-behaviour** (real risk) apart
  from **synthetic-but-orphan** (dead weight).
- **has_provenance** — whether metadata records `trained_on` / `eval_accuracy` /
  `data`; field presence does not validate the records or reported accuracy.
- **has_test_guard** — the current heuristic finds a model name and `==` in test
  text. It does not demonstrate a model-output assertion or a passed real-world
  test. Inspect and run the relevant assertion before claiming test coverage.
- **verdict** — `grounded` | `synthetic — drives behaviour: ground it` |
  `synthetic + orphan: delete or wire` | `unknown`; these are heuristic review
  labels, not validation results. **`at_risk` = synthetic AND wired** is likewise
  an inspection flag, not proof of a vulnerability or measured model failure.

Use the labels to prioritize a manual review of actual training data, integration
and held-out evaluation. A `grounded` label does not establish provenance or
accuracy. Do not delete, connect or deploy a model solely because of a label.
Exposed via [[llm-mcp]] as `nn_audit`; pairs with [[botte-nn]].
The upstream audit uses file inspection; require the model files and provenance evidence before reporting results.
