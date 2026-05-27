---
id: "pkis:technique:normalizing-flows"
aliases: []
title: "Normalizing Flows"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, deep-learning]
tags: [variational-methods, generative-models, deep-learning, probability-theory]
related_concepts: ["[[variational-inference]]", "[[variational-autoencoder]]", "[[probability-theory]]"]
sources: ["[[yellapragada-variational-bayes]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

A family of generative models that transform a simple base distribution (e.g., Gaussian) into a complex target distribution through a sequence of invertible, differentiable mappings f_k; the change-of-variables formula gives the log-density of the final variable, enabling exact likelihood evaluation; used in VI to construct expressive variational posteriors beyond the mean-field family.

## Connections

- [[variational-inference]] — extends: normalizing flows enrich the variational family beyond mean-field, enabling more accurate posterior approximations
- [[variational-autoencoder]] — extends: flow-based posteriors can replace the diagonal Gaussian encoder in VAEs (IAF-VAE, NVAE)
- [[reparameterization-trick]] — uses: flows are typically combined with reparameterization for gradient-based ELBO optimization

## Reading Path

- [[yellapragada-variational-bayes]] (unread) — Section 2.5; change-of-variables formula for flows; Multiplicative Normalizing Flows for BNNs (Section 3.4); masked RealNVP with inverse autoregressive flow
