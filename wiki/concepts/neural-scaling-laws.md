---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-10-12'
domain:
- deep-learning
- optimization
id: pkis:concept:neural-scaling-laws
knowledge_type: concept
maturity: evolving
related_concepts:
- '[[kolmogorov-arnold-networks]]'
- '[[universal-approximation-theorem]]'
- '[[bias-variance-tradeoff]]'
- '[[curse-of-dimensionality]]'
sources:
- '[[liu-kan-2024]]'
- kaplan-scaling-2020
tags:
- approximation-theory
- statistical-learning
title: Neural Scaling Laws
understanding: 0
---

The empirical and theoretical relationship ℓ ∝ N^{-α} between test loss ℓ and model parameter count N, where the scaling exponent α measures how quickly accuracy improves with scale; KANs with cubic splines achieve α=4 (beating curse of dimensionality for compositionally structured functions), while MLPs with ReLU activations typically saturate at α≈1 and plateau quickly.

## Reading Path
- [[liu-kan-2024]] (unread) — primary treatment; proves KAT approximation bound giving α=k+1 for order-k splines, compares empirically against MLPs