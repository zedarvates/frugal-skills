---
name: auto-memory
description: "Guidance for upstream memory storage, recall, compression and consolidation, conceptually inspired by Stanford AutoMem. Use to plan a learning-oriented memory workflow; inspect the installed implementation and storage policy before persisting data."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: auto_memory
---
# AutoMemory

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

Memory as a capability, not just storage. Adapts to patterns in agent behavior.

## Features

- **MemoryBank** — persistent key/value store with categories and confidence scores
- **TrajectoryRecorder** — capture goal→actions→outcomes paths
- **Compressor** — deduplicate, bottleneck reduction, pattern extraction
- **Hook** — integrate with context_profiler and control loop

## Usage

```python
from skills.auto_memory import init_memory, store_memory, recall_memory

bank = init_memory()
store_memory("user_pref.format", "concise", category="user_pref", confidence=0.95)
prefs = recall_memory("user_pref.format")
```

## Integration

Add to `control_loop.py`:

```python
from skills.auto_memory.hook import init_memory, record_step, consolidate_memory

bank = init_memory("task_123")
record_step("plan", {"steps": ["a", "b"]})
consolidate_memory()  # merge similar memories
```
