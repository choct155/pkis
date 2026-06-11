---
aliases: []
also_type: []
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
- probabilistic-graphical-models
- machine-learning
- statistics
generalizes:
- multivariate-normal-model
- factor-analysis
- kalman-filter
id: pkis:concept:linear-gaussian-graphical-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
specializes:
- dag-factorization
tags:
- Gaussian
- DAG
- factor-analysis
- Kalman-filter
- covariance-structure
title: Linear-Gaussian Graphical Model
understanding: 0
uses:
- gaussian-distribution
- sum-product-algorithm
---

## Definition
A **linear-Gaussian graphical model** over a DAG assigns each node $x_i$ a Gaussian conditional distribution whose mean is a linear function of its parents:
$$p(x_i \mid \text{pa}_i) = \mathcal{N}\!\left(x_i \,\Big|\, \sum_{j \in \text{pa}_i} w_{ij} x_j + b_i,\; v_i\right)$$
The joint distribution $p(\mathbf{x})$ is multivariate Gaussian with mean and covariance computable by topological recursions:
$$\mathbb{E}[x_i] = \sum_{j \in \text{pa}_i} w_{ij}\mathbb{E}[x_j] + b_i$$
$$\text{cov}[x_i, x_j] = \sum_{k \in \text{pa}_j} w_{jk}\,\text{cov}[x_i, x_k] + I_{ij} v_j$$

Intermediate graph structures yield multivariate Gaussians with partially constrained covariance matrices—interpolating between fully independent ($\Sigma = \text{diag}$) and fully correlated (general $\Sigma$).

### Why it matters
Linear-Gaussian DAGs unify probabilistic PCA, factor analysis, Kalman filters, and linear dynamical systems under a single graphical framework. The recursions allow exact computation of the Gaussian parameters from the local weights, and the sum-product algorithm on such graphs is equivalent to Kalman smoothing. Parameter count for a fully connected $D$-node graph is $D(D+1)/2$, matching a general symmetric covariance matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sum-product-algorithm]] — uses
- [[kalman-filter]] — generalizes
- [[factor-analysis]] — generalizes
- [[multivariate-normal-model]] — generalizes
- [[gaussian-distribution]] — uses
- [[dag-factorization]] — specializes
[To be populated during integration]