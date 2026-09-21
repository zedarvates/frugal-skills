---
name: decision-ladder
description: "Ponytail-inspired YAGNI enforcement — explicit need, existing code, stdlib, native platform, installed dependency, one-liner, then evidence-gated new code."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: decision_ladder
---
# Decision Ladder

Ponytail-inspired YAGNI enforcement for botte-secrete. Before writing ANY code, climb this ladder. Each rung that passes saves the cost of every rung above it.

## The Ladder

1. **not_needed** — Is the requirement explicitly unnecessary?
2. **existing_module** — Does the real codebase already solve it?
3. **stdlib** — Is it in Python's standard library?
4. **native_platform** — Does the browser, OS, database, or protocol provide it?
5. **installed_dependency** — Is an accepted dependency already available?
6. **regex_oneliner** — Does one readable expression suffice without cutting safety?
7. **new_code** — Only after affected files and the real flow were inspected.

## Usage

```python
from skills.decision_ladder.ladder import climb, audit_task_list

# Single task
result = climb("extract function names from a Python file")
# → LadderResult(rung="stdlib", solution="ast module (ast.parse/walk)", saved_lines=15)

# Audit a task list
report = audit_task_list([
    "parse JSON config",
    "design auth middleware",
    "count word frequency in text",
    "strip HTML tags from string",
    "implement custom OR-Tools solver",
])
# → avoidable_pct: 80%, lines_saved: 85
```

## Integration

Add to workflow-check as a pre-code hook. See `hook.py`.

## Metrics

Tracks:
- % of tasks that could be avoided (stdlib, regex, existing module)
- Estimated lines saved per task
- Confidence score per suggestion
