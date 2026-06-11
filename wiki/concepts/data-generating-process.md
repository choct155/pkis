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
- statistics
- machine-learning
- causal-inference
id: pkis:concept:data-generating-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch01
tags:
- ground-truth-distribution
- generative-model
- distribution-shift
- identifiability
title: Data-Generating Process (DGP)
understanding: 0
---

## Definition
The underlying stochastic mechanism $\mathcal{M}$ that produces observed data $\mathcal{D} = \{x_i\}_{i=1}^n$, formally characterised by a joint distribution $p^*(x)$ (or $p^*(x,y)$ in supervised settings) that the analyst's model attempts to approximate.

The DGP is the latent 'ground truth' whose structure — causal, compositional, or otherwise — a model-based approach explicitly tries to recover, rather than only fit its surface statistics.

### Why it matters
Distinguishing the DGP from the analyst's approximate model is central to understanding generalisation, robustness to distribution shift, and identifiability. Scientific modelling, causal inference, and principled uncertainty quantification all hinge on how faithfully the postulated model captures the true DGP.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]