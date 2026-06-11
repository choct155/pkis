---
aliases: []
also_type: []
analogous-to:
- clustering
applies:
- community-detection
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
- machine-learning
- network-science
- statistics
id: pkis:concept:stochastic-block-model
instantiates:
- latent-variable-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
specializes:
- mixture-models
tags:
- community-detection
- latent-variable
- random-graph
- generative-model
title: Stochastic Block Model (SBM)
understanding: 0
---

## Definition
$$P(A_{ij}=1 \mid z_i, z_j) = B_{z_i z_j}$$

where $A$ is the adjacency matrix, $z_i \in \{1,\dots,K\}$ is the latent community label of node $i$, and $B \in [0,1]^{K \times K}$ is a block affinity matrix. Edges are drawn independently given community assignments.

The SBM is the canonical generative model for community structure in networks: nodes in the same block connect with probability $B_{kk}$ (usually high) and nodes in different blocks connect with probability $B_{kl}$ (usually low).

### Why it matters
The SBM is the workhorse latent variable model for graph clustering. It admits exact and approximate inference algorithms (variational EM, belief propagation, spectral methods) and has sharp phase-transition characterisations for community detectability. Extensions include the degree-corrected SBM and the mixed-membership SBM.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[latent-variable-models]] — instantiates
- [[clustering]] — analogous-to
- [[community-detection]] — applies
- [[mixture-models]] — specializes
[To be populated during integration]