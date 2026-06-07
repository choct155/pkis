---
aliases: []
authors: Yanlin Feng, Simone Papicchio, Sajjadur Rahman
concepts: []
date_added: '2026-06-07'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:feng-cypherbench-2024
source_url: https://arxiv.org/abs/2412.18702
status: unread
tags: []
title: 'CypherBench: Towards Precise Retrieval over Full-scale Modern Knowledge Graphs
  in the LLM Era'
type: paper
year: 2024
---

## Summary
Retrieval from graph data is crucial for augmenting large language models (LLM) with both open-domain knowledge and private enterprise data, and it is also a key component in the recent GraphRAG system (edge et al., 2024). Despite decades of research on knowledge graphs and knowledge base question answering, leading LLM frameworks (e.g. Langchain and LlamaIndex) have only minimal support for retrieval from modern encyclopedic knowledge graphs like Wikidata. In this paper, we analyze the root cau

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:zhang-graphrag-survey
- pkis:source:barron-legal-rag-nmf
- pkis:source:cheng-cograg
- pkis:source:sequeda-kg-benchmark-llm-2023
- pkis:concept:knowledge-graph

## Notes
Benchmark for NL-to-Cypher query generation and retrieval over modern knowledge graphs. Tests LLM ability to navigate typed property graphs. Metric: execution accuracy. Most directly applicable benchmark for IKS Neo4j LPG traversal evaluation. Lower contamination risk — modern KGs and Cypher syntax less covered in pre-training. Priority: medium. Read alongside graph schema expressivity work.