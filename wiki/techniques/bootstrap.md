---
aliases: []
also_type: []
analogous-to:
- bayesian-model-averaging
applies:
- model-selection-problem
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
id: pkis:technique:bootstrap
knowledge_type: technique
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[cross-validation]]'
- '[[hypothesis-testing]]'
sources:
- '[[kroese-statistical-modeling]]'
tags:
- resampling
- monte-carlo
- nonparametric
- inference
- confidence-intervals
title: Bootstrap
understanding: 0
uses:
- maximum-likelihood-estimation
---

The bootstrap is a resampling technique that estimates the sampling distribution of a statistic T(X) by repeatedly drawing samples with replacement from the observed data, computing T on each resample, and using the empirical distribution of T across B bootstrap replications as a proxy for the true sampling distribution.

## Connections
- [[maximum-likelihood-estimation]] — uses: the bootstrap is a computer implementation of nonparametric/parametric maximum likelihood
- [[bayesian-model-averaging]] — analogous-to: the nonparametric bootstrap distribution approximates a noninformative-prior Bayes posterior; the bagged estimate is an approximate posterior mean
- [[model-selection-problem]] — applies
- [[cross-validation]] — contrasts-with: both estimate generalization error but via different resampling schemes; bootstrap averages over non-independent resamples while CV partitions
- [[hypothesis-testing]] — uses: bootstrap provides a distribution-free method for computing p-values and confidence intervals without distributional assumptions

## Reading Path
- [[kroese-statistical-modeling-ch07]] (unread) — primary treatment: bootstrap for standard errors and confidence intervals (BCa), with connections to kernel density estimation and Monte Carlo