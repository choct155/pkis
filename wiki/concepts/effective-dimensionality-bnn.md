---
aliases: []
also_type: []
analogous-to:
- effective-number-of-parameters
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
- deep-learning
- bayesian-inference
- model-complexity
id: pkis:concept:effective-dimensionality-bnn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- Hessian-spectrum
- flat-minima
- compression
- generalisation
- model-complexity
title: Effective Dimensionality of a Neural Network
understanding: 0
uses:
- hessian-matrix
- low-rank-approximation
---

## Definition
$$N_{\text{eff}}(\mathbf{H}, c) = \sum_{i=1}^{k} \frac{\lambda_i}{\lambda_i + c}$$
where $\lambda_i$ are eigenvalues of the Hessian $\mathbf{H}$ at a local mode, and $c > 0$ is a regularisation constant.

Effective dimensionality counts the number of *well-determined* parameters: directions with $\lambda_i \gg c$ contribute nearly 1, while directions with $\lambda_i \ll c$ contribute nearly 0.

### Why it matters
Although modern DNNs have millions of nominal parameters, their effective dimension is typically far smaller. Flat minima have low effective dimension, enabling posterior inference in a low-dimensional subspace and significant model compression. Effective dimensionality closely tracks generalisation performance for CNNs with low training loss, and explains why deeper (but not necessarily wider) networks generalise better: depth provides hierarchical inductive bias that compresses data more efficiently.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[low-rank-approximation]] — uses
- [[effective-number-of-parameters]] — analogous-to
- [[hessian-matrix]] — uses
[To be populated during integration]