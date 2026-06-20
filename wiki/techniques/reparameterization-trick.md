---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- bayesian-stats
- deep-learning
- optimization
id: pkis:technique:reparameterization-trick
knowledge_type: technique
maturity: settled
related_concepts:
- '[[variational-inference]]'
- '[[elbo]]'
- '[[amortized-inference]]'
- '[[automatic-differentiation]]'
sources:
- '[[sjolund-parametric-vi]]'
- '[[yellapragada-variational-bayes]]'
- mohamed-monte-2020
tags:
- variational-methods
- stochastic-optimization
- deep-learning
- automatic-differentiation
title: Reparameterization Trick
understanding: 0
---

A gradient estimation method that reformulates a random variable z ~ q_β(z) as a deterministic transformation z = g_β(ε) of a noise variable ε ~ p(ε) with no parameters, moving the parameter dependence outside the expectation and enabling standard backpropagation to compute ∇_β E_q[f(z)] = E_ε[∇_β f(g_β(ε))] with low variance; the canonical example is z = μ + σ·ε for Gaussian q.

## Connections

- [[variational-inference]] — uses: reparameterization is the dominant gradient estimator for parametric VI with continuous latent variables
- [[elbo]] — uses: enables low-variance Monte Carlo gradient estimates of ∇_β ELBO(q_β)
- [[automatic-differentiation]] — uses: after reparameterization, standard AD computes exact gradients through the transformed expectation
- [[amortized-inference]] — prerequisite-of: amortized VI (e.g., VAE encoder) requires differentiating through the stochastic encoder output, which the reparameterization trick enables
- [[variational-autoencoder]] — used-by: the VAE's training algorithm depends fundamentally on reparameterizing z = μ(x) + σ(x)·ε

## Reading Path

- [[sjolund-parametric-vi]] (unread) — dedicated section with Examples 4 and 5; derivation from score-function form; comparison with BBVI; validity conditions
- [[yellapragada-variational-bayes]] (unread) — Section 3.2.1; original Kingma & Welling formulation; z = g_φ(ε,x) notation; SGVB estimator