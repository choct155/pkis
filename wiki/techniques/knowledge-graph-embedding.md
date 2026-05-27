---
id: "pkis:technique:knowledge-graph-embedding"
aliases: []
title: "Knowledge Graph Embedding"
knowledge_type: technique
also_type: []
domain: [knowledge-representation, deep-learning]
tags: [knowledge-graphs, embeddings, link-prediction, translational-models, tensor-decomposition, representation-learning]
related_concepts: [knowledge-graph, knowledge-graph-completion, graph-neural-networks, node-embedding]
sources: ["[[delong-nsai-kg-survey-2024]]", "[[sheth-neurosymbolic-why-2023]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Knowledge Graph Embedding (KGE) methods represent KG entities and relations as dense low-dimensional vectors such that proximity in the embedding space approximates semantic similarity in the KG; major families include translational models (TransE: relation as translation), bilinear models (DistMult, ComplEx: relation as diagonal/complex matrix), and GNN-based encoders (R-GCN, GAT) with a decoder that scores triples.

## Reading Path
- [[delong-nsai-kg-survey-2024]] (unread) — KGE as the neural component in logically-informed and constrained embedding approaches; TransE, DistMult, ComplEx, RESCAL, DeepWalk, node2vec comparisons
- [[sheth-neurosymbolic-why-2023]] (unread) — KGE as "lowering" approach: compressing knowledge graph structure for neural integration
