---
aliases:
- GMM
also_type:
- framework
analogous-to:
- soft-k-means
- kernel-density-estimation
applies:
- number-of-components-selection
- density-estimation
coverage: 4
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:gaussian-mixture-models
instantiates:
- latent-variable-models
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
specializes:
- mixture-models
tags:
- probability-theory
- simulation
title: Gaussian Mixture Models (GMM)
understanding: 0
uses:
- em-algorithm
- ancestral-sampling
- gibbs-sampler
- dirichlet-distribution
---

## Reading Path
- [[deisenroth-mml]] (unread) — generative model derivation; EM fit with responsibilities; connection to K-means as hard-assignment limit
- [[blei-vi-review]] (unread) — Section 3: complete CAVI derivation for Bayesian GMM; canonical VI illustration with Dirichlet mixture prior
- [[ganguly-intro-vi]] (unread) — Section 5: CAVI toy problem on 3-component Gaussian mixture; Algorithm 1 step-by-step
- [[kroese-statistical-modeling-ch06]] (unread) — EM algorithm for GMMs as the primary worked example of the EM procedure

Density estimation model that represents the data distribution as a weighted sum of Gaussian components $p(x) = \sum_k \pi_k \mathcal{N}(x | \mu_k, \Sigma_k)$, fit via the EM algorithm; serves as both a generative model and a soft-clustering technique.

## Connections
- [[density-estimation]] — applies
- [[number-of-components-selection]] — applies
- [[dirichlet-distribution]] — uses
- [[gibbs-sampler]] — uses
- [[kernel-density-estimation]] — analogous-to
- [[soft-k-means]] — analogous-to
- [[ancestral-sampling]] — uses
- [[mixture-models]] — specializes
- [[latent-variable-models]] — instantiates: Mixture models are latent variable models with the class label as the latent.
- [[em-algorithm]] — uses: GMMs are fit by EM, computing responsibilities (E) and updating means, covariances, weights (M).

## Relation to K-means and soft K-means
MacKay (ITILA Ch. 20) reaches GMMs by repairing K-means. Plain K-means is a *hard* clustering that represents only distances to means, so it misassigns points across clusters of unequal weight and slices elongated clusters in half. Soft K-means fixes the hard assignment with a stiffness-$\beta$ softmax over distances, but version 1 still has a single isotropic lengthscale $\sigma = 1/\sqrt{\beta}$ shared by all clusters — no per-cluster weight $\pi_k$ or covariance $\Sigma_k$. A full Gaussian mixture restores exactly these missing degrees of freedom: the responsibility $r_k^{(n)} = \pi_k \mathcal{N}(\mathbf{x}^{(n)}|\mu_k,\Sigma_k) / \sum_{k'} \pi_{k'} \mathcal{N}(\mathbf{x}^{(n)}|\mu_{k'},\Sigma_{k'})$ generalizes the soft K-means softmax, and EM updates means, covariances, and mixing weights. K-means is recovered as the hard-assignment, equal-weight, spherical-fixed-variance limit.