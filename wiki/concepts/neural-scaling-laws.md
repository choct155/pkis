---
title: "Neural Scaling Laws"
knowledge_type: concept
also_type: []
domain: [deep-learning, optimization]
tags: [approximation-theory, statistical-learning]
related_concepts: ["[[kolmogorov-arnold-networks]]", "[[universal-approximation-theorem]]", "[[bias-variance-tradeoff]]", "[[curse-of-dimensionality]]"]
sources: ["[[liu-kan-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

The empirical and theoretical relationship ℓ ∝ N^{-α} between test loss ℓ and model parameter count N, where the scaling exponent α measures how quickly accuracy improves with scale; KANs with cubic splines achieve α=4 (beating curse of dimensionality for compositionally structured functions), while MLPs with ReLU activations typically saturate at α≈1 and plateau quickly.

## Reading Path
- [[liu-kan-2024]] (unread) — primary treatment; proves KAT approximation bound giving α=k+1 for order-k splines, compares empirically against MLPs
