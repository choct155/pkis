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
- machine-learning
- graph-learning
- deep-learning
id: pkis:technique:graph-attention-network
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- attention
- GAT
- inductive
- neighbourhood-aggregation
- graph-convolution
title: Graph Attention Network (GAT)
understanding: 0
---

## Definition
At each GAT layer, the aggregated message for node $i$ is a softmax-normalised weighted sum over neighbours:
$$\mathbf{H}^{\ell+1}_i = \sigma\!\left(\sum_{j \in \mathcal{N}(i)} \alpha_{ij}\, \mathbf{W}^\ell \mathbf{H}^\ell_j\right)$$
where the attention coefficients $\alpha_{ij} = \frac{\exp(e_{ij})}{\sum_{k \in \mathcal{N}(i)}\exp(e_{ik})}$ are computed from a learned scoring function $e_{ij} = a(\mathbf{W}^\ell \mathbf{H}^\ell_i, \mathbf{W}^\ell \mathbf{H}^\ell_j)$ (Veličković et al. 2018).

GAT replaces the fixed graph-structure weights of GCN with learnable, content-dependent attention scores, allowing each node to selectively weight its neighbours.

### Why it matters
GAT is suitable for both transductive and inductive settings. Unlike GraphSAGE it attends over all neighbours rather than a fixed sample, and unlike GCN the weights are not determined solely by node degree. Multi-head attention further improves stability. GAT has become a standard component in graph learning pipelines for node classification and link prediction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]