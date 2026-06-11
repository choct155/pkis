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
- bayesian-inference
extends:
- automatic-relevance-determination
id: pkis:concept:rvm-sparsity-quality-factors
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- rvm-evidence-sparsity-result
related_concepts: []
sources:
- bishop-prml-ch07
tags:
- RVM
- sparsity
- Bayesian
- marginal-likelihood
- sequential-algorithm
title: Sparsity and Quality Factors in RVM
understanding: 0
---

## Definition
In the sequential sparse Bayesian learning framework, for each candidate basis vector $\boldsymbol{\varphi}_i$, two scalars are defined:
$$s_i = \boldsymbol{\varphi}_i^T C_{-i}^{-1}\boldsymbol{\varphi}_i, \qquad q_i = \boldsymbol{\varphi}_i^T C_{-i}^{-1}\mathbf{t},$$
where $C_{-i}$ is the covariance matrix with basis function $i$ excluded. The optimal hyperparameter satisfies:
- $q_i^2 > s_i$: basis function is included, with $\alpha_i = s_i^2/(q_i^2 - s_i)$.
- $q_i^2 \leq s_i$: basis function is pruned ($\alpha_i \to \infty$).

$s_i$ measures the overlap of $\boldsymbol{\varphi}_i$ with the remaining model; $q_i$ measures its alignment with the residual.

### Why it matters
These factors provide a closed-form criterion for deciding, at each step of the sequential algorithm, whether a basis function should enter, remain in, or be removed from the model. This reduces RVM training to $O(M^3)$ per step (where $M \ll N$ is the current model size) and gives geometric insight: a basis vector orthogonal to the data residual will always be pruned.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[automatic-relevance-determination]] — extends
- [[rvm-evidence-sparsity-result]] — prerequisite-of
[To be populated during integration]