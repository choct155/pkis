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
id: pkis:technique:shallow-graph-embeddings
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- graph-embeddings
- transductive
- lookup-table
- DeepWalk
- node2vec
title: Shallow Graph Embeddings
understanding: 0
---

## Definition
$$\mathbf{Z} = \text{ENC}(\Theta^E) \triangleq \Theta^E \in \mathbb{R}^{N \times L}$$

The encoder is a simple lookup table: each node $v_i$ is assigned a learnable embedding vector $\mathbf{Z}_i \in \mathbb{R}^L$ directly as a model parameter, without any function of node features. The embedding matrix is optimised to reconstruct graph structure (unsupervised) or predict labels (supervised).

### Why it matters
Shallow embeddings are the simplest GRL methods and include influential algorithms such as DeepWalk, node2vec, LINE, and GraRep. They are transductive — the embedding dictionary cannot naturally generalise to nodes unseen during training — but they are computationally cheap and serve as strong baselines. Their relationship to matrix factorisation (NetMF) reveals that skip-gram random-walk methods implicitly factorise a smoothed powers-of-adjacency matrix.

### Limitations
Because node features $\mathbf{X}$ are not used in the encoder, shallow embeddings cannot leverage semantic attributes and cannot transfer across graphs in inductive settings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]