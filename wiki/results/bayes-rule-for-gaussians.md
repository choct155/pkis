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
- probability
- statistics
- machine-learning
id: pkis:result:bayes-rule-for-gaussians
instantiates:
- conjugate-prior
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch03
specializes:
- linear-gaussian-system
tags:
- conjugate-prior
- gaussian
- posterior
- bayesian-inference
title: Bayes Rule for Gaussians
understanding: 0
uses:
- mvn-marginal-conditional
- completing-the-square-multivariate
---

## Definition
Given a Gaussian prior $p(z) = \mathcal{N}(z|\mu_z, \Sigma_z)$ and a Gaussian likelihood $p(y|z) = \mathcal{N}(y|Wz+b, \Sigma_y)$, the posterior and marginal likelihood are:
$$p(z|y) = \mathcal{N}(z | \mu_{z|y}, \Sigma_{z|y})$$
$$\Sigma_{z|y}^{-1} = \Sigma_z^{-1} + W^T \Sigma_y^{-1} W$$
$$\mu_{z|y} = \Sigma_{z|y}\left[W^T \Sigma_y^{-1}(y - b) + \Sigma_z^{-1}\mu_z\right]$$
$$p(y) = \mathcal{N}(y | W\mu_z + b,\; \Sigma_y + W\Sigma_z W^T)$$

The Gaussian prior is conjugate to the Gaussian likelihood, so the posterior is Gaussian and all computations are analytic.

### Why it matters
This is the fundamental engine behind Kalman filtering, Gaussian process regression, Bayesian linear regression, and sensor fusion. The posterior precision equals the prior precision plus the Fisher information $W^T\Sigma_y^{-1}W$ from the data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[completing-the-square-multivariate]] — uses
- [[mvn-marginal-conditional]] — uses
- [[conjugate-prior]] — instantiates
- [[linear-gaussian-system]] — specializes
[To be populated during integration]