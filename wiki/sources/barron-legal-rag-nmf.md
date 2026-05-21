---
title: "Bridging Legal Knowledge and AI: RAG with Vector Stores, Knowledge Graphs, and Hierarchical NMF"
authors: ["Ryan C. Barron", "Maksim E. Eren", "Olga M. Serafimova", "Cynthia Matuszek", "Boian S. Alexandrov"]
year: 2025
type: paper
domain: [knowledge-representation, deep-learning]
tags: [rag, knowledge-graphs, legal, nmf, topic-modeling, vector-stores, llm, information-retrieval, semi-structured-data]
source_url: "https://doi.org/XXXXXXX.XXXXXXX"
drive_id: "1UHkzaeszOPlUKRwIQNPeDNKhnU0WvmuZ"
drive_path: "PKIS/sources/papers/barron-legal-rag-nmf.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[retrieval-augmented-generation]]", "[[knowledge-graph]]", "[[knowledge-graph-construction]]", "[[non-negative-matrix-factorization]]"]
---

## Summary

Barron et al. present a generative AI system for legal information retrieval that integrates three complementary technologies: vector stores (VS) for semantic similarity search, knowledge graphs (KG) for structured relational navigation, and Non-Negative Matrix Factorization (NMF) for latent topic discovery. The system is applied to the legal domain — constitutions, statutes, case law — where documents are inherently semi-structured with complex hierarchical and citation-based relations.

The legal KG is constructed via NMF applied to word-embedding matrices, yielding interpretable latent topics that cluster related legal documents. Hierarchical NMF enables multi-level topic discovery at varying granularities. Vector stores embed legal texts for semantic retrieval beyond keyword matching, while the KG formalizes citation and doctrinal relationships between cases, statutes, and constitutional provisions. A RAG layer combines all three retrieval modes to ground LLM outputs in authoritative legal texts, reducing hallucinations.

The system demonstrates capabilities in legal document clustering, summarization, and cross-referencing. A key contribution is using NMF to identify latent topics not visible in raw citation structure, which can then seed edges in the legal KG. The paper addresses both the scalability challenge (large volumes of continuously produced legal texts) and the interpretability challenge (NMF's additive factorization is more transparent than neural embeddings alone). The ICAIL 2025 work positions this as a significant step toward augmenting legal research with scalable, interpretable, and accurate retrieval methods.

## Key Knowledge Objects

- [[retrieval-augmented-generation]] (technique, high) — core framework combining VS, KG, and NMF retrieval with LLM generation for legal QA
- [[knowledge-graph]] (concept, high) — legal KG encoding statute–case, case–case, and doctrine relationships for structured navigation
- [[knowledge-graph-construction]] (technique, high) — NMF-seeded KG construction from legal text embedding matrices
- [[non-negative-matrix-factorization]] (technique, high) — latent topic discovery from word-embedding matrices; interpretable dimensionality reduction for clustering and topic labeling
- [[graph-rag]] (technique, moderate) — system integrates KG-based retrieval within a RAG framework, overlapping with GraphRAG pattern

## Key Extractions

1. **Three-component integration**: Vector stores handle semantic similarity beyond keywords; knowledge graphs encode explicit legal relationships (citation, doctrinal); NMF uncovers hidden latent topics in unstructured legal text — each component addresses different retrieval failure modes.
2. **NMF for legal KG construction**: NMF is applied to word-embedding matrices derived from legal corpora to extract interpretable topic clusters; these topics then seed edges and node groupings in the legal KG, providing structure that citation networks alone do not reveal.
3. **Hierarchical NMF**: Multi-level factorization enables coarse-to-fine topic discovery; the paper notes prior work applied NMF hierarchically to legal documents but lacked automatic cluster-count estimation, which this system addresses.
4. **Hallucination reduction via grounding**: RAG architecture roots LLM responses in retrieved authoritative legal texts (statutes, case opinions), demonstrably reducing hallucinations relative to ungrounded generation — critical for high-stakes legal applications.
5. **Semi-structured data challenge**: Legal texts mix hierarchical structure (constitutional/statutory sections) with unstructured prose (case opinions); the system must handle both via VS embeddings for unstructured content and KG traversal for hierarchical references.

## Connection Candidates

- [[retrieval-augmented-generation]] — extends: adds VS, KG, and NMF as three complementary retrieval mechanisms within the RAG framework
- [[knowledge-graph-construction]] — uses: NMF applied to embeddings as an alternative (latent-topic-based) KG construction approach alongside citation extraction
- [[non-negative-matrix-factorization]] — uses: core dimensionality reduction method for topic discovery and KG seeding
- [[knowledge-graph]] — uses: legal KG encodes citation and doctrinal relationships for structured RAG retrieval
- [[graph-rag]] — specializes: this system is a domain-specific (legal) instantiation of the GraphRAG pattern
