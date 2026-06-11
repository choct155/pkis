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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
- information-theory
id: pkis:technique:sum-product-algorithm-trees
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch09
tags:
- belief-propagation
- tree-inference
- message-passing
- marginal-inference
title: Sum-Product Algorithm on Trees
understanding: 0
---

## Definition
For a pairwise undirected tree with node potentials $\psi_s(z_s)$ and edge potentials $\psi_{st}(z_s, z_t)$, messages are passed in two sweeps—leaves to root then root to leaves:

$$m_{s \to t}(z_t) = \sum_{z_s} \psi_{st}(z_s, z_t)\,\text{bel}_s(z_s) \bigg/ m_{t \to s}(z_s)$$

$$\text{bel}_s(z_s) \propto \psi_s(z_s)\prod_{t \in \text{nbrs}(s)} m_{t \to s}(z_s)$$

After both sweeps every node holds the exact posterior marginal $p(z_s \mid y)$.

Intuition: each node collects evidence from all branches, the root sees everything, then redistributes information back to the leaves—analogous to the forwards-backwards algorithm on a chain.

### Why it matters
The sum-product algorithm is the general tree-structured instance of belief propagation that subsumes forwards-backwards (chains) and Kalman smoothing (linear-Gaussian chains). It computes all marginals in a single upward and downward pass with time linear in the number of edges. It also forms the theoretical foundation for loopy belief propagation and the junction tree algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]