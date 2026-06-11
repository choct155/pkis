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
- machine-learning
- regularisation
id: pkis:technique:soft-weight-sharing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
tags:
- regularisation
- mixture-model
- weight-decay
- sparsity
title: Soft Weight Sharing
understanding: 0
---

## Definition
A regularisation scheme (Nowlan & Hinton 1992) that encourages network weights to cluster into groups by placing a Gaussian mixture prior on each weight independently:
$$p(\mathbf{w}) = \prod_i \sum_{j=1}^{M}\pi_j\,\mathcal{N}(w_i\mid\mu_j,\sigma_j^2).$$
The regulariser is $\Omega(\mathbf{w}) = -\sum_i\ln\sum_j\pi_j\mathcal{N}(w_i|\mu_j,\sigma_j^2)$, and the total loss $\tilde{E}=E+\lambda\Omega$ is minimised jointly over weights $w_i$ and mixture parameters $(\pi_j,\mu_j,\sigma_j)$.

Gradients use posterior responsibilities $\gamma_j(w_i)$, which pull each weight toward the centre of its most probable cluster. Mixing proportions are parameterised via softmax; variances via exp to enforce positivity.

### Why it matters
Generalises hard weight-tying (as in convolutional networks) to any architecture without requiring prior knowledge of the grouping structure. It automatically discovers weight clusters during training, providing a principled alternative to weight decay that can capture multi-scale structure in the parameter space.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]