---
aliases: []
authors: Kwiatkowski, T. et al.
concepts: []
date_added: '2026-06-20'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:kwiatkowski-do-2024
linked_nodes: []
source_url: https://arxiv.org/abs/2410.15531
status: unread
tags: []
title: Do RAG Systems Cover What Matters? Evaluating and Optimizing Responses with
  Sub-Question Coverage
type: paper
year: 2024
---

## Summary
Evaluating retrieval-augmented generation (RAG) systems remains challenging, particularly for open-ended questions that lack definitive answers and require coverage of multiple sub-topics. In this paper, we introduce a novel evaluation framework based on sub-question coverage, which measures how well a RAG system addresses different facets of a question. We propose decomposing questions into sub-questions and classifying them into three types -- core, background, and follow-up -- to reflect thei

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:es-ragas-2024
- pkis:source:ru-ragchecker-2024
- pkis:source:saadfalcon-ares-2024
- pkis:source:radhakrishnan-datagemma-2024
- pkis:source:rau-revisiting-2026

## Notes
Sub-question coverage evaluation for RAG: decomposes queries into sub-questions and measures whether the retrieved context and generated response address all sub-questions. Directly relevant to our Coverage dimension — sub-question coverage is a fine-grained operationalization of Coverage(q, S) that maps query decomposition onto verifiable coverage units. The sub-question decomposition approach is also relevant to the two-step query decomposition formalism (retrieval vs synthesis as separable problems).