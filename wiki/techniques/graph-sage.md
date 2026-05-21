---
title: "GraphSAGE (Sample and Aggregate)"
knowledge_type: technique
also_type: []
domain: [deep-learning, knowledge-representation]
tags: [graph-theory, node-embedding, neighborhood-aggregation, gnn, inductive-learning, node-classification]
related_concepts: [node-embedding, graph-neural-networks, inductive-representation-learning]
sources: ["[[hamilton-graphsage]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

An inductive node embedding algorithm (GraphSAGE = SAmple and aggreGatE) that learns aggregation functions over fixed-size uniformly sampled local neighborhoods, iterating K depth layers to produce node representations for both seen and unseen nodes at inference time.

## Reading Path
- [[hamilton-graphsage]] (unread) — the defining paper; introduces the algorithm, three aggregator architectures (mean/LSTM/pooling), unsupervised and supervised training variants, and theoretical analysis via Weisfeiler-Lehman connection
