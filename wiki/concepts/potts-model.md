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
- statistical-physics
- probabilistic-graphical-models
- bioinformatics
id: pkis:concept:potts-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch04
tags:
- multi-label
- image-segmentation
- protein-structure
- energy-based-model
- DCA
title: Potts Model
understanding: 0
---

## Definition
A generalization of the Ising model to $K>2$ discrete states $x_i \in \{1,\ldots,K\}$, with energy
$$E(x) = -\sum_i\sum_k \alpha_k\,\mathbb{1}[x_i=k] - J\sum_{i\sim j}\mathbb{1}[x_i=x_j]$$
The pairwise potential rewards equal labels: $\psi_{ij}(x_i,x_j) = e^J$ if $x_i=x_j$, else $1$. Phase transition on a 2d lattice at $J_c = \log(1+\sqrt{K})$. Reduces to Ising when $K=2$ with $J_{\text{Potts}}=2J_{\text{Ising}}$.

The multi-label generalization of the Ising model, used for image segmentation and protein coevolution analysis.

### Why it matters
Potts models underlie direct coupling analysis (DCA) for protein contact-map prediction, a key step in structural bioinformatics. In computer vision they provide the standard smoothness prior for multi-label segmentation. The tractability of inference and the location of the phase transition are both well-characterized.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]