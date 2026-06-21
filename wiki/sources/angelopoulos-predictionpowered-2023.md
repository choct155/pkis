---
aliases: []
authors: Angelopoulos, A.N., Bates, S., Fannjiang, C., Jordan, M.I., Zrnic, T.
concepts: []
date_added: '2026-06-20'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:angelopoulos-predictionpowered-2023
linked_nodes: []
source_url: https://www.science.org/doi/10.1126/science.adi6000
status: unread
tags: []
title: Prediction-Powered Inference
type: paper
year: 2023
illustrated-by:
- accuracy-calibration-explainer
---

## Summary
[To be filled during ingest]

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:technique:learned-approximate-inference
- pkis:source:murphy-pml2-advanced-ch07
- pkis:source:mackay-itila
- pkis:source:saadfalcon-ares-2024
- pkis:source:hastie-esl-ch08

## Notes
Introduces Prediction-Powered Inference (PPI) — a semi-supervised estimation framework that combines a small gold set of human labels with a large set of machine learning predictions to produce provably valid, unbiased statistical estimates. The gold set measures the ML predictor's systematic error and corrects for it. Each additional unlabeled/LLM-judged example reduces variance without introducing new bias. Published in Science.

Directly relevant to the accuracy measurement framework developed in this research program: the silver/gold calibration architecture is a direct instantiation of PPI. Also the statistical foundation underlying ARES (Saad-Falcon et al. 2024) and PRECISE (2026). The PRECISE extension applies PPI to ranking metrics (Precision@K, Recall@K) at sub-instance granularity, achieving 95% cost reduction with 30 gold samples.

High priority read — the foundational paper for the entire cost-reduction approach to continuous quality assessment.