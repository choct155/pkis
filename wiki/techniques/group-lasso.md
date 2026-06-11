---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine learning
id: pkis:technique:group-lasso
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- sparsity
- structured regularization
- variable selection
- multi-task learning
title: Group Lasso
understanding: 0
---

## Definition
$$\min_{\mathbf{w}} \text{NLL}(\mathbf{w}) + \lambda \sum_{g=1}^G \|\mathbf{w}_g\|_2$$

Group lasso partitions the weight vector into $G$ groups and penalises the $\ell_2$ norm of each group's sub-vector, encouraging entire groups of coefficients to be simultaneously zero (group sparsity) rather than individual coefficients.

### Why it matters
Many structured models require group-level variable selection: categorical features encoded as one-hot vectors, multi-class weights for a single predictor, neurons in a neural network layer, or features shared across tasks in multi-task learning. Penalising $\|\mathbf{w}_g\|_2$ (not $\|\mathbf{w}_g\|_2^2$, which reduces to ridge) creates a singularity at $\mathbf{w}_g=\mathbf{0}$ analogous to the $\ell_1$ singularity, driving whole groups to zero. The $\ell_\infty$ variant forces the largest-magnitude element to zero, dragging the rest along.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]