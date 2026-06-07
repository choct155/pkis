---
aliases: []
authors: Wen-tau Yih, Matthew Richardson, Chris Meek, Ming-Wei Chang, Jina Suh
concepts: []
date_added: '2026-06-07'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:yih-the-2016
source_url: https://aclanthology.org/P16-2033/
status: unread
tags: []
title: The Value of Semantic Parse Labeling for Knowledge Base Question Answering
  (WebQuestionsSP)
type: paper
year: 2016
---

## Summary
[To be filled during ingest]

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:cimiano-ontology-nlp-ch09
- pkis:technique:semantic-parsing
- pkis:source:sequeda-kg-benchmark-llm-2023
- pkis:source:cimiano-ontology-nlp
- pkis:source:fama-french-value-premium-2020

## Notes
WebQuestionsSP (WebQSP): foundational KGQA benchmark. 4,737 NL questions from Google query logs annotated with SPARQL over Freebase. 1-2 hops (65% single-hop, 35% two-hop). Metric: Hits@1. Contamination risk: high (Freebase in LLM training). Role: sanity-check benchmark — establishes method works at all. Insufficient alone for VGT (does not stress multi-hop). Used by ToG as primary benchmark.