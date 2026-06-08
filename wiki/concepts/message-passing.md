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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
- bayesian-stats
id: pkis:concept:message-passing
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch16
tags:
- message-passing
- graph-theory
- distributed-computation
- dynamic-programming
- factorization
title: Message Passing
understanding: 0
---

## Definition
Message passing is a paradigm for computing a global function of many variables using only local communication between simple processors arranged on a graph. Each node holds local state, exchanges scalar (or vector) **messages** with its graph neighbours, and updates by combining incoming messages with its own data; after the messages have propagated, every node can read off the global answer from the messages it has received. MacKay's parable makes this concrete: a line of soldiers counts itself when each soldier sends 'one plus the number I was told' to the neighbour who has not yet spoken, so the global count emerges with no central tally.

### Separability is the enabling property
Message passing works precisely when the target function is **separable**: a quantity at a point (e.g. the total) decomposes into independent contributions from disjoint regions that the point separates. On a line or, more generally, a cycle-free graph (a **tree**), removing a node splits the rest into independent subtrees, so partial results can be merged. Functions lacking this structure — number of shared birthdays, largest equal-height group, the travelling-salesman tour — admit no such local decomposition.

### Why it matters
It converts seemingly global, combinatorially explosive computations (counting $\sim 2^{N/2}$ grid paths, lowest-cost routing, marginal inference) into linear-time passes over a graph, using only local memory and arithmetic. It is the common backbone of dynamic programming, the sum-product and min-sum algorithms, the forward-backward and Viterbi algorithms, and belief propagation — and underlies decoding of modern error-correcting codes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]