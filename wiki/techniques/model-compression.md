---
aliases: []
also_type: []
applies:
- neural-networks
- overfitting-and-underfitting
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- dropout
- bayesian-model-averaging
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- model-efficiency
extends:
- ensemble-learning
id: pkis:technique:model-compression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
tags:
- inference
- distillation
- efficiency
- ensemble
- neural-networks
title: Model Compression (Knowledge Distillation)
understanding: 0
uses:
- regularization
---

## Definition
Given a large, expensive model (or ensemble) $f(\mathbf{x})$ and a smaller target architecture, model compression trains the small model to mimic $f$ by minimising a loss between the small model's outputs and $f$'s outputs on a synthetic or real dataset:
$$\mathcal{L}_{\text{compress}} = \mathbb{E}_{\mathbf{x} \sim q(\mathbf{x})}\left[\ell\bigl(f_\text{small}(\mathbf{x}),\, f(\mathbf{x})\bigr)\right].$$
Because the large model has already distilled training-set information into a smooth function, the small model can learn from infinitely many synthetic $\mathbf{x}$ samples, exploiting the 'soft' output distribution (including probabilities assigned to incorrect classes) as a richer supervision signal than hard labels.

### Why it matters
Enables deployment of large, accurate models on resource-constrained devices (phones, embedded systems) by separating the high-cost *training* regime from the low-cost *inference* regime; the soft-target variant (Hinton et al., 2014) shows that incorrect-class probabilities carry transferable structural information about the learned function.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-model-averaging]] — contrasts-with
- [[overfitting-and-underfitting]] — applies
- [[dropout]] — contrasts-with
- [[regularization]] — uses
- [[ensemble-learning]] — extends
- [[neural-networks]] — applies
[To be populated during integration]