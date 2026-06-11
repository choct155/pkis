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
- variational-inference
generalizes:
- loopy-belief-propagation
id: pkis:technique:generalised-belief-propagation
instantiates:
- variational-inference
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch09
specializes:
- junction-tree-algorithm
tags:
- Bethe-approximation
- cluster-variational-method
- region-graph
- approximate-inference
- treewidth
title: Generalised Belief Propagation (Cluster Variational Method)
understanding: 0
uses:
- variational-free-energy
---

## Definition
Improve LBP by clustering tightly-looped nodes into **hyper-edges** and running belief propagation on the resulting hyper-graph (represented as a partially-ordered set / region graph):

$$p^*(z) \approx \frac{\prod_{R \in \mathcal{F}} b_R(z_R)^{c_R}}{\prod_{R \in \mathcal{F}} \prod_{R' \subset R, R' \in \mathcal{F}} b_{R'}(z_{R'})^{c_{R'}}}$$

where $c_R$ are Möbius coefficients (counting numbers) chosen so that each variable and edge is counted exactly once. The special case of singleton nodes and pairwise edges reduces to standard LBP (Bethe approximation). Expanding hyper-edges to the full treewidth gives exact inference.

Intuition: group short loops into clusters so that inter-cluster messages remain on an acyclic hyper-graph.

### Why it matters
Generalised BP (Yedidia, Freeman & Weiss, 2000) provides a systematic hierarchy of approximations between LBP and exact junction-tree inference. It yields more accurate marginals on graphs with short, dense loops by explicitly representing within-cluster correlations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variational-free-energy]] — uses
- [[variational-inference]] — instantiates
- [[junction-tree-algorithm]] — specializes: when hyper-edges cover full treewidth, equals junction tree
- [[loopy-belief-propagation]] — generalizes
[To be populated during integration]