---
aliases: []
also_type: []
analogous-to:
- generative-adversarial-network
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
- self-supervised-learning
id: pkis:technique:deep-graph-infomax
instantiates:
- graph-encoder-decoder-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- contrastive-learning
- mutual-information
- self-supervised
- GNN
- graph-embeddings
- DGI
title: Deep Graph Infomax (DGI)
understanding: 0
uses:
- mutual-information
- graph-convolutional-network
---

## Definition
DGI (Veličković et al. 2019) trains a GNN encoder unsupervised by maximising a lower bound on the mutual information between node-level representations and a graph-level summary:
$$\min_\Theta -\mathbb{E}_{\mathbf{X},\mathbf{W}}\sum_{i}\log \mathcal{D}(Z_i, \mathcal{R}(\mathbf{Z})) - \mathbb{E}_{\mathbf{X}^-,\mathbf{W}^-}\sum_{j}\log(1 - \mathcal{D}(Z_j^-, \mathcal{R}(\mathbf{Z}^-)))$$
where $\mathcal{R}: \mathbb{R}^{N \times L}\to\mathbb{R}^L$ is a readout/pooling function, $\mathcal{D}$ is a discriminator, and negative samples $\mathbf{X}^-$ are row-wise random permutations of node features on the same graph.

DGI is a contrastive self-supervised method: it distinguishes real node–graph pairs from corrupted ones, forcing the encoder to capture global graph structure without labels.

### Why it matters
DGI achieves competitive or superior performance to supervised GCN on node classification using no labels, establishing contrastive learning as a powerful paradigm for graph self-supervision. It inspired subsequent contrastive graph methods (e.g. GraphCL, GMI) and the broader field of self-supervised graph representation learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[graph-convolutional-network]] — uses
- [[generative-adversarial-network]] — analogous-to
- [[mutual-information]] — uses
- [[graph-encoder-decoder-model]] — instantiates
[To be populated during integration]