---
title: "Retrieval-Augmented Generation"
knowledge_type: technique
also_type: [framework]
domain: [knowledge-representation, deep-learning]
tags: [llm, information-retrieval, rag, vector-databases]
related_concepts: [knowledge-graph, graph-rag]
sources: ["[[zhang-graphrag-survey]]", "[[gulli-agentic-design-patterns]]", "[[barron-legal-rag-nmf]]", "[[baldazzi-soft-ontological-reasoning]]", "[[cheng-cograg]]", "[[banf-tripartite-graphrag]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 6
understanding: 0
maturity: evolving
---

## Reading Path
- [[zhang-graphrag-survey]] (unread) — theoretical survey; covers knowledge-based, index-based, and hybrid RAG variants
- [[gulli-agentic-design-patterns-ch14]] (unread) — practical pattern treatment; covers standard RAG, GraphRAG, and Agentic RAG with code examples
- [[barron-legal-rag-nmf]] (unread) — legal domain; integrates VS, KG, and NMF retrieval; demonstrates RAG for reducing hallucinations in high-stakes legal QA
- [[baldazzi-soft-ontological-reasoning]] (unread) — RAG used to enrich LLM semantic unifier in soft chase for ontological reasoning
- [[cheng-cograg]] (unread) — KGQA application; graph-structured retrieval augmenting LLM reasoning with KG triples
- [[banf-tripartite-graphrag]] (unread) — tripartite GraphRAG with concept-anchored graph construction and MRF-based prompt assembly

A framework that enhances LLM generation by retrieving relevant content from an external knowledge base at inference time: the corpus is chunked, embedded, and indexed; at query time, the most similar chunks are retrieved and prepended to the LLM prompt, grounding the response in external knowledge without modifying model weights.

Classification note: assigned as technique but also functions as framework — RAG defines a three-stage pipeline (knowledge organization → retrieval → integration) that organizes multiple sub-techniques into a coherent system architecture.
