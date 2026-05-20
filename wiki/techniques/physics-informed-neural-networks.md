---
title: "Physics-Informed Neural Networks (PINNs)"
knowledge_type: technique
also_type: []
domain: [deep-learning, optimization]
tags: [scientific-computing, partial-differential-equations, physics-informed-ml]
related_concepts: ["[[hybrid-modeling]]", "[[neural-networks]]", "[[kolmogorov-arnold-networks]]", "[[bayesian-optimization]]"]
sources: ["[[kurz-hybrid-modeling-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Neural networks trained to satisfy partial differential equations by incorporating PDE residuals directly in the loss function alongside data fit terms; introduced by Raissi, Perdikaris & Karniadakis (2019); a paradigmatic example of hybrid modeling where the "Newtonian" physics constraint (PDE) guides data-driven learning — at the cost of losing sparsity in the model representation.

## Reading Path
- [[kurz-hybrid-modeling-2022]] (unread) — mentioned as a hybrid modeling approach; referenced in contrast to data-driven field simulation and Bayesian optimization cases
