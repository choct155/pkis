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
- network-science
- machine-learning
id: pkis:concept:community-detection
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
specializes:
- clustering
tags:
- graph-clustering
- modularity
- social-networks
- latent-variable
- network-science
title: Community Detection
understanding: 0
uses:
- stochastic-block-model
---

## Definition
Community detection is the task of partitioning the nodes $V$ of a graph $G=(V,E)$ into $K$ groups (communities) such that intra-community edge density is high and inter-community edge density is low:

$$\max_{z: V \to [K]} \; Q(z, G) = \frac{1}{2|E|} \sum_{ij} \left(A_{ij} - \frac{d_i d_j}{2|E|}\right) \mathbf{1}[z_i = z_j]$$

where $Q$ is the **modularity** objective, $d_i$ is the degree of node $i$, and $A$ is the adjacency matrix.

### Why it matters
Community detection is the graph-domain analogue of clustering and underlies applications in social network analysis (friend groups), bioinformatics (functional protein modules), and epidemiology (disease transmission clusters). Generative approaches (SBM) provide principled statistical inference and model selection, while modularity maximisation offers fast heuristics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stochastic-block-model]] — uses
- [[clustering]] — specializes
[To be populated during integration]