---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- Bayesian-inference
- statistics
id: pkis:result:gp-marginal-likelihood
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch18
tags:
- marginal-likelihood
- kernel-learning
- hyperparameter
- model-selection
- GP
title: GP Marginal Likelihood for Kernel Learning
understanding: 0
---

## Definition
For a GP regression model with hyperparameters $\theta$ (kernel parameters and noise variance $\sigma_y^2$), the **log marginal likelihood** is
$$\log p(\mathcal{D}|\theta) = -\frac{1}{2}(y-\boldsymbol{\mu}_X)^T K_\sigma^{-1}(y-\boldsymbol{\mu}_X) - \frac{1}{2}\log|K_\sigma| - \frac{N}{2}\log 2\pi$$
The three terms represent: (1) a data-fit term (Mahalanobis distance), (2) a complexity penalty ($\log|K_\sigma|$, smaller for smoother functions), and (3) a normalisation constant.

Maximizing $\log p(\mathcal{D}|\theta)$ w.r.t. $\theta$ via gradient descent automatically trades off fit against complexity, providing a principled alternative to cross-validation for hyperparameter selection.

### Why it matters
The GP marginal likelihood is an instance of the Occam factor / evidence framework: it penalises overly complex models without held-out data. Gradients w.r.t. $\theta$ can be computed in $O(N^3)$ via the Cholesky decomposition, enabling joint kernel selection and inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]