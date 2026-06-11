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
- machine-learning
- unsupervised-learning
id: pkis:concept:bernoulli-mixture-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch28
tags:
- binary-data
- mixture-model
- em-algorithm
- unsupervised-clustering
title: Bernoulli Mixture Model (BMM)
understanding: 0
---

## Definition
$$p(x \mid z = k, \theta) = \prod_{d=1}^D \text{Ber}(x_d \mid \mu_{dk}) = \prod_{d=1}^D \mu_{dk}^{x_d}(1-\mu_{dk})^{1-x_d}$$

A Bernoulli mixture model is a mixture model for binary-valued $D$-dimensional data $x \in \{0,1\}^D$, where each mixture component $k$ is parameterised by a vector of independent Bernoulli probabilities $\mu_{\cdot k} \in [0,1]^D$. The parameter $\mu_{dk}$ represents the probability that feature $d$ is active in cluster $k$.

### Why it matters
BMMs are the natural counterpart of GMMs for binary data such as binarised images, document term vectors, or genomic presence/absence data. Fitting by EM is straightforward, and the learned $\mu_k$ vectors can be visualised as prototype images, enabling unsupervised discovery of categories (e.g., digit classes in MNIST) without labels.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]