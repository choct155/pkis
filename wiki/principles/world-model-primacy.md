---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- artificial-intelligence
- cognitive-science
- machine-learning
id: pkis:principle:world-model-primacy
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch01
tags:
- world-model
- intelligence
- model-based
- cognitive-science
- compositionality
title: World-Model Primacy
understanding: 0
---

## Definition
The thesis that *intelligence fundamentally requires an internal model of the world* — a structured, predictive representation of the environment — rather than merely the ability to map stimuli to responses:
$$\text{Intelligence} \supset \text{Pattern Recognition}, \quad \text{Intelligence} \approx \text{World Modelling}.$$

Attributed in spirit to Josh Tenenbaum's 2021 NeurIPS keynote: "Intelligence is not just about pattern recognition and function approximation. It's about modeling the world."

### Why it matters
This principle motivates the entire model-based ML paradigm: without an internal world model, systems cannot reason counterfactually, plan reliably, or generalise to novel situations. It underpins hierarchical predictive processing, model-based RL, and cognitive science accounts of perception and reasoning.

### Contrast with function-approximation view
Pure function-approximation (e.g., deep learning as 'glorified curve fitting') can achieve impressive performance on i.i.d. benchmarks but lacks the compositional, causal, and counterfactual reasoning enabled by explicit world models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]