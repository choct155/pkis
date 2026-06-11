---
aliases: []
also_type: []
applies:
- elbo
- variational-inference
- density-estimation
- latent-variable-models
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
- deep-learning
generalizes:
- autoregressive-model
id: pkis:technique:normalizing-flows
knowledge_type: technique
maturity: evolving
related_concepts:
- '[[variational-inference]]'
- '[[variational-autoencoder]]'
- '[[probability-theory]]'
sources:
- '[[yellapragada-variational-bayes]]'
tags:
- variational-methods
- generative-models
- deep-learning
- probability-theory
title: Normalizing Flows
understanding: 0
uses:
- change-of-variables-for-densities
- pushforward-distribution
- inverse-transform-sampling
- reparameterization-trick
- maximum-likelihood-estimation
---

A family of generative models that transform a simple base distribution (e.g., Gaussian) into a complex target distribution through a sequence of invertible, differentiable mappings f_k; the change-of-variables formula gives the log-density of the final variable, enabling exact likelihood evaluation; used in VI to construct expressive variational posteriors beyond the mean-field family.

## Connections
- [[autoregressive-model]] — generalizes
- [[maximum-likelihood-estimation]] — uses
- [[latent-variable-models]] — applies
- [[density-estimation]] — applies
- [[variational-inference]] — applies
- [[reparameterization-trick]] — uses
- [[elbo]] — applies: Used to train normalizing-flow variational posteriors via the ELBO
- [[inverse-transform-sampling]] — uses: The universal approximation argument for 1D flows is equivalent to inverse-CDF sampling
- [[pushforward-distribution]] — uses
- [[change-of-variables-for-densities]] — uses

- [[variational-inference]] — extends: normalizing flows enrich the variational family beyond mean-field, enabling more accurate posterior approximations
- [[variational-autoencoder]] — extends: flow-based posteriors can replace the diagonal Gaussian encoder in VAEs (IAF-VAE, NVAE)
- [[reparameterization-trick]] — uses: flows are typically combined with reparameterization for gradient-based ELBO optimization

## Reading Path

- [[yellapragada-variational-bayes]] (unread) — Section 2.5; change-of-variables formula for flows; Multiplicative Normalizing Flows for BNNs (Section 3.4); masked RealNVP with inverse autoregressive flow