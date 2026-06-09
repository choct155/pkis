---
aliases: []
also_type: []
applies:
- density-estimation
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:kernel-density-estimation
knowledge_type: technique
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[gaussian-distribution]]'
- '[[bootstrap]]'
sources:
- '[[kroese-statistical-modeling]]'
tags:
- nonparametric
- density-estimation
- smoothing
- kernel-functions
- bandwidth
title: Kernel Density Estimation
understanding: 0
---

Kernel Density Estimation (KDE) is a nonparametric method for estimating a continuous probability density function from data by placing a smooth kernel function (typically Gaussian) centered at each observation, producing a smooth estimate f̂(x) = (1/nh) Σ K((x - xᵢ)/h) controlled by bandwidth h.

## Connections
- [[density-estimation]] — applies
- [[bootstrap]] — uses: the smoothed bootstrap uses KDE in place of the empirical CDF as the resampling distribution
- [[gaussian-process-regression]] — contrasts-with: KDE estimates densities nonparametrically; GP regression estimates conditional means nonparametrically

## Reading Path
- [[kroese-statistical-modeling-ch07]] (unread) — KDE in the context of Monte Carlo methods: empirical CDF, density estimation, and resampling