---
aliases: []
also_type: []
applies:
- clustering
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- probability
generalizes:
- k-means-clustering
id: pkis:concept:gaussian-mixture-model
instantiates:
- probabilistic-graphical-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch03
specializes:
- mixture-models
tags:
- clustering
- density-estimation
- latent-variables
- EM-algorithm
title: Gaussian Mixture Model
understanding: 0
uses:
- gaussian-distribution
- em-algorithm
- cluster-responsibility
---

## Definition
A **Gaussian Mixture Model (GMM)** is a mixture model in which each component is a multivariate Gaussian:
$$p(\mathbf{y}|\boldsymbol{\theta}) = \sum_{k=1}^{K} \pi_k \,\mathcal{N}(\mathbf{y}|\boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)$$
with mixing weights $\pi_k \geq 0$, $\sum_k \pi_k = 1$. It can be expressed hierarchically by introducing a discrete latent variable $z \in \{1,\ldots,K\}$: $p(z=k)=\pi_k$, $p(\mathbf{y}|z=k) = \mathcal{N}(\mathbf{y}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)$.

Given enough components, a GMM can approximate any smooth density on $\mathbb{R}^D$.

### Why it matters
GMMs are the canonical model for soft probabilistic clustering and density estimation of continuous data. The cluster responsibilities $r_{nk} = p(z_n=k|\mathbf{y}_n,\boldsymbol{\theta})$ drive the EM algorithm, and hard assignments recover K-means as a special case. They also serve as the likelihood component in many generative models and as priors in Bayesian non-parametrics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[probabilistic-graphical-models]] — instantiates
- [[cluster-responsibility]] — uses
- [[k-means-clustering]] — generalizes
- [[clustering]] — applies
- [[em-algorithm]] — uses
- [[gaussian-distribution]] — uses
- [[mixture-models]] — specializes
[To be populated during integration]