---
title: "Multi-Hop Reasoning"
knowledge_type: concept
also_type: []
domain: [knowledge-representation, symbolic-subsymbolic]
tags: [knowledge-graphs, inference, graph-theory, question-answering]
related_concepts: [knowledge-graph, graph-rag, directed-graphical-models]
sources: ["[[zhang-graphrag-survey]]", "[[cheng-cograg]]", "[[liu-symagent]]", "[[hamilton-graphsage]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: evolving
---

The capacity to answer a query by traversing multiple edges across entities in a knowledge graph — inferring a relationship between A and D by chaining through intermediate nodes B and C — as opposed to single-step fact retrieval from an anchor entity.

## Reading Path
- [[zhang-graphrag-survey]] (unread) — multi-hop reasoning as the core motivation for GraphRAG over flat RAG
- [[cheng-cograg]] (unread) — mind-map decomposition explicitly structures multi-hop chains as hierarchical sub-question trees
- [[liu-symagent]] (unread) — symbolic rules as first-order logic chains; multi-hop reasoning structured by KG relational path induction
- [[hamilton-graphsage]] (unread) — K-layer neighborhood aggregation captures K-hop structural context; theoretical analysis via Weisfeiler-Lehman
