---
title: "A Tutorial on Parametric Variational Inference"
knowledge_type: source
source_type: paper
authors: ["Jens Sjölund"]
year: 2023
domain: [bayesian-stats, optimization]
tags: [variational-methods, probability-theory, approximate-inference, stochastic-optimization]
source_url: "https://arxiv.org/abs/2301.01296"
drive_id: "1GPrvoKVvnpNpZe1RDAKQdDOIxjZc-YlA"
drive_path: "PKIS/sources/papers/sjolund-parametric-vi.pdf"
status: unread
date_added: 2026-05-20
date_updated: 2026-05-20
concepts: ["[[variational-inference]]", "[[elbo]]", "[[amortized-inference]]", "[[reparameterization-trick]]", "[[black-box-vi]]"]
---

Tutorial introducing variational inference from the parametric perspective that dominates modern practice, deliberately contrasting with the mean-field perspective found in most textbooks. The paper begins with the standard ELBO derivation — showing that log-evidence = ELBO + KL(q‖p(z|x)) — and then focuses on how to *optimize* the ELBO when the variational posterior is parameterized by a neural network or other expressive model. The central challenge addressed is that ELBO gradient estimation requires differentiating through an expectation whose distribution depends on the parameters. Two solutions are covered: the **reparameterization trick** (Kingma & Welling 2014), which decouples the source of randomness from the parameters and enables gradient flow; and **black-box variational inference (BBVI)** (Ranganath et al. 2014), which uses the REINFORCE/score-function estimator and is more general but suffers from high variance. The tutorial also derives **amortized variational inference**, where a neural network (the encoder) directly predicts the local variational parameters, enabling mini-batch SGD and connecting directly to the VAE architecture. Five worked examples with explicit calculations make the abstract concepts concrete.

## Key Knowledge Objects

- [[variational-inference]] (technique, high) — core framework; this tutorial emphasizes the parametric (neural-network parameterized) approach
- [[elbo]] (concept, high) — Evidence Lower Bound; derived from the identity log p(x) = ELBO + KL(q‖p(z|x))
- [[reparameterization-trick]] (technique, high) — decouple randomness from parameters via z = g_β(ε), ε ~ p(ε); enables moving gradient inside expectation
- [[amortized-inference]] (technique, high) — train a network Λ_θ to predict variational parameters ϕ_i = Λ_θ(x_i), replacing per-datapoint optimization with a shared predictor; foundation of VAE encoder
- [[black-box-vi]] (technique, moderate — could be principle) — gradient estimation using score-function / REINFORCE trick; general but high-variance; contrasts with reparameterization approach

## Key Extractions

1. **ELBO identity**: log p(x) = ELBO(q(z)) + KL(q(z)‖p(z|x)), where ELBO(q) = E_q[log p(x,z) − log q(z)]. Since KL ≥ 0, ELBO lower-bounds log p(x) for any choice of q. Maximizing ELBO minimizes the KL gap without ever needing to evaluate the intractable posterior.
2. **Variational family support constraint**: q(z) must be zero whenever p(z|x) = zero; otherwise ELBO = −∞. Concretely, a Gaussian variational posterior fails for a Gamma posterior because E_q[log z] is undefined for q having mass on negative reals (Example 3).
3. **Reparameterization trick mechanics**: For q_β(z) = N(z; μ, σ²), write z = μ + σε, ε ~ N(0,1). Then ∇_β E_q[f(z)] = E_ε[∇_β f(z(ε,β))], and Monte Carlo gradients are low-variance.
4. **Amortized inference**: Replace local variational parameters ϕ_i for each datapoint with a shared neural network ϕ_i = Λ_θ(x_i). Same ELBO objective, but optimization variables shift from {ϕ_1,...,ϕ_n} to θ. Enables SGD over minibatches; this is the VAE encoder.
5. **BBVI (score-function estimator)**: ∇_β E_q[f(z)] = E_q[(f(z) − baseline) ∇_β log q_β(z)]. General across all models, but estimator variance is typically too high for practical use without control variates.

## Connection Candidates

- [[variational-autoencoder]] — uses: the amortized inference section derives the VAE encoder directly as a special case of amortized VI
- [[gradient-descent]] — uses: ELBO maximization is performed via gradient-based optimization (SGD, Adam); natural gradient descent also discussed for exponential family models
- [[automatic-differentiation]] — uses: reparameterization trick relies on AD to compute gradients through the Monte Carlo ELBO estimate
- [[em-algorithm]] — contrasts-with: EM computes exact E-step posteriors (when tractable); parametric VI replaces exact E-step with a learned approximation, enabling non-conjugate models

## Awaiting Classification

- **black-box-vi** — candidate types: technique or principle
  - Case for technique: it's a concrete algorithm with inputs (model, data) and output (gradient estimates)
  - Case for principle: "use score-function gradient estimation" is a methodological stance applicable across many algorithms
  - What makes this hard: BBVI names both a specific paper's algorithm and a broader class of gradient estimators
