---
aliases: []
also_type: []
analogous-to:
- exponential-family
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:conjugate-prior
knowledge_type: concept
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[gaussian-distribution]]'
- '[[bayesian-linear-regression]]'
sources:
- '[[deisenroth-mml]]'
- '[[kroese-statistical-modeling]]'
- '[[capretto-bambi-2022]]'
tags:
- probability-theory
title: Conjugate Prior
understanding: 0
uses:
- sufficient-statistics
---

A prior distribution that, combined with a given likelihood, yields a posterior in the same distributional family — enabling closed-form Bayesian updating; arises naturally from the exponential family structure where the natural parameters of the prior and posterior match.

## Reading Path
- [[deisenroth-mml]] (unread) — foundational treatment: Gaussian-Gaussian conjugacy, table of conjugate pairs
- [[kroese-statistical-modeling-ch08]] (unread) — conjugate Bayesian models for normal (unknown μ and σ²), normal linear, and multinomial models; §8.5 priors and conjugacy
- [[capretto-bambi-2022]] (unread) — Bambi's automatic priors are motivated by approximate conjugacy (Normal priors for Normal likelihoods, HalfStudentT for variance)

## Connections
- [[exponential-family]] — analogous-to
- [[sufficient-statistics]] — uses: Conjugate priors combine with the likelihood through its sufficient statistics, giving closed-form posterior updates.

## Canonical conjugate pairs from MacKay Ch. 23
MacKay's distribution catalog supplies the standard conjugate families used throughout Bayesian modelling:

- **Beta–Binomial**: a $\mathrm{Beta}(u_1,u_2)$ prior on a coin's bias updates to $\mathrm{Beta}(u_1+r,\ u_2+N-r)$ after $r$ heads in $N$ trials.
- **Dirichlet–Multinomial**: the $I$-dimensional generalization; observing counts $\mathbf{F}$ updates $\alpha\mathbf{m}\to\alpha\mathbf{m}+\mathbf{F}$. The concentration $\alpha$ quantifies how many observations are needed before data dominate the prior.
- **Gamma / Inverse-gamma**: the gamma is conjugate for a Poisson rate or a Gaussian *precision* $\tau=1/\sigma^2$; its reciprocal, the inverse-gamma, is conjugate for a Gaussian *variance* $\sigma^2$.

In each case the prior's pseudo-counts add directly to the data counts, which is the practical hallmark of conjugacy.