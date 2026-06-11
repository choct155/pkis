---
aliases: []
also_type: []
analogous-to:
- exponential-family
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- probabilistic-modelling
extends:
- matrix-factorization-recommender
id: pkis:framework:probabilistic-matrix-factorization
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch22
specializes:
- latent-variable-models
tags:
- matrix-factorization
- latent-variable
- collaborative-filtering
- gaussian-likelihood
title: Probabilistic Matrix Factorization (PMF)
understanding: 0
uses:
- gaussian-distribution
- maximum-a-posteriori-estimation-map
---

## Definition
$$p(y_{ui} = y) = \mathcal{N}\!\left(y \,\big|\, \mu + b_u + c_i + \mathbf{u}_u^\top \mathbf{v}_i,\; \sigma^2\right)$$

PMF places a Gaussian likelihood over observed ratings and (optionally) Gaussian priors over the latent user/item vectors, converting matrix factorisation into a fully probabilistic latent-variable model.

### Why it matters
The probabilistic framing (i) makes MAP estimation equivalent to the regularised matrix-factorisation objective, (ii) allows likelihood-based model selection and uncertainty quantification, and (iii) naturally accommodates non-Gaussian likelihoods (Poisson, negative-Binomial) for count or integer ratings — analogous to exponential-family PCA.

### Connections
- [[exponential-family]] — analogous-to
- [[maximum-a-posteriori-estimation-map]] — uses
- [[gaussian-distribution]] — uses
- [[latent-variable-models]] — specializes
- [[matrix-factorization-recommender]] — extends
PMF is a special case of latent-variable models applied to relational data; Bayesian extensions place hyperpriors on $\sigma^2$ and embedding norms, enabling fully Bayesian inference via MCMC or variational methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]