---
title: "Retrieval-Augmented Generation"
knowledge_type: technique
also_type: [framework]
domain: [knowledge-representation, deep-learning]
tags: [llm, information-retrieval, rag, vector-databases]
related_concepts: [knowledge-graph, graph-rag]
sources: ["[[zhang-graphrag-survey]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

A framework that enhances LLM generation by retrieving relevant content from an external knowledge base at inference time: the corpus is chunked, embedded, and indexed; at query time, the most similar chunks are retrieved and prepended to the LLM prompt, grounding the response in external knowledge without modifying model weights.

Classification note: assigned as technique but also functions as framework — RAG defines a three-stage pipeline (knowledge organization → retrieval → integration) that organizes multiple sub-techniques into a coherent system architecture.
