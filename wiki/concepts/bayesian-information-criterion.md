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
- model-selection
id: pkis:concept:bayesian-information-criterion
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- model-selection
- information-criterion
- Occam-razor
- marginal-likelihood
- BIC
title: Bayesian Information Criterion (BIC)
understanding: 0
---

## Definition
$$L_{\text{BIC}}(m) = -2\log p(D|\hat{\theta},m) + D_m \log N$$

where $D_m=\dim(\theta_m)$ is the number of free parameters and $N$ is the sample size. Equivalently, the BIC score to maximise is $J_{\text{BIC}}=\log p(D|\hat{\theta},m)-\frac{D_m}{2}\log N$.

**Derivation:** Apply a Laplace (Gaussian) approximation to the log marginal likelihood $\log p(D|m)$; under a uniform prior and assuming the empirical Fisher information is $\approx N\hat{\mathbf{H}}$, the $\frac{1}{2}\log|\mathbf{H}|$ term reduces to $\frac{D_m}{2}\log N$ plus a term independent of $N$.

### Why it matters
BIC provides a tractable proxy for the log marginal likelihood and embodies Bayesian Occam's razor: the penalty $D_m\log N$ grows with both model complexity and sample size, automatically penalising overparameterisation. Unlike AIC (penalty $2D_m$), BIC is consistent — it selects the true model as $N\to\infty$ if it is in the candidate set. BIC, AIC, and MDL share the same two-part NLL + complexity-penalty structure but differ in the penalty coefficient.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]