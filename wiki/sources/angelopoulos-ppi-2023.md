---
aliases: []
authors: Angelopoulos, A.N., Duchi, J.C., Zrnic, T.
concepts: []
date_added: '2026-06-20'
date_updated: '2026-06-21'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:angelopoulos-ppi-2023
linked_nodes: []
priority: high
source_url: https://arxiv.org/abs/2311.01453
status: unread
tags: []
title: 'PPI++: Efficient Prediction-Powered Inference'
type: paper
year: 2023
---

## Summary
We present PPI++: a computationally lightweight methodology for estimation and inference based on a small labeled dataset and a typically much larger dataset of machine-learning predictions. The methods automatically adapt to the quality of available predictions, yielding easy-to-compute confidence sets -- for parameters of any dimensionality -- that always improve on classical intervals using only the labeled data. PPI++ builds on prediction-powered inference (PPI), which targets the same probl

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:angelopoulos-predictionpowered-2023
- pkis:source:saadfalcon-ares-2024
- pkis:technique:fake-data-simulation
- pkis:framework:probabilistic-programming-language
- pkis:source:mikolov-efficient-2013

## Notes
PPI++ — the efficient variant of Prediction-Powered Inference. Introduces a power-tuning coefficient λ that guarantees variance no worse than the classical labeled-only estimator asymptotically. Addresses the key practical limitation of the original PPI paper: the original estimator could occasionally be less efficient than using only the gold labels. PPI++ eliminates this by adaptively weighting the LLM predictions. The λ parameter is estimated from pilot data and the resulting estimator is always at least as good as the gold-only baseline.

This is the implementation reference for the silver/gold calibration framework — use PPI for the theory and PPI++ for the actual estimator in production. Together these two papers are the statistical foundation for cost-efficient continuous quality assessment across all automatable dimensions of the multidimensional retrieval quality framework.