---
aliases: []
authors: Saad-Falcon, J., Khattab, O., Potts, C., Zaharia, M.
concepts: []
date_added: '2026-06-20'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:saadfalcon-ares-2024
linked_nodes: []
source_url: https://arxiv.org/abs/2311.09476
status: unread
tags: []
title: 'ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation
  Systems'
type: paper
year: 2024
---

## Summary
Evaluating retrieval-augmented generation (RAG) systems traditionally relies on hand annotations for input queries, passages to retrieve, and responses to generate. We introduce ARES, an Automated RAG Evaluation System, for evaluating RAG systems along the dimensions of context relevance, answer faithfulness, and answer relevance. By creating its own synthetic training data, ARES finetunes lightweight LM judges to assess the quality of individual RAG components. To mitigate potential prediction 

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:es-ragas-2024
- pkis:technique:retrieval-augmented-generation
- pkis:source:zhang-graphrag-survey
- pkis:framework:multidimensional-retrieval-quality-framework
- pkis:source:radhakrishnan-datagemma-2024

## Notes
Automated RAG evaluation using fine-tuned lightweight LM judges for context relevance, answer faithfulness, and answer relevance. Uses prediction-powered inference (PPI) to mitigate prediction errors with small human annotation sets. Key contribution: reduces human annotation requirement while maintaining alignment with human judgments. Most relevant to our automated measurement strategy — the PPI approach is the right tool for calibrating our five computable dimensions against ground truth on a small sample.