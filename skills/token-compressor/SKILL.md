---
name: token-compressor
description: "Instructions for the upstream TokenCompressor reversible TC1 codec: zlib compression of UTF-8 text with base85 encoding. All current level names use the same codec; historical hashing, pruning and schema strategies are not used by compress(). Not for direct model-readable content compaction."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: token_compressor
---
# token-compressor — reversible upstream text codec

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

## Current upstream behavior

The current `TokenCompressor.compress()` in `skills.token_compressor.cli` compresses UTF-8 bytes with zlib and base85-encodes them under a `TC1:` prefix. `expand()` decodes that self-contained payload. All accepted level names currently select this same codec; the old semantic hashing, byte-pair pruning, JSON-schema and n-gram transformations are not invoked by `compress()`.

The encoded result requires a compatible decoder. It is not a smaller model-readable prompt, and fewer bytes do not establish fewer model tokens. Encoding overhead can increase the size of small inputs. Verify the round-trip and measured sizes before choosing this transport.

## Conditional upstream example

```python
from skills.token_compressor.cli import TokenCompressor

codec = TokenCompressor()
original = 'Keep every value, including whitespace and Unicode.'
encoded = codec.compress(original)
assert codec.expand(encoded) == original
```

Inspect CLI help before using its command output as a payload: the CLI also prints measurement lines, so do not pass the entire mixed stdout to a decoder as though it were only TC1 data.

## When NOT to use

- For content a model must read directly, use ordinary text or a verified content-type transform.
- For per-turn output policy, consider token-shaper.
- For an inter-agent message contract, consider agent-compression.
