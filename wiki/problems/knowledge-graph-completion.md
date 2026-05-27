---
id: "pkis:problem:knowledge-graph-completion"
aliases: []
title: "Knowledge Graph Completion"
knowledge_type: problem
also_type: []
domain: [knowledge-representation, deep-learning]
tags: [knowledge-graphs, link-prediction, relation-prediction, embeddings, neurosymbolic, missing-data]
related_concepts: [knowledge-graph, graph-neural-networks, knowledge-graph-embedding, inductive-logic-programming, markov-logic-networks]
sources: ["[[delong-nsai-kg-survey-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Knowledge Graph Completion (KGC) is the problem of inferring missing facts in a knowledge graph — where the graph's inherent incompleteness (due to the open-world nature of human knowledge) requires predicting new entity-relation-entity triples from observed graph structure; primary subtasks are link prediction (does an edge exist between u and v?) and relation prediction (what relation type connects u and v?), with applications in drug discovery, social network analysis, and biomedical knowledge bases.

## Reading Path
- [[delong-nsai-kg-survey-2024]] (unread) — comprehensive survey of neurosymbolic KGC methods across three taxonomic categories; benchmarks including YAGO, DBpedia, Gene Ontology
