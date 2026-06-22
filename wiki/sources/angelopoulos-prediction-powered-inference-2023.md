---
id: "pkis:source:angelopoulos-prediction-powered-inference-2023"
aliases: []
title: "Prediction-Powered Inference"
authors: "Anastasios N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael I. Jordan, Tijana Zrnic"
year: 2023
type: paper
domain: [statistical-learning, bayesian-stats]
tags: [prediction-powered-inference, confidence-intervals, semi-supervised, llm-as-judge, calibration, valid-inference]
source_url: "https://arxiv.org/abs/2301.09633"
arxiv: "2301.09633"
venue: "Science"
illustrated-by:
- accuracy-calibration-explainer
status: unread
date_added: 2026-06-21
relevance: high
concepts: ["[[calibration]]", "[[confidence-interval]]"]
---

## Summary

Introduces prediction-powered inference (PPI): valid statistical inference when a large set
of machine-learning predictions ("silver" labels) is combined with a small set of gold-standard
labels. PPI forms a rectifier that debiases estimates computed on the predictions using the
labeled subset, yielding confidence intervals with correct coverage that are tighter than
gold-only inference. Applies to means, quantiles, and general M-estimation / convex problems.

## Notes

The gold set measures the ML predictor's systematic error and corrects for it; each additional
unlabeled/LLM-judged example reduces variance without introducing new bias. Published in Science.
The silver/gold calibration architecture in this research program is a direct instantiation of
PPI, and it is the statistical foundation underlying ARES (Saad-Falcon et al. 2024). Foundational
paper for the cost-reduction approach to continuous quality assessment — read first (theory +
estimator), then PPI++ for the production variant.

## Connection Candidates
- pkis:source:saadfalcon-ares-2024
- pkis:source:hastie-esl-ch08
- pkis:source:mackay-itila
