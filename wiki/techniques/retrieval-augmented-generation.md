---
aliases: []
also_type:
- framework
coverage: 9
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
- deep-learning
id: pkis:technique:retrieval-augmented-generation
knowledge_type: technique
maturity: evolving
related_concepts:
- knowledge-graph
- graph-rag
sources:
- '[[zhang-graphrag-survey]]'
- '[[gulli-agentic-design-patterns]]'
- '[[barron-legal-rag-nmf]]'
- '[[baldazzi-soft-ontological-reasoning]]'
- '[[cheng-cograg]]'
- '[[banf-tripartite-graphrag]]'
- '[[sequeda-kg-benchmark-llm-2023]]'
- '[[sequeda-kg-trust-llm-2025]]'
- '[[radhakrishnan-datagemma-2024]]'
- arxivorg-thinkongraph
- edge-from-2024
- es-ragas-2024
- feng-cypherbench-2024
- gao-retrievalaugmented-2025
- kwiatkowski-do-2024
- procko-from-2026
- rau-revisiting-2026
- ru-ragchecker-2024
- saadfalcon-ares-2024
- share-thinkongraph-1
- wu-stark-2024
- gulli-agentic-design-patterns-ch14
- gulli-agentic-design-patterns-ch22
tags:
- llm
- information-retrieval
- rag
- vector-databases
title: Retrieval-Augmented Generation
understanding: 0
---

## Reading Path
- [[zhang-graphrag-survey]] (unread) — theoretical survey; covers knowledge-based, index-based, and hybrid RAG variants
- [[gulli-agentic-design-patterns-ch14]] (unread) — practical pattern treatment; covers standard RAG, GraphRAG, and Agentic RAG with code examples
- [[barron-legal-rag-nmf]] (unread) — legal domain; integrates VS, KG, and NMF retrieval; demonstrates RAG for reducing hallucinations in high-stakes legal QA
- [[baldazzi-soft-ontological-reasoning]] (unread) — RAG used to enrich LLM semantic unifier in soft chase for ontological reasoning
- [[cheng-cograg]] (unread) — KGQA application; graph-structured retrieval augmenting LLM reasoning with KG triples
- [[banf-tripartite-graphrag]] (unread) — tripartite GraphRAG with concept-anchored graph construction and MRF-based prompt assembly
- [[sequeda-kg-benchmark-llm-2023]] (unread) — OWL ontology as structured context injected into LLM prompt; a structured RAG variant achieving 54.2% AOEA vs. 16.7% for ungrounded SQL prompting
- [[sequeda-kg-trust-llm-2025]] (unread) — governed KG access as principled RAG with formal validity checking and provenance; trust infrastructure framing
- [[radhakrishnan-datagemma-2024]] (unread) — domain-specific RAG over public statistical data: fine-tuned query decomposition step routes sub-questions to Data Commons, tables augment long-context LLM prompt for factual grounding

A framework that enhances LLM generation by retrieving relevant content from an external knowledge base at inference time: the corpus is chunked, embedded, and indexed; at query time, the most similar chunks are retrieved and prepended to the LLM prompt, grounding the response in external knowledge without modifying model weights.

Classification note: assigned as technique but also functions as framework — RAG defines a three-stage pipeline (knowledge organization → retrieval → integration) that organizes multiple sub-techniques into a coherent system architecture.