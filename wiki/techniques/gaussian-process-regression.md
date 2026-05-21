---
title: "Gaussian Process Regression"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, statistical-learning]
tags: [gaussian-process, nonparametric, bayesian-inference, kernel-functions, regression]
related_concepts: ["[[gaussian-distribution]]", "[[conjugate-prior]]", "[[kernel-density-estimation]]", "[[bayesian-linear-regression]]"]
sources: ["[[kroese-statistical-modeling]]", "[[kurz-hybrid-modeling-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Gaussian Process Regression (GPR) is a nonparametric Bayesian regression method that places a Gaussian process prior over the function space — a collection of random variables where any finite subset is jointly Gaussian, defined by a mean function m(x) and covariance kernel k(x,x') — yielding exact closed-form posterior inference over functions given observed data.

## Connections
- [[bayesian-linear-regression]] — generalizes: Bayesian linear regression is GPR with a linear kernel; GPR extends to nonlinear relationships via richer kernels
- [[conjugate-prior]] — uses: the Gaussian likelihood combined with a GP prior yields a GP posterior (exact conjugacy)
- [[kernel-density-estimation]] — contrasts-with: KDE estimates marginal densities; GPR estimates conditional mean functions via kernel-induced covariance structure
- [[variational-inference]] — contrasts-with: VI provides approximate posterior inference for GP models at scale; exact GPR requires O(n³) matrix inversion

## Reading Path
- [[kroese-statistical-modeling-ch11]] (unread) — primary treatment: GP regression, kernel functions, smoothing splines, connection to RKHS
- [[kurz-hybrid-modeling-2022]] (unread) — GP used as surrogate model in Bayesian optimization for free-shape trace pair design; provides mean and uncertainty for Expected Improvement acquisition
