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
- bayesian-stats
- information-theory
id: pkis:technique:junction-tree-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch26
tags:
- exact-inference
- marginalization
- graphical-models
- treewidth
- cycles
title: Junction Tree Algorithm
understanding: 0
---

## Definition
The junction tree algorithm is the standard *exact* method for marginalization on graphical models that contain cycles. Because the sum-product algorithm is only guaranteed correct on trees, the junction tree algorithm first transforms a loopy graph into a tree of **clusters**: variables are agglomerated together until the resulting cluster graph (the junction tree) has no cycles, after which a sum-product-style two-pass message schedule over the clusters computes exact marginals.

The price of exactness is that each message is a function over a whole cluster of variables, so the work and storage grow exponentially in the size of the largest cluster:
$$\text{cost} \sim O\big(\,|\mathcal{X}|^{\,w+1}\,\big),$$
where $w$ (one less than the largest cluster) is the **treewidth** of the graph.

### When it is tractable
For graphs of bounded treewidth (chains, polytrees, thin grids) the junction tree algorithm is efficient and exact. For densely connected graphs the maximal clusters become huge and the method is intractable, motivating approximate alternatives such as loopy belief propagation, Monte Carlo, and variational methods.

### Why it matters
It delineates the boundary between exact and approximate inference: marginalization on a graph with cycles is exactly solvable, but only at a cost set by the graph's treewidth. References: Lauritzen (1996); Jordan (1998).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]