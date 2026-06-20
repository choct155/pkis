---
aliases: []
authors: Edge, D. et al.
concepts: []
date_added: '2026-06-20'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:edge-from-2024
linked_nodes: []
source_url: https://arxiv.org/abs/2404.16130
status: unread
tags: []
title: 'From Local to Global: A Graph RAG Approach to Query-Focused Summarization'
type: paper
year: 2024
---

## Summary
The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs) to answer questions over private and/or previously unseen document collections. However, RAG fails on global questions directed at an entire text corpus, such as "What are the main themes in the dataset?", since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task. Prior QFS methods, meanwhile, do no

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:zhang-graphrag-survey
- pkis:technique:retrieval-augmented-generation
- pkis:source:es-ragas-2024
- pkis:source:rau-revisiting-2026
- pkis:source:saadfalcon-ares-2024

## Notes
Microsoft GraphRAG: builds entity-relation knowledge graphs from documents via LLM extraction, partitions into hierarchical community structure, generates bottom-up summaries. Two retrieval modes: local (entity neighborhood) and global (community summary). Key finding: global GraphRAG dominates vector RAG on global sensemaking queries; local mode is competitive on factoid queries. Directly relevant to the graph vs vector comparison hypothesis. Important caveat for our framework: GraphRAG builds graphs from document content (entity extraction) whereas our framework builds from ontological structure (typed concept nodes). The distinction matters — GraphRAG graphs inherit document noise; ontological concept graphs encode principled conceptual structure. The quality profile comparison in our framework applies to ontological graph retrieval, not document-derived entity graphs.