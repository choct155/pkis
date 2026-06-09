---
aliases: []
also_type: []
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:importance-sampling
knowledge_type: technique
maturity: settled
related_concepts:
- '[[data-augmentation]]'
- '[[gibbs-sampler]]'
- '[[probability-theory]]'
- '[[bayesian-linear-regression]]'
sources:
- '[[tanner-tools-statistical-inference]]'
- '[[kroese-statistical-modeling]]'
- '[[lange-applied-probability]]'
specializes:
- numerical-vs-simulation-integration
tags:
- monte-carlo
- posterior-inference
- likelihood
- non-iterative
- variance-reduction
- sir-algorithm
title: Importance Sampling
understanding: 0
---

A non-iterative Monte Carlo technique for estimating expectations under a target distribution p(θ) by drawing samples from an alternative proposal distribution q(θ) and reweighting: E_p[f(θ)] ≈ Σ w_i f(θ_i) / Σ w_i where θ_i ~ q(θ) and w_i = p(θ_i)/q(θ_i). When p is the posterior, the weights are proportional to the likelihood times prior divided by the proposal.

Sampling/Importance Resampling (SIR) extends this to approximate iid posterior samples: draw a large set from q, then resample without replacement using normalized importance weights. The result is an approximately iid sample from p, useful when subsequent calculations require iid structure. Key requirement: q(θ) > 0 wherever p(θ) > 0 and the tails of q must dominate those of p to avoid weight degeneracy.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary treatment; Chapter 3 covers importance sampling and rejection-acceptance in the likelihood/posterior context; Chapter 5 covers SIR and sequential imputation
- [[tanner-tools-statistical-inference-ch03]] (unread) — primary chapter
- [[tanner-tools-statistical-inference-ch05]] (unread) — SIR treatment
- [[kroese-statistical-modeling-ch07]] (unread) — importance sampling in the context of Monte Carlo methods alongside bootstrap and MCMC
- [[lange-applied-probability-ch12]] (unread) — asymptotic methods context including importance-weighted approximations

## MacKay's Cautions: Heavy Tails and the High-Dimensional Weight Catastrophe
MacKay stresses that importance sampling solves **only** Problem 2 (estimating $\Phi=\langle\varphi\rangle$); it does not generate samples from $P$. Drawing $x^{(r)}\sim Q$ and reweighting by $w_r = P^*(x^{(r)})/Q^*(x^{(r)})$ gives the self-normalized estimator
$$\hat{\Phi} = \frac{\sum_r w_r\,\varphi(x^{(r)})}{\sum_r w_r},$$
which is consistent (it converges to $\Phi$) but **biased for finite $R$**, because it is a ratio of two unbiased estimators of $Z_P/Z_Q$ and $(Z_P/Z_Q)\Phi$.

### Why heavy tails are essential
The estimator's reliability is hard to assess: if $Q$ is small where $|\varphi P^*|$ is large, no sample may ever land there, and the empirical variance gives no warning of a wildly wrong answer. MacKay's amino-acid example shows a Gaussian sampler giving glitchy, non-converged estimates even after $10^6$ samples, while a heavy-tailed Cauchy sampler converges after a few thousand. **An importance sampler must have heavier tails than the target.** Indeed even in 1-D with two Gaussians, $\text{var}(w)$ becomes infinite once $\sigma_q^2 < \tfrac12\sigma_p^2$.

### High-dimensional weight catastrophe
In $N$ dimensions the weights vary enormously even when $Q$ is reasonable. For a Gaussian $Q$ targeting a uniform sphere, the largest of 100 weights typically exceeds the median by $\exp(\sqrt{2N})$ — about $10^{19}$ at $N=1000$. The estimate is then dominated by a handful of samples, so importance sampling is impractical in high dimensions unless $Q$ is a near-perfect match to $P$.

## Connections
- [[numerical-vs-simulation-integration]] — specializes: Importance sampling is a simulation-based integration method.