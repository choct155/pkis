---
title: "Gaussian Distribution"
knowledge_type: concept
also_type: []
domain: [bayesian-stats, statistical-learning]
tags: [probability-theory]
related_concepts: ["[[probability-theory]]", "[[conjugate-prior]]", "[[gaussian-mixture-models]]", "[[bayesian-linear-regression]]"]
sources: ["[[deisenroth-mml]]", "[[capretto-bambi-2022]]", "[[kurz-hybrid-modeling-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The normal distribution, characterized by mean and covariance, central to ML because it is the maximum entropy distribution for a given mean and variance, is closed under linear transformations and marginalization, and is its own conjugate prior — making Gaussian models analytically tractable.

## Reading Path
- [[deisenroth-mml]] (unread) — foundational treatment; max-entropy property, conjugacy, closure under linear transforms
- [[capretto-bambi-2022]] (unread) — Gaussian is the default Bambi family; automatic Normal priors for slopes and HalfStudentT for variance
- [[kurz-hybrid-modeling-2022]] (unread) — Gaussian prior p(ν) ~ N(ν_0, L_ν^{-1}) and Gaussian sensor noise model enable analytic conditional posteriors in BEM Bayesian update
