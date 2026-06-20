---
aliases: []
authors: Ru, J. et al.
concepts: []
date_added: '2026-06-20'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:ru-ragchecker-2024
linked_nodes: []
source_url: https://arxiv.org/abs/2408.08067
status: unread
tags: []
title: 'RAGChecker: A Fine-Grained Framework for Diagnosing Retrieval-Augmented Generation'
type: paper
year: 2024
---

## Summary
Despite Retrieval-Augmented Generation (RAG) showing promising capability in leveraging external knowledge, a comprehensive evaluation of RAG systems is still challenging due to the modular nature of RAG, evaluation of long-form responses and reliability of measurements. In this paper, we propose a fine-grained evaluation framework, RAGChecker, that incorporates a suite of diagnostic metrics for both the retrieval and generation modules. Meta evaluation verifies that RAGChecker has significantly

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:es-ragas-2024
- pkis:source:saadfalcon-ares-2024
- pkis:technique:retrieval-augmented-generation
- pkis:source:rau-revisiting-2026
- pkis:source:radhakrishnan-datagemma-2024

## Notes
Fine-grained RAG evaluation via claim decomposition. Decomposes ground-truth answers and model responses into atomic verifiable claims, then checks entailment relations between them. Key metrics: precision (correctness of generated claims), recall (completeness relative to ground truth), claim-level grounding. Most relevant to our Groundedness dimension — the claim-level approach is the right mechanism for automated groundedness checking without requiring full human annotation. The claim extraction step is LLM-based but lightweight and scalable.