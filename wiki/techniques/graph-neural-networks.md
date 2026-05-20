---
title: "Graph Neural Networks"
knowledge_type: technique
also_type: []
domain: [deep-learning, knowledge-representation]
tags: [graph-theory, message-passing, node-classification, link-prediction, embeddings]
related_concepts: [neural-networks, knowledge-graph, graph-rag]
sources: ["[[zhang-graphrag-survey]]", "[[hamilton-graphsage]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A class of neural networks that operates on graph-structured data by iteratively aggregating information from each node's neighbors (message-passing), producing node embeddings that encode both semantic features and structural position; used in GraphRAG as retrieval encoders that score node relevance jointly on content and graph topology.

## Reading Path
- [[zhang-graphrag-survey]] (unread) — GNNs as retrieval encoders in GraphRAG; message-passing in context of knowledge graph indexing
- [[hamilton-graphsage]] (unread) — GraphSAGE: foundational inductive GNN with sampled neighborhood aggregation; three aggregator architectures and theoretical analysis
