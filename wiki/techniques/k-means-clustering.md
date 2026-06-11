---
aliases: []
also_type: []
applies:
- prototype-methods
- vector-quantization-clustering
- number-of-components-selection
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:k-means-clustering
instantiates:
- clustering
- gaussian-mixture-models
- mixture-models
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- soft-k-means
related_concepts: []
sources:
- mackay-itila-ch20
specializes:
- gaussian-mixture-models
- em-algorithm
- clustering
- unsupervised-learning
tags:
- unsupervised-learning
- competitive-learning
- optimization
title: K-means Clustering
understanding: 0
uses:
- cluster-dissimilarity-measures
- k-means-plus-plus
- silhouette-coefficient
- spectral-clustering
- information-criteria
---

## Definition
An iterative algorithm that partitions $N$ points $\{\mathbf{x}^{(n)}\}$ in $\mathbb{R}^I$ into $K$ clusters, each parameterized by a mean $\mathbf{m}^{(k)}$. After initializing the means (e.g. randomly), it alternates two steps until assignments stop changing:

**Assignment step** — each point goes to its nearest mean, $\hat{k}^{(n)} = \operatorname{argmin}_k d(\mathbf{m}^{(k)}, \mathbf{x}^{(n)})$, encoded by hard responsibilities $r_k^{(n)} \in \{0,1\}$.

**Update step** — each mean is moved to the sample mean of the points it owns, $\mathbf{m}^{(k)} = \sum_n r_k^{(n)} \mathbf{x}^{(n)} / R(k)$ where $R(k) = \sum_n r_k^{(n)}$.

### Convergence
The algorithm always converges to a fixed point: the energy $\sum_n \beta\, d(\mathbf{x}^{(n)}, \mathbf{m}^{(\hat{k}^{(n)})})$ (springs connecting points to their means) is a Lyapunov function — both steps can only decrease it and it is bounded below.

### Failure modes
K-means represents only distances, never the weight or shape of a cluster. It thus misassigns points from a broad cluster to a nearby narrow one, slices elongated clusters in half, and — being a *hard* assignment — gives each borderline point full membership of exactly one cluster. The outcome also depends on initialization.

### Why it matters
K-means is the canonical competitive-learning clustering method and the hard-assignment limit of richer probabilistic models; its ad hoc choices (why the mean? which distance? which $K$?) motivate soft K-means and ultimately mixture models fit by EM.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[number-of-components-selection]] — applies: choosing K in K-means is an instance of the number-of-components-selection problem
- [[unsupervised-learning]] — specializes
- [[mixture-models]] — instantiates
- [[information-criteria]] — uses: BIC/WAIC on GMM used to choose K
- [[spectral-clustering]] — uses: K-means applied to eigenvector rows in the final step of spectral clustering
- [[silhouette-coefficient]] — uses: silhouette score used to choose K for K-means
- [[k-means-plus-plus]] — uses
- [[vector-quantization-clustering]] — applies
- [[gaussian-mixture-models]] — instantiates: K-means corresponds to a GMM with Sigma_k=I, pi_k=1/K, hard E-step
- [[clustering]] — specializes
- [[em-algorithm]] — specializes: K-means is the hard (σ²→0) limit of EM for a spherical Gaussian mixture
- [[cluster-dissimilarity-measures]] — uses: fixes the dissimilarity to squared Euclidean distance
- [[prototype-methods]] — applies: K-means within each class produces labeled prototypes for classification.
- [[gaussian-mixture-models]] — specializes: K-means is the hard-assignment, equal-weight, fixed-spherical-covariance limit of a Gaussian mixture.
- [[soft-k-means]] — prerequisite-of: Soft K-means generalizes the hard assignment of K-means via a stiffness-controlled softmax.
- [[clustering]] — instantiates: K-means is the canonical hard clustering algorithm.
[To be populated during integration]