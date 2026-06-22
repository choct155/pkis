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
status: unread
date_added: 2026-06-21
relevance: high
concepts: ["[[calibration]]"]
---

## Summary

Introduces prediction-powered inference (PPI): a framework for valid statistical inference when a large set of machine-learning predictions ('silver' labels) is combined with a small set of gold-standard labels. PPI forms a rectifier that debiases estimates computed on the predictions using the labeled subset, yielding confidence intervals with correct coverage that are tighter than gold-only inference. Applies to means, quantiles, and general M-estimation / convex problems.
