---
aliases: []
also_type: []
applies:
- vector-quantization
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
- machine-learning
- statistics
- unsupervised-learning
id: pkis:technique:k-means-algorithm
instantiates:
- clustering
- k-means-as-em-limit
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch09
specializes:
- gaussian-mixture-models
- em-algorithm
tags:
- clustering
- expectation-maximization
- vector-quantization
- coordinate-descent
title: K-Means Algorithm
understanding: 0
uses:
- cluster-dissimilarity-measures
---

## Definition
$$J = \sum_{n=1}^{N}\sum_{k=1}^{K} r_{nk}\|\mathbf{x}_n - \boldsymbol{\mu}_k\|^2$$

where $r_{nk}\in\{0,1\}$ is a 1-of-K assignment indicator. The algorithm alternates between an **E step** — assigning each point to its nearest centre $r_{nk}=1$ iff $k=\arg\min_j\|\mathbf{x}_n-\boldsymbol{\mu}_j\|^2$ — and an **M step** — updating each centre to the mean of assigned points $\boldsymbol{\mu}_k = (\sum_n r_{nk}\mathbf{x}_n)/(\sum_n r_{nk})$. Monotone decrease of $J$ guarantees convergence to a local minimum in a finite number of iterations (because there are finitely many hard assignments).

Intuition: iteratively perform the best hard cluster assignment given fixed centres, then the best centre positions given fixed assignments.

### Why it matters
K-means is a foundational non-probabilistic clustering algorithm and the canonical example of coordinate-descent / alternating optimisation. It also corresponds to the $\epsilon\to 0$ limit of EM applied to isotropic Gaussian mixtures, linking it directly to the probabilistic framework. It is widely used for initialising Gaussian mixture models before EM and for lossy data compression (vector quantisation).

### Variants and limitations
K-medoids generalises the distortion measure to any $\mathcal{V}(\mathbf{x},\mathbf{x}')$; an online (Robbins–Monro) version gives sequential updates $\boldsymbol{\mu}_k^{\text{new}}=\boldsymbol{\mu}_k^{\text{old}}+\eta_n(\mathbf{x}_n-\boldsymbol{\mu}_k^{\text{old}})$. Hard assignments make the algorithm sensitive to outliers and unable to represent cluster uncertainty.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cluster-dissimilarity-measures]] — uses
- [[k-means-as-em-limit]] — instantiates
- [[vector-quantization]] — applies: K-means minimises the VQ distortion measure
- [[em-algorithm]] — specializes: K-means E/M steps correspond to hard-assignment limit of EM E/M steps
- [[gaussian-mixture-models]] — specializes: K-means is the hard-assignment, zero-temperature limit of EM for isotropic Gaussian mixtures
- [[clustering]] — instantiates
[To be populated during integration]