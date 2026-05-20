---
title: "Importance Sampling"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, statistical-learning]
tags: [monte-carlo, posterior-inference, likelihood, non-iterative, variance-reduction, sir-algorithm]
related_concepts: ["[[data-augmentation]]", "[[gibbs-sampler]]", "[[probability-theory]]", "[[bayesian-linear-regression]]"]
sources: ["[[tanner-tools-statistical-inference]]", "[[kroese-statistical-modeling]]", "[[lange-applied-probability]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

A non-iterative Monte Carlo technique for estimating expectations under a target distribution p(θ) by drawing samples from an alternative proposal distribution q(θ) and reweighting: E_p[f(θ)] ≈ Σ w_i f(θ_i) / Σ w_i where θ_i ~ q(θ) and w_i = p(θ_i)/q(θ_i). When p is the posterior, the weights are proportional to the likelihood times prior divided by the proposal.

Sampling/Importance Resampling (SIR) extends this to approximate iid posterior samples: draw a large set from q, then resample without replacement using normalized importance weights. The result is an approximately iid sample from p, useful when subsequent calculations require iid structure. Key requirement: q(θ) > 0 wherever p(θ) > 0 and the tails of q must dominate those of p to avoid weight degeneracy.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary treatment; Chapter 3 covers importance sampling and rejection-acceptance in the likelihood/posterior context; Chapter 5 covers SIR and sequential imputation
- [[tanner-tools-statistical-inference-ch03]] (unread) — primary chapter
- [[tanner-tools-statistical-inference-ch05]] (unread) — SIR treatment
- [[kroese-statistical-modeling-ch07]] (unread) — importance sampling in the context of Monte Carlo methods alongside bootstrap and MCMC
- [[lange-applied-probability-ch12]] (unread) — asymptotic methods context including importance-weighted approximations
