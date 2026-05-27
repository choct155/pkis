---
id: "pkis:technique:lagrange-multipliers"
aliases: []
title: "Lagrange Multipliers"
knowledge_type: technique
also_type: [result]
domain: [optimization]
tags: [calculus, mathematical-foundations]
related_concepts: ["[[continuous-optimization]]", "[[convex-optimization]]", "[[support-vector-machines]]"]
sources: ["[[deisenroth-mml]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Method for optimizing a function subject to equality constraints by introducing multipliers $\lambda$ and solving the unconstrained Lagrangian $\mathcal{L}(x, \lambda) = f(x) - \lambda^T g(x)$; extended by KKT conditions to inequality constraints, providing the theoretical foundation for SVM duality and constrained statistical estimation.
