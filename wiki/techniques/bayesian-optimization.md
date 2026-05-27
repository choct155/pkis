---
id: "pkis:technique:bayesian-optimization"
aliases: []
title: "Bayesian Optimization"
knowledge_type: technique
also_type: []
domain: [optimization, bayesian-stats]
tags: [gaussian-processes, surrogate-models, exploration-exploitation, black-box-optimization]
related_concepts: ["[[gaussian-process-regression]]", "[[hybrid-modeling]]", "[[acquisition-functions]]", "[[exploration-exploitation]]"]
sources: ["[[kurz-hybrid-modeling-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Sequential optimization of expensive black-box functions using a cheap probabilistic surrogate model (typically a Gaussian Process) updated with each evaluation: an acquisition function (e.g., Expected Improvement) balances exploration of uncertain regions against exploitation of known-good regions; the next evaluation point is chosen to maximize expected improvement; particularly effective for high-dimensional design spaces with costly function evaluations, as demonstrated for free-shape optimization of printed circuit board trace pairs.

## Reading Path
- [[kurz-hybrid-modeling-2022]] (unread) — multi-objective Bayesian free-shape optimization; GP surrogate restricted to adjoint-gradient-defined 2D subspaces; ~100 evaluations to converge Pareto front in 200-dimensional space
