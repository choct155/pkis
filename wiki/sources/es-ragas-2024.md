---
aliases: []
authors: Es, S., James, J., Anke, L.E., Schockaert, S.
concepts: []
date_added: '2026-06-20'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:es-ragas-2024
linked_nodes: []
source_url: https://arxiv.org/abs/2309.15217
status: unread
tags: []
title: 'RAGAS: Automated Evaluation of Retrieval Augmented Generation'
type: paper
year: 2024
---

## Summary
We introduce Ragas (Retrieval Augmented Generation Assessment), a framework for reference-free evaluation of Retrieval Augmented Generation (RAG) pipelines. RAG systems are composed of a retrieval and an LLM based generation module, and provide LLMs with knowledge from a reference textual database, which enables them to act as a natural language layer between a user and textual databases, reducing the risk of hallucinations. Evaluating RAG architectures is, however, challenging because there are

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:radhakrishnan-datagemma-2024
- pkis:source:zhang-graphrag-survey
- pkis:technique:retrieval-augmented-generation
- pkis:source:wu-stark-2024
- pkis:source:barron-legal-rag-nmf

## Notes
Reference-free evaluation framework for RAG systems. Three core dimensions: faithfulness (is the response grounded in retrieved context), answer relevance (does the response address the query), context relevance (is the retrieved context sufficiently focused). Widely adopted baseline. Key limitation: context relevance and answer relevance conflate structural and semantic properties that our framework separates. Faithfulness maps to our Groundedness dimension. Context relevance maps to a blend of Coverage and Concision.