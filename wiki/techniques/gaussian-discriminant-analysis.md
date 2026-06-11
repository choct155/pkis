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
- statistics
id: pkis:technique:gaussian-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- classification
- generative-model
- gaussian
- quadratic-boundary
- MLE
title: Gaussian Discriminant Analysis (GDA / QDA)
understanding: 0
---

## Definition
$$p(y=c\mid x,\theta) \propto \pi_c\, \mathcal{N}(x\mid \mu_c, \Sigma_c)$$

A generative classifier that places a multivariate Gaussian class-conditional density on the features for each class $c$, with (possibly distinct) mean $\mu_c$ and covariance $\Sigma_c$. When covariances differ across classes the log-posterior is quadratic in $x$, yielding **quadratic decision boundaries** (QDA); when covariances are shared ($\Sigma_c = \Sigma$) the quadratic term cancels, yielding **linear decision boundaries** (LDA).

### Why it matters
GDA provides a principled generative account of linear and quadratic classifiers, directly connecting Gaussian density estimation to the softmax/logistic form of the posterior. The MLEs are closed-form: $\hat{\mu}_c = \bar{x}_c$, $\hat{\Sigma}_c = \text{Sctr}_c / N_c$, $\hat{\pi}_c = N_c/N$.

### Regularisation variants
- **Diagonal LDA**: force $\Sigma_c$ diagonal ($O(CD)$ parameters).
- **Regularised Discriminant Analysis (RDA)**: MAP estimate $\hat{\Sigma}_{\text{map}} = \lambda\,\text{diag}(\hat{\Sigma}_{\text{mle}}) + (1-\lambda)\hat{\Sigma}_{\text{mle}}$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]