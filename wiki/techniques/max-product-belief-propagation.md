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
- machine-learning
id: pkis:technique:max-product-belief-propagation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch09
tags:
- MAP-inference
- belief-propagation
- message-passing
- max-marginals
- MPE
title: Max-Product Belief Propagation
understanding: 0
---

## Definition
Replace the summation in the sum-product algorithm with a maximisation:

$$m_{s \to t}(z_t) = \max_{z_s} \psi_{st}(z_s, z_t)\,\psi_s(z_s)\prod_{u \in \text{nbrs}(s)\setminus t} m_{u \to s}(z_s)$$

The resulting **max-marginals** are $\zeta_i(k) = \max_{z_{-i}} p(z_i=k, z_{-i}\mid y)$. On a tree, the MMM estimate $\tilde{z}_i = \arg\max_k \zeta_i(k)$ recovers the global MAP estimate $z^* = \arg\max_z p(z\mid y)$ when max-marginals are unique.

Intuition: substitute max for sum so that each message tracks the maximum probability achievable in the sub-graph rather than the sum.

### Why it matters
Max-product BP generalises the Viterbi algorithm from chains to general (tree-structured) graphs. It is used in energy minimisation, stereo vision, and LDPC decoding. Importantly, it contrasts with the MPM (posterior-marginal) estimator: MAP/MMM minimises sequence (word) error while MPM minimises per-node (bit) error. On graphs with cycles it becomes loopy max-product BP, which is exact for graphs with a single loop.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]