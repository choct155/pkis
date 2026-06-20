---
aliases: []
also_type: []
coverage: 4
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:concept:multi-hop-reasoning
knowledge_type: concept
maturity: evolving
related_concepts:
- knowledge-graph
- graph-rag
- directed-graphical-models
sources:
- '[[zhang-graphrag-survey]]'
- '[[cheng-cograg]]'
- '[[liu-symagent]]'
- '[[hamilton-graphsage]]'
- 2307-07697-think-on-graph-deep
- ho-constructing-2020
- share-thinkongraph
- talmor-the-2018
- yang-hotpotqa-2018
- zhang-variational-2018
- gulli-agentic-design-patterns-ch17
tags:
- knowledge-graphs
- inference
- graph-theory
- question-answering
title: Multi-Hop Reasoning
understanding: 0
---

The capacity to answer a query by traversing multiple edges across entities in a knowledge graph — inferring a relationship between A and D by chaining through intermediate nodes B and C — as opposed to single-step fact retrieval from an anchor entity.

## Reading Path
- [[zhang-graphrag-survey]] (unread) — multi-hop reasoning as the core motivation for GraphRAG over flat RAG
- [[cheng-cograg]] (unread) — mind-map decomposition explicitly structures multi-hop chains as hierarchical sub-question trees
- [[liu-symagent]] (unread) — symbolic rules as first-order logic chains; multi-hop reasoning structured by KG relational path induction
- [[hamilton-graphsage]] (unread) — K-layer neighborhood aggregation captures K-hop structural context; theoretical analysis via Weisfeiler-Lehman