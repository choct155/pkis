---
title: "Amortized Variational Inference"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, deep-learning, optimization]
tags: [variational-methods, approximate-inference, deep-learning, stochastic-optimization]
related_concepts: ["[[variational-inference]]", "[[variational-autoencoder]]", "[[reparameterization-trick]]", "[[neural-networks]]"]
sources: ["[[sjolund-parametric-vi]]", "[[yellapragada-variational-bayes]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A technique for scalable variational inference that replaces per-datapoint optimization of local variational parameters with a shared neural network (the inference network or encoder) trained to predict those parameters from the data point; the inference network Λ_θ(x_i) = ϕ_i amortizes the cost of inference over all data, enabling mini-batch SGD and making VI feasible for large datasets.

## Connections

- [[variational-inference]] — specializes: amortized inference is the parametric sub-family where variational parameters are functions of data rather than free variables
- [[variational-autoencoder]] — used-by: the VAE encoder is the canonical example of an amortized inference network
- [[reparameterization-trick]] — uses: amortized inference typically requires the reparameterization trick to backpropagate through the stochastic encoder output
- [[neural-networks]] — uses: the inference network Λ_θ is a neural network trained by gradient descent on the ELBO

## Reading Path

- [[sjolund-parametric-vi]] (unread) — Section on amortized VI; derives amortization from the per-datapoint ELBO decomposition; shows how Λ_θ(x_i) replaces ϕ_i optimization
- [[yellapragada-variational-bayes]] (unread) — Section 3.2; AEVB algorithm is the first widely-adopted amortized VI algorithm; minibatch ELBO estimator
