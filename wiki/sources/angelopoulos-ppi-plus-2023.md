---
id: "pkis:source:angelopoulos-ppi-plus-2023"
aliases: []
title: "PPI++: Efficient Prediction-Powered Inference"
authors: "Anastasios N. Angelopoulos, John C. Duchi, Tijana Zrnic"
year: 2023
type: paper
domain: [statistical-learning, bayesian-stats]
tags: [prediction-powered-inference, confidence-intervals, semi-supervised, llm-as-judge, calibration, valid-inference, power-tuning]
source_url: "https://arxiv.org/abs/2311.01453"
arxiv: "2311.01453"
venue: "arXiv"
illustrated-by:
- accuracy-calibration-explainer
status: unread
date_added: 2026-06-21
relevance: high
concepts: ["[[calibration]]", "[[confidence-interval]]"]
---

## Summary

Refines prediction-powered inference with a power-tuning coefficient lambda that optimally
weights the prediction-based correction by the predictor's quality. PPI++ is computationally
lighter and statistically never worse than classical (gold-only) inference, removing PPI's
failure mode when predictions are weak. The production-ready variant of the PPI estimator.

## Notes

The lambda power-tuning coefficient is estimated from pilot data and guarantees variance
asymptotically no worse than the gold-only estimator — eliminating PPI's occasional inefficiency
when predictions are weak. Use PPI for the theory and PPI++ for the production estimator in the
silver/gold calibration framework.

## Connection Candidates
- pkis:source:angelopoulos-prediction-powered-inference-2023
- pkis:source:saadfalcon-ares-2024
