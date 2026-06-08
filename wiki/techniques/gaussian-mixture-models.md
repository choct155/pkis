---
aliases:
- GMM
also_type:
- framework
coverage: 4
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:gaussian-mixture-models
knowledge_type: technique
maturity: settled
related_concepts:
- '[[gaussian-distribution]]'
- '[[em-algorithm]]'
- '[[probability-theory]]'
sources:
- '[[deisenroth-mml]]'
- '[[blei-vi-review]]'
- '[[ganguly-intro-vi]]'
- '[[kroese-statistical-modeling]]'
tags:
- probability-theory
- simulation
title: Gaussian Mixture Models (GMM)
understanding: 0
uses:
- em-algorithm
---

## Reading Path
- [[deisenroth-mml]] (unread) — generative model derivation; EM fit with responsibilities; connection to K-means as hard-assignment limit
- [[blei-vi-review]] (unread) — Section 3: complete CAVI derivation for Bayesian GMM; canonical VI illustration with Dirichlet mixture prior
- [[ganguly-intro-vi]] (unread) — Section 5: CAVI toy problem on 3-component Gaussian mixture; Algorithm 1 step-by-step
- [[kroese-statistical-modeling-ch06]] (unread) — EM algorithm for GMMs as the primary worked example of the EM procedure

Density estimation model that represents the data distribution as a weighted sum of Gaussian components $p(x) = \sum_k \pi_k \mathcal{N}(x | \mu_k, \Sigma_k)$, fit via the EM algorithm; serves as both a generative model and a soft-clustering technique.

## Connections
- [[em-algorithm]] — uses: GMMs are fit by EM, computing responsibilities (E) and updating means, covariances, weights (M).