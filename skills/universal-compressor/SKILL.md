---
name: universal-compressor
description: "Instructions for the current upstream content compressor: JSON whitespace minification, exact repeated-line summaries, ANSI removal and code passthrough. Optional restoration retains originals in process memory; durable stores and sampling/truncation are not implemented by this API. Measure bytes and fidelity; not model token savings."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: universal_compressor
---
# universal-compressor — conservative upstream content transforms

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Current upstream strategies

| Content type | Current transformation |
|---|---|
| `text` | Collapse repeated blank lines and summarize exact consecutive repeats |
| `json` | Remove whitespace outside strings; retain keys, values and number lexemes |
| `log` | Summarize exact repetition without sampling distinct lines or truncating the tail |
| `tool_output` | Strip ANSI color codes while retaining all lines |
| `code` | Keep the source unchanged |
| `auto` | Choose a type with the installed runtime's detection rules |

These operations do not implement the former sampling, head/tail truncation, comment stripping or import collapsing claims. Inspect the selected strategy and retained data. Summarizing repeats and collapsing blank lines changes text representation; check that the consumer can still answer the task, or keep the original.

## Conditional upstream example

```python
from skills.universal_compressor import compress, restore

result = compress(content, content_type="json", reversible=True)
original = restore(result.reversible_key)
# Compare UTF-8 byte sizes and task fidelity; bytes are not provider token counts.
```

`reversible=True` retains the original in an in-process dictionary, indexed by its content hash. `restore(key)` has no `store_path` parameter in this implementation. Restoration requires that same live process and store entry; a restart loses it. The current API does not implement a durable restoration directory, TTL or size limit. Originals may contain sensitive data, so bound their lifetime and use the upstream `flush_store()` when appropriate. Do not claim durable recovery from a hash alone.

## When NOT to use

- For self-contained encoded transport, consider token-compressor and its TC1 decoder.
- For per-turn verbosity decisions, consider token-shaper.
- For durable governed memory, use an independently verified storage workflow.
