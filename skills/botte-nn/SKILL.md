---
name: botte-nn
description: "Instructions for upstream small-classifier inference, active learning, calibration and dataset review. Use when a routing or effort decision needs a separately trained classifier. Requires compatible model files and Rust or numpy runtime components. Not for tier selection (nn-router), generative calls (llm-backends) or lexical tool selection."
license: MIT
metadata:
  version: "1.0.0"
  domain: agent-skills
  canonical-name: botte_nn
---
# botte-nn — tiny classifier inference and calibration

## Package scope and prerequisites

This catalog ships instructions, not the executable runtime. Python modules, scripts, local services and optional tools named below must be installed separately from the upstream project. Check their availability before running commands; if they are missing, explain the prerequisite instead of claiming execution or results. The host agent may use model tokens while following these instructions.

Commands, APIs and runtime behavior described below are conditional examples for a compatible upstream installation; they are not evidence of execution in this package.

## Purpose

Inférence de classifieurs feedforward minuscules (effort, binary router), avec
le boucle d'apprentissage qui va avec : remontée de verdicts, apprentissage
actif, calibration en température et audit du jeu de données.

Inspect the separately installed runtime's model registry first. Use an
identifier reported by that registry, and report a missing model instead of
assuming that a model file or compiled classifier is available.

    python -m skills.botte_nn.cli list
    python -m skills.botte_nn.cli predict effort_classifier --input 0.5 0.3 0.8 0.1
    python -m skills.botte_nn.cli which --input 0.1 0.2 0.8 0.0

## When NOT to use

- You want a complexity-to-tier decision without a trained model — use nn_router.
- You want a generative model call — use llm_backends.
- You want a tool chosen lexically — use tool_router.
