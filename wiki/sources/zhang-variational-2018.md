---
aliases: []
authors: Yuyu Zhang, Hanjun Dai, Zornitsa Kozareva, Alexander J. Smola, Le Song
concepts: []
date_added: '2026-06-07'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:zhang-variational-2018
source_url: https://arxiv.org/abs/1709.04071
status: unread
tags: []
title: Variational Reasoning for Question Answering with Knowledge Graphs (MetaQA)
type: paper
year: 2018
---

## Summary
Knowledge graph (KG) is known to be helpful for the task of question answering (QA), since it provides well-structured relational information between entities, and allows one to further infer indirect facts. However, it is challenging to build QA systems which can learn to reason over knowledge graphs based on question-answer pairs alone. First, when people ask questions, their expressions are noisy (for example, typos in texts, or variations in pronunciations), which is non-trivial for the QA s

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:sequeda-kg-benchmark-llm-2023
- pkis:source:liu-symagent
- pkis:source:sequeda-kg-trust-llm-2025
- pkis:source:cheng-cograg
- pkis:hypothesis:variational-graph-traversal

## Notes
MetaQA: KGQA dataset, movie domain, three difficulty levels (1-hop, 2-hop, 3-hop). ~400,000 questions. Metric: Hits@1. Contamination risk: lower than Freebase (domain-specific KG). Role: controlled analysis of reasoning-depth effects; useful for ablation on ELBO plateau as convergence criterion (plateau should occur at correct depth per level). Note: title says 'Variational Reasoning' — coincidental to VGT but worth examining.