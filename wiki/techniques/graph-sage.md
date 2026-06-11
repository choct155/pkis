---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- deep-learning
- knowledge-representation
id: pkis:technique:graph-sage
knowledge_type: technique
maturity: settled
related_concepts:
- node-embedding
- graph-neural-networks
- inductive-representation-learning
sources:
- '[[hamilton-graphsage]]'
specializes:
- message-passing-neural-networks
tags:
- graph-theory
- node-embedding
- neighborhood-aggregation
- gnn
- inductive-learning
- node-classification
title: GraphSAGE (Sample and Aggregate)
understanding: 0
uses:
- transductive-vs-inductive-graph-learning
---

An inductive node embedding algorithm (GraphSAGE = SAmple and aggreGatE) that learns aggregation functions over fixed-size uniformly sampled local neighborhoods, iterating K depth layers to produce node representations for both seen and unseen nodes at inference time.

## Reading Path
- [[hamilton-graphsage]] (unread) — the defining paper; introduces the algorithm, three aggregator architectures (mean/LSTM/pooling), unsupervised and supervised training variants, and theoretical analysis via Weisfeiler-Lehman connection

## Connections
- [[transductive-vs-inductive-graph-learning]] — uses
- [[message-passing-neural-networks]] — specializes