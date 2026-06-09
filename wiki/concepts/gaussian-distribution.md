---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:gaussian-distribution
instantiates:
- exponential-family
- conjugate-prior
- maximum-entropy-principle
knowledge_type: concept
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[conjugate-prior]]'
- '[[gaussian-mixture-models]]'
- '[[bayesian-linear-regression]]'
sources:
- '[[deisenroth-mml]]'
- '[[capretto-bambi-2022]]'
- '[[kurz-hybrid-modeling-2022]]'
tags:
- probability-theory
title: Gaussian Distribution
understanding: 0
---

The normal distribution, characterized by mean and covariance, central to ML because it is the maximum entropy distribution for a given mean and variance, is closed under linear transformations and marginalization, and is its own conjugate prior — making Gaussian models analytically tractable.

## Reading Path
- [[deisenroth-mml]] (unread) — foundational treatment; max-entropy property, conjugacy, closure under linear transforms
- [[capretto-bambi-2022]] (unread) — Gaussian is the default Bambi family; automatic Normal priors for slopes and HalfStudentT for variance
- [[kurz-hybrid-modeling-2022]] (unread) — Gaussian prior p(ν) ~ N(ν_0, L_ν^{-1}) and Gaussian sensor noise model enable analytic conditional posteriors in BEM Bayesian update

## Precisions add: combining Gaussian evidence
When two independent sources contribute Gaussian information about an unknown $x$ — here a prior $\mathrm{Normal}(0,v)$ and a likelihood $\mathrm{Normal}(x,\sigma^2)$ — the posterior is Gaussian with **precision equal to the sum of the precisions**:
$$P(x\mid y)=\mathrm{Normal}\!\Big(\tfrac{v}{v+\sigma^2}y,\ \big(\tfrac1v+\tfrac1{\sigma^2}\big)^{-1}\Big).$$
The posterior mean is a precision-weighted blend of the data-best value $x=y$ and the prior-best value $x=0$. This is the dual of the familiar rule that *variances add when independent variables are summed*: under inference, precisions (inverse variances) add.

## Connections
- [[maximum-entropy-principle]] — instantiates: The Gaussian is the maxent distribution for fixed first and second moments.
- [[conjugate-prior]] — instantiates: The normal is its own conjugate prior for the mean with known variance; precisions add.
- [[exponential-family]] — instantiates