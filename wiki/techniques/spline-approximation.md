---
title: "Spline Approximation"
knowledge_type: technique
also_type: []
domain: [optimization, deep-learning]
tags: [approximation-theory, numerical-methods]
related_concepts: ["[[kolmogorov-arnold-networks]]", "[[kolmogorov-arnold-theorem]]", "[[neural-scaling-laws]]"]
sources: ["[[liu-kan-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Piecewise polynomial function approximation using B-spline basis functions with learnable coefficients; in KANs, each activation function on an edge is a trainable B-spline combined with a residual basis (SiLU), enabling progressive refinement via grid extension (increasing number of knots) and beating the curse of dimensionality for univariate function approximation.

## Reading Path
- [[liu-kan-2024]] (unread) — B-spline parameterization of KAN activation functions, grid extension algorithm, and approximation theory (Theorem 2.1)
