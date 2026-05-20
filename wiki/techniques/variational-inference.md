---
title: "Variational Inference"
knowledge_type: technique
also_type: [framework]
domain: [bayesian-stats, optimization]
tags: [variational-methods, approximate-inference, probability-theory, optimization]
related_concepts: ["[[elbo]]", "[[mean-field-approximation]]", "[[kl-divergence]]", "[[directed-graphical-models]]", "[[em-algorithm]]"]
sources: ["[[blei-vi-review]]", "[[ganguly-intro-vi]]", "[[sjolund-parametric-vi]]", "[[yellapragada-variational-bayes]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: evolving
---

A family of algorithms for approximating intractable posterior distributions in Bayesian models by casting inference as optimization: given a family Q of tractable distributions, find the member q*(z) that minimizes KL(q(z)‖p(z|x)), equivalently maximizing the Evidence Lower Bound (ELBO).

Classification note: assigned as technique (it is a procedure with inputs — model, data, variational family — and output — approximate posterior) but also qualifies as framework because it organizes a large ecosystem of sub-techniques (mean-field, amortized, SVI, BBVI, normalizing flows) under a shared objective.

## Connections

- [[em-algorithm]] — extends: EM is the special case of VI where the E-step posterior is computed exactly; VI generalizes this to intractable models by optimizing an approximate E-step
- [[gaussian-mixture-models]] — uses: the Gaussian mixture is the canonical pedagogical example for VI (CAVI derivation)
- [[elbo]] — uses: VI optimizes the ELBO as a tractable surrogate for the intractable KL to posterior
- [[mean-field-approximation]] — specializes: mean-field VI is the historically dominant sub-family; assumes full factorization of q
- [[directed-graphical-models]] — uses: the conditional independence structure of the model governs which CAVI updates are feasible
- [[kl-divergence]] — uses: reverse KL(q‖p) is the canonical objective; forward KL and α-divergences are active alternatives

## Reading Path

- [[blei-vi-review]] (unread) — canonical statistical review; full CAVI derivation, exponential family treatment, SVI extension, and open problems survey
- [[ganguly-intro-vi]] (unread) — accessible introduction; strong ELBO derivation, mean-field CAVI example, VAE and VAE-GAN applications
- [[sjolund-parametric-vi]] (unread) — parametric/neural-network perspective; reparameterization trick, amortized inference, BBVI gradient estimation
- [[yellapragada-variational-bayes]] (unread) — application survey; Bayesian neural networks, normalizing flows, RL exploration, continual learning
