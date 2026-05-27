---
id: "pkis:technique:graph-neural-networks"
aliases: []
title: "Graph Neural Networks"
knowledge_type: technique
also_type: []
domain: [deep-learning, knowledge-representation]
tags: [graph-theory, message-passing, node-classification, link-prediction, embeddings]
related_concepts: [neural-networks, knowledge-graph, graph-rag]
sources: ["[[zhang-graphrag-survey]]", "[[hamilton-graphsage]]", "[[lamb-gnn-neural-symbolic-2020]]", "[[delong-nsai-kg-survey-2024]]", "[[wan-cognitive-ai-nsai-survey-2023]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 5
understanding: 0
maturity: settled
---

A class of neural networks that operates on graph-structured data by iteratively aggregating information from each node's neighbors (message-passing), producing node embeddings that encode both semantic features and structural position; used in GraphRAG as retrieval encoders that score node relevance jointly on content and graph topology.

## Reading Path
- [[zhang-graphrag-survey]] (unread) — GNNs as retrieval encoders in GraphRAG; message-passing in context of knowledge graph indexing
- [[hamilton-graphsage]] (unread) — GraphSAGE: foundational inductive GNN with sampled neighborhood aggregation; three aggregator architectures and theoretical analysis
- [[lamb-gnn-neural-symbolic-2020]] (unread) — GNNs as natural neural-symbolic models (Type 1 Kautz); GCN/GAT architecture; attention as symbolic bridge; combinatorial optimization applications
- [[delong-nsai-kg-survey-2024]] (unread) — GNNs (GCN, R-GCN, GAT) as dominant neural encoder for KG neurosymbolic systems; role in logically-informed and constrained embedding approaches
- [[wan-cognitive-ai-nsai-survey-2023]] (unread) — GNN+attention classified as Neuro[Symbolic] (Type 6); SpMM and SDDMM as key compute operators
