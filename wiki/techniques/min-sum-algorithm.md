---
aliases: []
also_type: []
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
- information-theory
- bayesian-stats
id: pkis:technique:min-sum-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch16
tags:
- message-passing
- shortest-path
- viterbi
- dynamic-programming
- decoding
title: Min-Sum (Viterbi) Algorithm
understanding: 0
---

## Definition
The min-sum algorithm (also called the Viterbi algorithm) finds the lowest-cost path through a weighted directed acyclic graph by message passing. Define the cost of a node $x$ as the cost of the cheapest path from the source $A$ to $x$. Each node, once it knows the costs of all predecessors, sets
$$c(x) = \min_{u \to x}\big(c(u) + w_{u\to x}\big),$$
taking the **min** over incoming edges and **summing** the edge weight onto the predecessor's cost. The algorithm records (and prunes to) the surviving edge that achieved the minimum; the optimal path is then recovered by **backtracking** the surviving edges from the sink. In MacKay's Ambridge-to-Bognor example the costs propagate from $A$ and reveal an optimal path of cost $6$ along $A$–$I$–$K$–$M$–$B$.

### Relation to sum-product
Min-sum is the sum-product algorithm with the semiring changed: $(+,\times)$ becomes $(\min,+)$. Where sum-product marginalizes over all configurations, min-sum reports the single best one — the same local message structure, optimizing instead of summing. (In probability terms, max-product/min-sum finds the most probable configuration rather than the marginals.)

### Why it matters
It solves shortest-path and critical-path problems in linear time without enumerating exponentially many routes, and it is the standard decoder for trellis-structured error-correcting and convolutional codes, where it identifies the most likely transmitted sequence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]