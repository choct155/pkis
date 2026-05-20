---
title: "Graph Retrieval-Augmented Generation"
knowledge_type: technique
also_type: [framework]
domain: [knowledge-representation, deep-learning, symbolic-subsymbolic]
tags: [rag, knowledge-graphs, llm, graph-theory, multi-hop, information-retrieval]
related_concepts: [retrieval-augmented-generation, knowledge-graph, multi-hop-reasoning, graph-neural-networks, knowledge-graph-construction, in-context-learning]
sources: ["[[zhang-graphrag-survey]]", "[[gulli-agentic-design-patterns]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: evolving
---

## Reading Path
- [[zhang-graphrag-survey]] (unread) — primary theoretical treatment; full taxonomy and retrieval technique survey
- [[gulli-agentic-design-patterns-ch14]] (unread) — practical coverage; GraphRAG within the agentic knowledge retrieval pattern

A specialization of RAG that replaces flat vector-database retrieval with graph-structured knowledge organization, enabling multi-hop reasoning, explicit entity-relation retrieval, and structure-aware knowledge integration into LLM generation.

Classification note: assigned as technique but also functions as framework — GraphRAG defines a paradigm (knowledge organization → graph retrieval → knowledge integration) organizing concepts, techniques, and results into a coherent architecture; the three-way taxonomy (knowledge-based, index-based, hybrid) further structures the design space.
