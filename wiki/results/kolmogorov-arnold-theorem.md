---
id: "pkis:result:kolmogorov-arnold-theorem"
aliases: []
title: "Kolmogorov-Arnold Representation Theorem"
knowledge_type: result
also_type: []
domain: [deep-learning, optimization]
tags: [approximation-theory, functional-analysis]
related_concepts: ["[[kolmogorov-arnold-networks]]", "[[universal-approximation-theorem]]", "[[neural-scaling-laws]]"]
sources: ["[[liu-kan-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

For any smooth multivariate function f: [0,1]^n → R, there exist continuous univariate functions ϕ_{q,p}: [0,1] → R and Φ_q: R → R such that f(x) = Σ_{q=1}^{2n+1} Φ_q(Σ_{p=1}^n ϕ_{q,p}(x_p)) — meaning every multivariate function is expressible as compositions of univariate functions and addition; KANs are the neural network generalization of this theorem to arbitrary depth and width.

## Reading Path
- [[liu-kan-2024]] (unread) — motivates and invokes the theorem; provides approximation bound (KAT) for B-spline realizations
