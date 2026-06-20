---
aliases: []
also_type: []
applies:
- clustering
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- machine-learning
- statistics
generalizes:
- mixture-models
- gaussian-mixture-models
id: pkis:framework:dirichlet-process-mixture-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
- gelman-bda3-ch23
tags:
- mixture-model
- clustering
- dirichlet-process
- chinese-restaurant-process
- infinite-mixture
- nonparametric-bayes
title: Dirichlet Process Mixture Model
understanding: 0
uses:
- dirichlet-process
- chinese-restaurant-process
---

## Definition
A Dirichlet Process Mixture Model (DPMM) is an infinite mixture model in which the mixing measure $G$ is drawn from a Dirichlet process:
$$
G \sim \mathrm{DP}(\alpha, H), \quad \theta_i \mid G \sim G, \quad x_i \mid \theta_i \sim F(\cdot \mid \theta_i).
$$
Marginalising over $G$ yields the Chinese Restaurant Process (CRP) prior on partitions: the $n$-th observation joins cluster $k$ with probability proportional to its current size $n_k$, or starts a new cluster with probability proportional to $\alpha$.

The number of occupied clusters grows as $O(\alpha \log n)$, adapting to the data.

### Why it matters
DPMMs are the workhorse Bayesian nonparametric clustering model. They subsume finite Gaussian mixture models as a special (truncated) case and support posterior inference about the number of clusters without explicit model comparison.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[clustering]] — applies
- [[gaussian-mixture-models]] — generalizes
- [[mixture-models]] — generalizes
- [[chinese-restaurant-process]] — uses
- [[dirichlet-process]] — uses
[To be populated during integration]