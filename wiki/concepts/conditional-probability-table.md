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
- probability-theory
id: pkis:concept:conditional-probability-table
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch04
tags:
- discrete-Bayes-net
- parameter-learning
- row-stochastic
- Dirichlet-prior
title: Conditional Probability Table (CPT)
understanding: 0
---

## Definition
$$\theta_{ijk} \triangleq p(x_i = k \mid x_{\text{pa}(i)} = j), \quad 0 \le \theta_{ijk} \le 1, \quad \sum_{k=1}^{K_i} \theta_{ijk} = 1 \;\forall j$$

A CPT is a row-stochastic matrix that encodes the discrete CPD for node $i$ in a Bayesian network, with one categorical distribution per joint parent configuration $j$.

### Why it matters
CPTs are the canonical parametric form for discrete Bayesian networks. Parameter count is $O(K^{p+1})$ for $p$ parents and $K$ states, making sparsity essential. MLE reduces to normalized empirical counts $\hat{\theta}_{ijk} = N_{ijk}/\sum_{k'} N_{ijk'}$, and the Bayesian posterior is conjugate under a Dirichlet prior: $\theta_{ij}\mid D \sim \text{Dir}(N_{ij}+\alpha_{ij})$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]