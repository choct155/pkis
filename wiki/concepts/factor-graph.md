---
aliases: []
also_type: []
analogous-to:
- directed-graphical-models
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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- information-theory
id: pkis:concept:factor-graph
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- sum-product-algorithm
related_concepts: []
sources:
- mackay-itila-ch26
specializes:
- undirected-graphical-models
tags:
- graphical-models
- factorization
- marginalization
- bipartite-graph
- message-passing
title: Factor Graph
understanding: 0
---

## Definition
A factor graph is a bipartite graphical representation of a function that factorizes as a product of local factors,
$$P^*(\mathbf{x}) = \prod_{m=1}^{M} f_m(\mathbf{x}_m),$$
where each factor $f_m$ depends only on a subset $\mathbf{x}_m$ of the variables. The graph has two kinds of node: **variable nodes** (circles) for each $x_n$ and **factor nodes** (squares) for each $f_m$. An edge joins variable node $n$ to factor node $m$ iff $f_m$ depends on $x_n$. Writing $N(m)$ for the indices of variables in factor $m$ and $M(n)$ for the factors containing variable $n$ recovers the graph adjacency.

The normalized distribution is $P(\mathbf{x}) = \frac{1}{Z}\prod_m f_m(\mathbf{x}_m)$ with $Z = \sum_{\mathbf{x}}\prod_m f_m(\mathbf{x}_m)$.

### Relation to other graphical models
Factor graphs make the factorization *explicit and unambiguous*. A directed model's conditional $P(x_n\mid \mathrm{pa}(x_n))$ becomes one factor; an undirected model's clique potential becomes one factor. Unlike a Markov network, two different factorizations over the same clique structure yield distinct factor graphs, so the representation is strictly finer-grained.

### Why it matters
The factor graph is the data structure on which the sum-product algorithm runs: exact marginalization and normalization are linear-time when the graph is a tree, but the same local message rules can be applied ("loopily") to graphs with cycles, which is the basis of modern sparse-graph (e.g. LDPC) decoding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[directed-graphical-models]] — analogous-to: Each directed conditional P(x|pa(x)) maps to a single factor node, giving a unified factorization representation.
- [[undirected-graphical-models]] — specializes: A factor graph is a finer-grained factorization view; clique potentials of an undirected model map to factor nodes.
- [[sum-product-algorithm]] — prerequisite-of: The sum-product algorithm runs on a factor graph; the bipartite structure defines the message-passing edges.
[To be populated during integration]