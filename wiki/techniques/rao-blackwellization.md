---
aliases: []
also_type: []
applies:
- gibbs-sampler
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
- machine-learning
- Bayesian-inference
extends:
- monte-carlo-integration
id: pkis:technique:rao-blackwellization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch11
tags:
- variance-reduction
- marginalization
- collapsed-sampler
- MC-efficiency
title: Rao-Blackwellization
understanding: 0
uses:
- law-of-total-variance
- marginalization
---

## Definition
Replace the naive MC estimator $\hat{f}_{MC}=\frac{1}{S}\sum_s f(X_s,Y_s)$ with the Rao-Blackwellized estimator
$$\hat{f}_{RB} = \frac{1}{S}\sum_{s=1}^S E[f(X,Y)\mid X=X_s], \quad X_s\sim p(X)$$

whenever the conditional expectation over $Y$ is analytically tractable.

### Why it matters
By the law of total variance, $V[E[f(X,Y)|X]] \leq V[f(X,Y)]$, so the RB estimator always has variance no greater than the naive estimator and is still unbiased. It effectively reduces the sampling to a lower-dimensional space. The same principle underlies collapsed Gibbs sampling, where some variables are analytically marginalized to improve mixing and reduce variance.

### Relationship to Rao-Blackwell theorem
This is a direct application of the Rao-Blackwell theorem from statistical decision theory: conditioning on a sufficient statistic (or any function) cannot increase the MSE of an unbiased estimator.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gibbs-sampler]] — applies: Collapsed Gibbs uses Rao-Blackwellization to reduce variance
- [[marginalization]] — uses
- [[monte-carlo-integration]] — extends
- [[law-of-total-variance]] — uses
[To be populated during integration]