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
date_updated: '2026-06-20'
domain:
- probabilistic-graphical-models
- machine-learning
- statistics
id: pkis:concept:dag-factorization
instantiates:
- probabilistic-graphical-models
- directed-graphical-models
- bayesian-networks
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
- cunningham-causal-inference-mixtape-ch04
tags:
- Bayesian-network
- factorization
- conditional-independence
- DAG
- directed-graph
title: DAG Factorization (Directed Graphical Model)
understanding: 0
uses:
- conditional-independence
- product-rule
---

## Definition
$$p(\mathbf{x}) = \prod_{k=1}^{K} p(x_k \mid \text{pa}_k)$$
where $\text{pa}_k$ is the set of parent nodes of $x_k$ in a directed acyclic graph (DAG) over $K$ nodes.

Every joint distribution over a DAG factors into local conditional distributions, one per node, conditioned only on that node's graph-parents.

### Why it matters
This single equation is the foundation of Bayesian networks. It (i) encodes conditional independence structure graphically, (ii) reduces the number of free parameters when the graph is sparse, (iii) provides a normalised joint distribution automatically (since each factor is a normalised conditional), and (iv) permits efficient exact inference via message-passing on trees. The fully-connected graph recovers the chain rule without any independence assumptions, while sparser graphs encode progressively stronger independence constraints.

### Parameter count
For $M$ binary nodes with at most $p$ parents each, the naive $2^M - 1$ parameters reduce to at most $M \cdot 2^p$, an exponential saving in $M$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-networks]] — instantiates
- [[product-rule]] — uses
- [[conditional-independence]] — uses
- [[directed-graphical-models]] — instantiates
- [[probabilistic-graphical-models]] — instantiates
[To be populated during integration]