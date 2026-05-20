---
title: "Regularization"
knowledge_type: concept
also_type: []
domain: [statistical-learning, optimization]
tags: [linear-algebra, model-selection]
related_concepts: ["[[bias-variance-tradeoff]]"]
sources: ["[[hastie-esl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

## Disambiguation

The term "regularization" has domain-specific meanings:

**Statistical learning / optimization:** Adding a penalty term to the objective function that discourages complexity, trading increased bias for reduced variance. Manifests as L1 (lasso), L2 (ridge), or elastic net penalties.

**Inverse problems (Tikhonov):** Stabilizing ill-posed problems by imposing smoothness or norm constraints on the solution.

**Deep learning:** Umbrella term for any technique that reduces overfitting — includes weight decay, dropout, early stopping, data augmentation.

These uses share a common core (constraining the solution space to improve generalization) but differ in mechanism and theoretical grounding.
