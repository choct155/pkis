---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- probabilistic-graphical-models
id: pkis:concept:spurious-modes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
tags:
- generative-models
- undirected-models
- mode-coverage
- energy-based-models
title: Spurious Modes in Generative Models
understanding: 0
---

## Definition
**Spurious modes** are regions of high probability under the model distribution $p_{\text{model}}$ that have low probability under the true data distribution $p_{\text{data}}$. They arise when the model's negative phase fails to suppress model probability mass in regions not covered by training data.

### Why it matters
Spurious modes are the canonical failure mode of Contrastive Divergence (CD): because CD initializes chains at data points, the short Markov chains cannot reach model modes far from training examples, so these modes never receive negative-phase gradient to push their probability down. In contrast, Persistent Contrastive Divergence (SML/PCD) allows chains to explore widely and suppress spurious modes. Spurious modes reduce the quality of model samples and inflate probability estimates for non-data regions, degrading downstream tasks like density estimation and generation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]