---
id: "pkis:technique:graph-convolutional-networks"
aliases: []
title: "Graph Convolutional Networks"
knowledge_type: technique
also_type: []
domain: [deep-learning, knowledge-representation]
tags: [graph-neural-networks, message-passing, node-classification, spectral-convolution, adjacency-matrix]
related_concepts: [graph-neural-networks, message-passing-neural-networks, knowledge-graph-embedding, node-embedding]
sources: ["[[lamb-gnn-neural-symbolic-2020]]", "[[delong-nsai-kg-survey-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Graph Convolutional Networks (GCNs) generalize convolutional neural networks to non-Euclidean graph data by computing each node's updated representation as a normalized, degree-weighted linear transformation of its neighbors' representations: `x_i^(k+1) = σ( Σ_{j∈N(i)∪{i}} θ_k · x_j^(k) / √(deg(i)·deg(j)) )`; this can be written as `x^(k+1) = D̃^{-1/2} Ã D̃^{-1/2} x^(k) θ^(k)` where Ã = A + I.

## Reading Path
- [[lamb-gnn-neural-symbolic-2020]] (unread) — GCN as attention layer over non-Euclidean data; relationship to neural-symbolic computing
- [[delong-nsai-kg-survey-2024]] (unread) — GCN and variants (R-GCN, GAT) as neural encoders for KG embedding in neurosymbolic systems
