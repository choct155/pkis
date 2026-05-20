---
title: "Bambi (BAyesian Model Building Interface)"
knowledge_type: technique
also_type: []
domain: [bayesian-stats]
tags: [probabilistic-programming, software, python, glmm]
related_concepts: ["[[hierarchical-bayesian-models]]", "[[bayesian-linear-regression]]", "[[automatic-priors]]", "[[mcmc]]", "[[generalized-linear-models]]"]
sources: ["[[capretto-bambi-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Python package providing a formula-based interface (R lme4/brms syntax) for fitting Generalized Linear Multilevel Models via Bayesian inference; built on PyMC (NUTS sampler) and ArviZ (diagnostics/visualization); supports automatic weakly informative prior construction, categorical predictors, crossed random effects, and custom families and link functions. Classification note: assigned as technique (it is a procedure/tool for model specification and fitting) but has framework-like qualities in defining a complete workflow.

## Reading Path
- [[capretto-bambi-2022]] (unread) — primary source; full package description, usage examples, prior construction details
