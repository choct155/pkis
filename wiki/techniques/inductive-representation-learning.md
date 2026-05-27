---
id: "pkis:technique:inductive-representation-learning"
aliases: []
title: "Inductive Representation Learning"
knowledge_type: technique
also_type: []
domain: [deep-learning, knowledge-representation]
tags: [graph-theory, node-embedding, generalization, unseen-nodes, neighborhood-aggregation]
related_concepts: [node-embedding, graph-neural-networks, graph-sage]
sources: ["[[hamilton-graphsage]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

A class of node embedding approaches that learn generalizable aggregation functions over node neighborhoods, enabling embedding generation for previously unseen nodes at inference time without retraining — contrasting with transductive methods that embed only nodes present at training.

## Reading Path
- [[hamilton-graphsage]] (unread) — primary treatment; GraphSAGE as the foundational inductive framework, with formal definition, aggregator variants, and theoretical analysis of expressive capability
