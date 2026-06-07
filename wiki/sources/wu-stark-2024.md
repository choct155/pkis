---
aliases: []
authors: Shirley Wu, Shiyu Zhao, Michihiro Yasunaga, Kexin Huang, Kaidi Cao, Qian
  Huang, Vassilis N. Ioannidis, Karthik Subbian, James Zou, Jure Leskovec
concepts: []
date_added: '2026-06-07'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:wu-stark-2024
source_url: https://arxiv.org/abs/2404.13207
status: unread
tags: []
title: 'STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases'
type: paper
year: 2024
---

## Summary
Answering real-world complex queries, such as complex product search, often requires accurate retrieval from semi-structured knowledge bases that involve blend of unstructured (e.g., textual descriptions of products) and structured (e.g., entity relations of products) information. However, many previous works studied textual and relational retrieval tasks as separate topics. To address the gap, we develop STARK, a large-scale Semi-structure retrieval benchmark on Textual and Relational Knowledge

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:barron-legal-rag-nmf
- pkis:source:cheng-cograg
- pkis:source:zhang-graphrag-survey
- pkis:problem:knowledge-graph-question-answering
- pkis:source:wu-thinkongraph-2025

## Notes
Benchmark for LLM retrieval over textual and relational knowledge bases. Three domains: scientific literature, e-commerce, medical. Requires combining structured and unstructured knowledge. Metrics: recall@k, MRR. Most relevant benchmark for IKS context — tests hybrid structured-unstructured retrieval analogous to private markets. Lower contamination risk than Freebase/Wikidata. Priority: medium. Read after KGQA fundamentals (WebQSP, CWQ).