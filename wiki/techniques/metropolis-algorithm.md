---
id: "pkis:technique:metropolis-algorithm"
aliases: []
title: "Metropolis Algorithm"
knowledge_type: technique
also_type: []
domain: [bayesian-stats]
tags: [mcmc, posterior-sampling, markov-chains, acceptance-rejection, bayesian-computation, metropolis-hastings]
related_concepts: ["[[gibbs-sampler]]", "[[data-augmentation]]", "[[probability-theory]]", "[[directed-graphical-models]]"]
sources: ["[[tanner-tools-statistical-inference]]", "[[kroese-statistical-modeling]]", "[[lange-applied-probability]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

An MCMC algorithm for sampling from p(θ|Y) ∝ p(Y|θ)p(θ) by constructing a Markov chain via proposal-acceptance: propose θ* from a symmetric proposal q(θ*|θ^{(t)}), accept with probability min(1, p(θ*|Y)/p(θ^{(t)}|Y)), otherwise stay at θ^{(t)}. The chain's stationary distribution is the target posterior, with correctness guaranteed by detailed balance.

Unlike the Gibbs sampler, the Metropolis algorithm is a non-augmentation method — it operates directly on the joint posterior modulo its normalizing constant. This makes it applicable whenever the posterior can be evaluated up to a constant, even when conditionals are not available in closed form. The Metropolis-Hastings generalization allows asymmetric proposals with an additional correction term. Metropolis subchains can be embedded within Gibbs sampling for components whose conditionals are non-standard.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary treatment in second edition (1993); Section 6.5 covers discrete-space Markov chain theory, Metropolis method, and Metropolis subchains; convergence assessment methods
- [[tanner-tools-statistical-inference-ch06]] (unread) — primary chapter
- [[kroese-statistical-modeling-ch07]] (unread) — Metropolis-Hastings in Monte Carlo chapter; presents as the general MCMC algorithm of which Metropolis is the symmetric-proposal special case
- [[lange-applied-probability-ch07]] (unread) — foundational Hastings-Metropolis treatment with convergence of independence sampler
