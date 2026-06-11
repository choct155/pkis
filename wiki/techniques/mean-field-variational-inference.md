---
aliases: []
also_type: []
analogous-to:
- em-algorithm
applies:
- intractable-posterior
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- laplace-approximation
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- Bayesian-inference
- approximate-inference
generalizes:
- structured-variational-inference
id: pkis:technique:mean-field-variational-inference
instantiates:
- inference-as-optimization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch10
- goodfellow-deeplearning-ch19
specializes:
- coordinate-ascent-vi
- variational-inference
- mean-field-approximation
tags:
- variational-inference
- mean-field
- coordinate-ascent
- ELBO
- factorized-approximation
title: Mean-Field Variational Inference (Factorized VI)
understanding: 0
uses:
- elbo
- kl-divergence
- zero-forcing-vs-zero-avoiding-kl
- calculus-of-variations-inference
---

## Definition
$$q^*(\mathbf{Z}_j) \propto \exp\!\left(\mathbb{E}_{i\neq j}[\ln p(\mathbf{X},\mathbf{Z})]\right)$$

Given an approximating family that factorizes as $q(\mathbf{Z})=\prod_{i=1}^{M}q_i(\mathbf{Z}_i)$, the ELBO is maximized by cycling through factors and setting each to the exponential of the expected log-joint under all other factors — a coordinate-ascent procedure whose fixed points are the optimal factorized approximation to the posterior.

### Why it matters
Provides a deterministic, scalable alternative to MCMC for posterior inference; naturally yields closed-form updates when conjugate priors are used, making it the workhorse of Bayesian deep learning and probabilistic topic models. The factorization assumption typically causes the approximation to under-estimate posterior variance and concentrate near a single mode of $\text{KL}(q\|p)$.

### Convergence
Coordinate-ascent is guaranteed to converge because the ELBO is convex with respect to each individual factor $q_j$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[calculus-of-variations-inference]] — uses
- [[structured-variational-inference]] — generalizes
- [[mean-field-approximation]] — specializes
- [[inference-as-optimization]] — instantiates
- [[laplace-approximation]] — contrasts-with
- [[zero-forcing-vs-zero-avoiding-kl]] — uses
- [[em-algorithm]] — analogous-to
- [[intractable-posterior]] — applies
- [[variational-inference]] — specializes
- [[coordinate-ascent-vi]] — specializes
- [[kl-divergence]] — uses
- [[elbo]] — uses
[To be populated during integration]