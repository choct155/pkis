---
title: "Gibbs Sampler"
knowledge_type: technique
also_type: []
domain: [bayesian-stats]
tags: [mcmc, posterior-sampling, markov-chains, conditional-distributions, bayesian-computation]
related_concepts: ["[[data-augmentation]]", "[[metropolis-algorithm]]", "[[directed-graphical-models]]", "[[conjugate-prior]]", "[[probability-theory]]"]
sources: ["[[tanner-tools-statistical-inference]]", "[[kroese-statistical-modeling]]", "[[lange-applied-probability]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

An iterative MCMC algorithm for sampling from a multivariate posterior p(θ_1, ..., θ_d | Y) by cycling through the full conditional distributions: at step t+1, draw θ_i^{(t+1)} from p(θ_i | θ_{-i}^{(t)}, Y) for each i in sequence. Under regularity conditions, the generated chain is ergodic with the joint posterior as its stationary distribution.

The Gibbs sampler is the multi-component generalization of data augmentation (two components). Its key advantage is that full conditionals are often available in closed form (especially with conjugate priors in hierarchical models) even when the joint posterior is intractable. The Griddy Gibbs sampler handles non-standard conditionals by numerical integration on an adaptive grid. Convergence can be assessed via the Gibbs stopper (monitoring changes in the predictive distribution) or control variates.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary treatment; Chapter 6 covers theory, examples (rat growth, Poisson change-point, GLMs with random effects), convergence diagnostics, Griddy Gibbs, and application to conditional frequentist inference
- [[tanner-tools-statistical-inference-ch06]] (unread) — primary chapter
- [[kroese-statistical-modeling-ch07]] (unread) — integrated treatment within Monte Carlo chapter; presents Gibbs as special case of Metropolis-Hastings
- [[lange-applied-probability-ch07]] (unread) — Gibbs sampling treated as special case of Hastings-Metropolis; convergence analysis
