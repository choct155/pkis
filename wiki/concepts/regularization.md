---
title: "Regularization"
knowledge_type: concept
also_type: []
domain: [statistical-learning, optimization]
tags: [linear-algebra, model-selection]
related_concepts: ["[[bias-variance-tradeoff]]"]
sources: ["[[hastie-esl]]", "[[nielsen-nndl]]", "[[kroese-statistical-modeling]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

## Disambiguation

The term "regularization" has domain-specific meanings:

**Statistical learning / optimization:** Adding a penalty term to the objective function that discourages complexity, trading increased bias for reduced variance. Manifests as L1 (lasso), L2 (ridge), or elastic net penalties.

**Inverse problems (Tikhonov):** Stabilizing ill-posed problems by imposing smoothness or norm constraints on the solution.

**Deep learning:** Umbrella term for any technique that reduces overfitting — includes weight decay, dropout, early stopping, data augmentation.

These uses share a common core (constraining the solution space to improve generalization) but differ in mechanism and theoretical grounding.

## Reading Path
- [[nielsen-nndl-ch03]] (unread) — deep-learning treatment: L1/L2 weight decay, dropout, early stopping, and data augmentation with empirical MNIST comparisons
- [[hastie-esl-ch05]] (unread) — statistical learning perspective on regularization via basis expansions
- [[kroese-statistical-modeling-ch09]] (unread) — dedicated regularization chapter: James-Stein, ridge, lasso, and false discovery rate; shrinkage as a unified perspective
