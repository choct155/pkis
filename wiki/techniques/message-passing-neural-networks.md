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
generalizes:
- graph-sage
- graph-convolutional-network
- graph-attention-network
id: pkis:technique:message-passing-neural-networks
instantiates:
- graph-encoder-decoder-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
specializes:
- graph-neural-networks
tags:
- GNN
- message-passing
- neighbourhood-aggregation
- graph-convolution
- inductive
title: Message Passing Neural Networks (MPNN)
understanding: 0
---

## Definition
At each layer $\ell$ of an MPNN, every node $i$ aggregates messages from its graph-neighbours:
$$\mathbf{m}^{\ell+1}_i = \sum_{j \mid (v_i,v_j)\in E} f^\ell(\mathbf{H}^\ell_i, \mathbf{H}^\ell_j)$$
$$\mathbf{H}^{\ell+1}_i = h^\ell(\mathbf{H}^\ell_i,\, \mathbf{m}^{\ell+1}_i)$$
with $\mathbf{H}^0 = \mathbf{X}$. After $L$ layers, each node's hidden state encodes information from its $L$-hop neighbourhood.

The framework (Gilmer et al. 2017) subsumes many GNN variants — including GCN, GraphSAGE, GAT, and the original GNN — by varying the message function $f^\ell$ and update function $h^\ell$.

### Why it matters
MPNN provides the canonical abstraction for supervised graph learning: it couples local neighbourhood aggregation with learnable parameters to produce task-specific node/graph representations. It is inductive (parameters are shared across nodes and graphs) and its depth controls the receptive field. GraphNet (Battaglia et al. 2018) further extends MPNN to explicitly represent edges and global graph state.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[graph-attention-network]] — generalizes
- [[graph-convolutional-network]] — generalizes
- [[graph-sage]] — generalizes
- [[graph-encoder-decoder-model]] — instantiates
- [[graph-neural-networks]] — specializes
[To be populated during integration]