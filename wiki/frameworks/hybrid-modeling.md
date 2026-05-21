---
title: "Hybrid Modeling"
knowledge_type: framework
also_type: []
domain: [deep-learning, bayesian-stats, optimization]
tags: [physics-informed-ml, scientific-computing, surrogate-models]
related_concepts: ["[[physics-informed-neural-networks]]", "[[bayesian-optimization]]", "[[gaussian-process-regression]]", "[[gibbs-sampler]]", "[[kalman-filter]]"]
sources: ["[[kurz-hybrid-modeling-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Architectures combining first-principle physics models (Newtonian paradigm) with data-driven learning models (Keplerian paradigm) into a joint inference/optimization system; physics constraints reduce effective search space and enable data-efficient learning; encompasses Kalman filtering, PINNs, data-driven field simulation, and Bayesian optimization with physics surrogates; supports enhanced robustness, explainability, and reduced epistemic uncertainty compared to pure data-driven approaches.

## Reading Path
- [[kurz-hybrid-modeling-2022]] (unread) — three case studies: BEM+Bayesian update (CERN magnets), data-driven Maxwell field simulation, GP-based Bayesian free-shape optimization
