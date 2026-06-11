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
contrasts-with:
- lasso
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- bayesian-inference
id: pkis:concept:spike-and-slab-prior
instantiates:
- mixture-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
specializes:
- spike-and-slab
tags:
- sparsity
- variable-selection
- l0-regularization
- mixture-prior
- MCMC
title: Spike-and-Slab Prior
understanding: 0
uses:
- regularization
---

## Definition
$$p(w) = \prod_{d=1}^D \left[(1-\pi)\,\delta(w_d) + \pi\,\mathcal{N}(w_d \mid 0, \sigma_w^2)\right]$$

A two-component mixture prior that places probability mass $1-\pi$ exactly at zero (the "spike") and probability $\pi$ on a broad Gaussian (the "slab"), inducing exact sparsity in the weight vector.

### Why it matters
MAP estimation under the spike-and-slab prior is equivalent to $\ell_0$ regularization. Unlike the Laplace (lasso) prior, *posterior samples* are also sparse, which leads to better prediction accuracy. It is the canonical Bayesian approach to variable selection, though exact inference requires MCMC or greedy search over the $2^D$ model space.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[spike-and-slab]] — specializes
- [[mixture-models]] — instantiates
- [[regularization]] — uses: MAP estimation equivalent to l0 regularization
- [[lasso]] — contrasts-with
[To be populated during integration]