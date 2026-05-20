---
title: "Bootstrap"
knowledge_type: technique
also_type: []
domain: [statistical-learning]
tags: [resampling, monte-carlo, nonparametric, inference, confidence-intervals]
related_concepts: ["[[probability-theory]]", "[[cross-validation]]", "[[hypothesis-testing]]"]
sources: ["[[kroese-statistical-modeling]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The bootstrap is a resampling technique that estimates the sampling distribution of a statistic T(X) by repeatedly drawing samples with replacement from the observed data, computing T on each resample, and using the empirical distribution of T across B bootstrap replications as a proxy for the true sampling distribution.

## Connections
- [[cross-validation]] — contrasts-with: both estimate generalization error but via different resampling schemes; bootstrap averages over non-independent resamples while CV partitions
- [[hypothesis-testing]] — uses: bootstrap provides a distribution-free method for computing p-values and confidence intervals without distributional assumptions

## Reading Path
- [[kroese-statistical-modeling-ch07]] (unread) — primary treatment: bootstrap for standard errors and confidence intervals (BCa), with connections to kernel density estimation and Monte Carlo
