---
aliases: []
authors: Rau, D. et al.
concepts: []
date_added: '2026-06-20'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:rau-revisiting-2026
linked_nodes: []
source_url: https://arxiv.org/abs/2602.21553
status: unread
tags: []
title: 'Revisiting RAG Retrievers: An Information Theoretic Benchmark (MIGRASCOPE)'
type: paper
year: 2026
---

## Summary
Retrieval-Augmented Generation (RAG) systems rely critically on the retriever module to surface relevant context for large language models. Although numerous retrievers have recently been proposed, each built on different ranking principles such as lexical matching, dense embeddings, or graph citations, there remains a lack of systematic understanding of how these mechanisms differ and overlap. Existing benchmarks primarily compare entire RAG pipelines or introduce new datasets, providing little

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:es-ragas-2024
- pkis:source:saadfalcon-ares-2024
- pkis:source:zhang-graphrag-survey
- pkis:technique:retrieval-augmented-generation
- pkis:source:radhakrishnan-datagemma-2024

## Notes
MIGRASCOPE: Mutual Information based RAG Retriever Analysis Scope. Information-theoretic metrics for retrieval quality, redundancy, synergy, and marginal contribution across retrievers. Key finding: an ensemble of retrievers chosen carefully outperforms any single retriever. Most directly related to our information-theoretic framing — marginal contribution metric is the closest existing analog to our Structural Relevance dimension. Key difference from our framework: MIGRASCOPE is architecture-agnostic and does not formalize the graph-specific structural dimensions (validity, structural coherence, structural relevance). Provides the empirical methodology for our automated measurement strategy.