---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- bayesian-statistics
- statistics
id: pkis:technique:gaussian-gaussian-conjugate
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
tags:
- Gaussian
- conjugate-prior
- shrinkage
- precision
- posterior-mean
title: Gaussian-Gaussian Conjugate Model (known variance)
understanding: 0
---

## Definition
For $N$ i.i.d. observations $y_n\sim\mathcal{N}(\mu,\sigma^2)$ with known $\sigma^2$, the conjugate prior on $\mu$ is $\mathcal{N}(\bar{m},\bar{\tau}^2)$, giving the closed-form posterior:
$$p(\mu|D,\sigma^2)=\mathcal{N}(\mu\mid\hat{m},\hat{\lambda}^{-1})$$
$$\hat{\lambda}=\bar{\lambda}+N\lambda,\qquad \hat{m}=\frac{N\lambda\,\bar{y}+\bar{\lambda}\,\bar{m}}{\hat{\lambda}}$$
where $\lambda=1/\sigma^2$, $\bar{\lambda}=1/\bar{\tau}^2$.

The posterior mean is a convex combination of the prior mean and empirical mean, weighted by their respective precisions. This is a **shrinkage estimator**: the data pull $\hat{m}$ toward $\bar{y}$ while the prior pulls it toward $\bar{m}$.

### Why it matters
This is the simplest conjugate Gaussian update and serves as the building block for Kalman filters, Gaussian process regression, and hierarchical Gaussian models. The precision-weighted combination principle generalises to any linear-Gaussian model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]