---
aliases: []
also_type: []
analogous-to:
- kernel-smoothing
- gaussian-mixture-models
applies:
- density-estimation
contrasts-with:
- k-nearest-neighbors
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:kernel-density-estimation
instantiates:
- density-estimation
knowledge_type: technique
maturity: settled
prerequisite-of:
- nadaraya-watson-estimator
- knn-classifier
related_concepts:
- '[[probability-theory]]'
- '[[gaussian-distribution]]'
- '[[bootstrap]]'
sources:
- '[[kroese-statistical-modeling]]'
specializes:
- gaussian-mixture-models
tags:
- nonparametric
- density-estimation
- smoothing
- kernel-functions
- bandwidth
title: Kernel Density Estimation
understanding: 0
uses:
- convolution-of-distributions
- curse-of-dimensionality
---

Kernel Density Estimation (KDE) is a nonparametric method for estimating a continuous probability density function from data by placing a smooth kernel function (typically Gaussian) centered at each observation, producing a smooth estimate f̂(x) = (1/nh) Σ K((x - xᵢ)/h) controlled by bandwidth h.

## Connections
- [[density-estimation]] — instantiates
- [[gaussian-mixture-models]] — specializes: KDE is a GMM with one component per data point and fixed bandwidth
- [[knn-classifier]] — prerequisite-of: KNN classifier can be derived as a generative classifier using balloon KDE
- [[nadaraya-watson-estimator]] — prerequisite-of: KDE of the joint density leads directly to the N-W conditional mean estimator
- [[gaussian-mixture-models]] — analogous-to: Gaussian KDE is equal-weight mixture of N Gaussians
- [[curse-of-dimensionality]] — uses: KDE suffers from exponential scaling with dimension
- [[k-nearest-neighbors]] — contrasts-with: KDE fixes V and estimates K; KNN fixes K and estimates V
- [[convolution-of-distributions]] — uses
- [[kernel-smoothing]] — analogous-to
- [[density-estimation]] — applies
- [[bootstrap]] — uses: the smoothed bootstrap uses KDE in place of the empirical CDF as the resampling distribution
- [[gaussian-process-regression]] — contrasts-with: KDE estimates densities nonparametrically; GP regression estimates conditional means nonparametrically

## Reading Path
- [[kroese-statistical-modeling-ch07]] (unread) — KDE in the context of Monte Carlo methods: empirical CDF, density estimation, and resampling