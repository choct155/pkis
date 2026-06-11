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
- Bayesian-inference
- machine-learning
id: pkis:technique:bayesian-logistic-regression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
tags:
- Laplace-approximation
- MAP
- posterior-approximation
- predictive-distribution
- probit-Gaussian-convolution
- uncertainty-quantification
title: Bayesian Logistic Regression (Laplace)
understanding: 0
---

## Definition
Bayesian logistic regression approximates the intractable posterior $p(\mathbf{w}|\mathbf{t})\propto p(\mathbf{w})p(\mathbf{t}|\mathbf{w})$ using the Laplace approximation centred at the MAP estimate:

$$q(\mathbf{w}) = \mathcal{N}(\mathbf{w}|\mathbf{w}_{\text{MAP}}, S_N), \quad S_N^{-1} = S_0^{-1} + \sum_n y_n(1-y_n)\boldsymbol{\phi}_n\boldsymbol{\phi}_n^T.$$

Predictive probabilities are obtained by marginalising over $q(\mathbf{w})$. The marginal distribution of $a=\mathbf{w}^T\boldsymbol{\phi}$ is Gaussian with $\mu_a=\mathbf{w}_{\text{MAP}}^T\boldsymbol{\phi}$ and $\sigma_a^2=\boldsymbol{\phi}^T S_N\boldsymbol{\phi}$, giving the approximate predictive class probability

$$p(C_1|\boldsymbol{\phi},\mathbf{t}) \approx \sigma\!\left(\kappa(\sigma_a^2)\mu_a\right), \quad \kappa(\sigma^2) = (1+\pi\sigma^2/8)^{-1/2}.$$

### Why it matters
This framework regularises logistic regression against over-fitting on separable data (where MLE diverges), provides calibrated uncertainty, and enables model comparison via the Laplace evidence approximation. The kappa-shrinkage of the predictive sigmoid quantifies how posterior uncertainty 'softens' the classifier near the decision boundary.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]