---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
- deep-learning
id: pkis:technique:knowledge-graph-embedding
knowledge_type: technique
maturity: settled
related_concepts:
- knowledge-graph
- knowledge-graph-completion
- graph-neural-networks
- node-embedding
sources:
- '[[delong-nsai-kg-survey-2024]]'
- '[[sheth-neurosymbolic-why-2023]]'
- cetoli-named-2018
tags:
- knowledge-graphs
- embeddings
- link-prediction
- translational-models
- tensor-decomposition
- representation-learning
title: Knowledge Graph Embedding
understanding: 0
---

Knowledge Graph Embedding (KGE) methods represent KG entities and relations as dense low-dimensional vectors such that proximity in the embedding space approximates semantic similarity in the KG; major families include translational models (TransE: relation as translation), bilinear models (DistMult, ComplEx: relation as diagonal/complex matrix), and GNN-based encoders (R-GCN, GAT) with a decoder that scores triples.

## Reading Path
- [[delong-nsai-kg-survey-2024]] (unread) — KGE as the neural component in logically-informed and constrained embedding approaches; TransE, DistMult, ComplEx, RESCAL, DeepWalk, node2vec comparisons
- [[sheth-neurosymbolic-why-2023]] (unread) — KGE as "lowering" approach: compressing knowledge graph structure for neural integration