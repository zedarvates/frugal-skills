---
name: botte-nn
description: "Run inference with tiny feedforward classifiers and maintain their learning loop — predict with one model, classify across all models, list available models, plus active learning, temperature calibration, expected calibration error and dataset auditing; executes through a compiled Rust binary with a numpy fallback. Use when a routing or effort decision should come from a small trained classifier rather than a prompt. Not for the tier decision itself — use nn-router; not for a large language model call — use llm-backends; not for rule-based tool selection — use tool-router."
license: MIT
metadata:
  version: "1.0.0"
  domain: botte-secrete
  canonical-name: botte_nn
---
# botte-nn — tiny classifier inference and calibration

## Purpose

Inférence de classifieurs feedforward minuscules (effort, binary router), avec
le boucle d'apprentissage qui va avec : remontée de verdicts, apprentissage
actif, calibration en température et audit du jeu de données.

    python -m skills.botte_nn.cli list
    python -m skills.botte_nn.cli predict models/effort_classifier.json --input 0.5 0.3 0.8 0.1
    python -m skills.botte_nn.cli which --input 0.1 0.2 0.8 0.0

## When NOT to use

- You want a complexity-to-tier decision without a trained model — use nn_router.
- You want a generative model call — use llm_backends.
- You want a tool chosen lexically — use tool_router.
