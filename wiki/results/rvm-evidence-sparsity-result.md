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
- bayesian-inference
id: pkis:result:rvm-evidence-sparsity-result
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
tags:
- RVM
- sparsity
- evidence-approximation
- ARD
- closed-form
title: RVM Evidence Optimisation and Sparsity Theorem
understanding: 0
---

## Definition
For the RVM regression model the log marginal likelihood factors as
$$L(\boldsymbol{\alpha}) = L(\boldsymbol{\alpha}_{-i}) + \lambda(\alpha_i),$$
$$\lambda(\alpha_i) = \frac{1}{2}\left[\ln\alpha_i - \ln(\alpha_i + s_i) + \frac{q_i^2}{\alpha_i+s_i}\right].$$
Maximising $\lambda(\alpha_i)$ yields a unique closed-form solution:
$$\alpha_i = \frac{s_i^2}{q_i^2 - s_i} \quad \text{if } q_i^2 > s_i, \quad \text{else } \alpha_i \to \infty.$$
This is a global maximum of $\lambda(\alpha_i)$ (confirmed by the second derivative), establishing a sharp threshold criterion for inclusion or exclusion of each basis function.

### Why it matters
This result (Faul and Tipping, 2002) provides a rigorous mathematical account of why RVM training produces sparse solutions: the marginal likelihood, viewed as a function of a single hyperparameter, has its global maximum either at a finite value (inclusion) or at infinity (pruning), with no intermediate solutions. It enables the efficient sequential sparse Bayesian learning algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]