---
title: "Expectation-Maximization (EM) Algorithm"
knowledge_type: technique
also_type: []
domain: [statistical-learning, bayesian-stats]
tags: [optimization, probability-theory]
related_concepts: []
sources: ["[[hastie-esl]]", "[[deisenroth-mml]]", "[[sargent-sims-business-cycle-1977]]", "[[blei-vi-review]]", "[[ganguly-intro-vi]]", "[[sjolund-parametric-vi]]", "[[yellapragada-variational-bayes]]", "[[tanner-tools-statistical-inference]]", "[[kroese-statistical-modeling]]", "[[lange-applied-probability]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 10
understanding: 0
maturity: settled
---

Iterative technique for maximum likelihood estimation in latent variable models, alternating between computing expected sufficient statistics under the current parameter estimates (E-step) and maximizing the complete-data likelihood (M-step).

## Reading Path
- [[hastie-esl]] (unread) — general treatment of EM in the context of mixture models and missing data
- [[deisenroth-mml]] (unread) — EM for Gaussian mixture models; covers E-step as computing responsibilities and M-step as updating cluster parameters
- [[sargent-sims-business-cycle-1977]] (unread) — frequency-domain factor analysis algorithm (Geweke) referenced as the estimation method for the unobservable index model; analogous to EM for factor models in spectral domain
- [[blei-vi-review]] (unread) — Section 4: EM as special case of CAVI under conjugate models; complete-conditional structure connection
- [[ganguly-intro-vi]] (unread) — Section 3–5: EM connection via ELBO derivation; CAVI generalizes EM's E-step to non-conjugate models
- [[sjolund-parametric-vi]] (unread) — parametric VI as generalization of EM to non-conjugate models via reparameterization
- [[yellapragada-variational-bayes]] (unread) — MDL loss formulation connects VI to EM for Bayesian neural networks
- [[tanner-tools-statistical-inference-ch04]] (unread) — most thorough treatment in wiki; five standard-error methods including missing information principle; Monte Carlo E-step (MCEM)
- [[kroese-statistical-modeling-ch06]] (unread) — EM as likelihood maximization for latent variable models; Jensen's inequality convergence proof; mixture model examples
- [[lange-applied-probability-ch16]] (unread) — EM reinterpreted as entropy maximization; information-theoretic perspective
