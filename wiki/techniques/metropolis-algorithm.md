---
aliases: []
also_type: []
applies:
- ising-model
contrasts-with:
- gibbs-sampler
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:technique:metropolis-algorithm
knowledge_type: technique
maturity: settled
related_concepts:
- '[[gibbs-sampler]]'
- '[[data-augmentation]]'
- '[[probability-theory]]'
- '[[directed-graphical-models]]'
sources:
- '[[tanner-tools-statistical-inference]]'
- '[[kroese-statistical-modeling]]'
- '[[lange-applied-probability]]'
specializes:
- mcmc
tags:
- mcmc
- posterior-sampling
- markov-chains
- acceptance-rejection
- bayesian-computation
- metropolis-hastings
title: Metropolis Algorithm
understanding: 0
---

An MCMC algorithm for sampling from p(θ|Y) ∝ p(Y|θ)p(θ) by constructing a Markov chain via proposal-acceptance: propose θ* from a symmetric proposal q(θ*|θ^{(t)}), accept with probability min(1, p(θ*|Y)/p(θ^{(t)}|Y)), otherwise stay at θ^{(t)}. The chain's stationary distribution is the target posterior, with correctness guaranteed by detailed balance.

Unlike the Gibbs sampler, the Metropolis algorithm is a non-augmentation method — it operates directly on the joint posterior modulo its normalizing constant. This makes it applicable whenever the posterior can be evaluated up to a constant, even when conditionals are not available in closed form. The Metropolis-Hastings generalization allows asymmetric proposals with an additional correction term. Metropolis subchains can be embedded within Gibbs sampling for components whose conditionals are non-standard.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary treatment in second edition (1993); Section 6.5 covers discrete-space Markov chain theory, Metropolis method, and Metropolis subchains; convergence assessment methods
- [[tanner-tools-statistical-inference-ch06]] (unread) — primary chapter
- [[kroese-statistical-modeling-ch07]] (unread) — Metropolis-Hastings in Monte Carlo chapter; presents as the general MCMC algorithm of which Metropolis is the symmetric-proposal special case
- [[lange-applied-probability-ch07]] (unread) — foundational Hastings-Metropolis treatment with convergence of independence sampler

## Connections
- [[gibbs-sampler]] — contrasts-with: On the same Ising target, Metropolis accepts unfavourable moves about twice as often, trading off mixing speed differently from the Gibbs conditional update.
- [[ising-model]] — applies: Metropolis spin-flip acceptance is an alternative MCMC sampler for the Ising Boltzmann distribution.
- [[mcmc]] — specializes: Metropolis-Hastings is the foundational instance of Markov chain Monte Carlo.

## MacKay's Formulation: Why Local Proposals Beat Global Ones
MacKay frames the Metropolis-Hastings algorithm as the answer to a defect of importance and rejection sampling: both demand a single proposal $Q(x)$ resembling $P(x)$ everywhere, which is hopeless in large problems. Metropolis instead uses a proposal $Q(x';x^{(t)})$ that **depends on the current state** — typically a Gaussian centred on $x^{(t)}$ — so $Q$ need not resemble $P$ at all.

A proposed $x'$ is accepted with probability $\min(1,a)$ where
$$a = \frac{P^*(x')}{P^*(x^{(t)})}\,\frac{Q(x^{(t)};x')}{Q(x';x^{(t)})}.$$
For symmetric $Q$ the ratio of $Q$'s is 1 (the original Metropolis method); the general asymmetric case is Metropolis-Hastings. Crucially, a *rejection* writes the current state onto the sample list again — unlike rejection sampling, where rejected points vanish.

### Random-walk penalty
MacKay's key quantitative lesson: a random-walk Metropolis chain explores by diffusion, so with step size $\ell$ and largest length scale $L$ it needs at least
$$T \simeq (L/\ell)^2$$
iterations per independent sample (and a further factor $1/f$ if only a fraction $f$ of proposals are accepted). In $N$-dimensional Gaussian targets this becomes $T\simeq(\sigma_{\max}/\sigma_{\min})^2$ — no catastrophic dependence on $N$ (good news, unlike rejection sampling), but a punishing dependence on the conditioning of the target. Abolishing this random walk motivates Hamiltonian Monte Carlo and overrelaxation.