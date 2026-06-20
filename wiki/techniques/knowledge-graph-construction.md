---
aliases: []
also_type: []
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:technique:knowledge-graph-construction
knowledge_type: technique
maturity: evolving
related_concepts:
- knowledge-graph
- graph-rag
- rdf
sources:
- '[[zhang-graphrag-survey]]'
- '[[barron-legal-rag-nmf]]'
- '[[liu-symagent]]'
- edge-from-2024
tags:
- knowledge-graphs
- information-extraction
- oie
- nlp
- llm
title: Knowledge Graph Construction
understanding: 0
---

The automated process of transforming unstructured text corpora into structured knowledge graphs via entity recognition, relation extraction, and coreference resolution — using either classical Open Information Extraction (OIE) pipelines or LLM-based extraction — producing nodes (entities/concepts) and typed edges (relations) that can be queried or reasoned over.

## Reading Path
- [[zhang-graphrag-survey]] (unread) — KG construction as the first stage of GraphRAG pipelines; OIE and LLM-based extraction approaches
- [[barron-legal-rag-nmf]] (unread) — NMF-based KG construction from word-embedding matrices; latent topic discovery as alternative to citation-only graph construction
- [[liu-symagent]] (unread) — dynamic KG expansion via LLM triple extraction from Wikipedia documents during agent reasoning