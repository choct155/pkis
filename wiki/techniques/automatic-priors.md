---
title: "Automatic Prior Construction"
knowledge_type: technique
also_type: []
domain: [bayesian-stats]
tags: [probabilistic-programming, weakly-informative-priors, empirical-bayes]
related_concepts: ["[[conjugate-prior]]", "[[bayesian-linear-regression]]", "[[hierarchical-bayesian-models]]"]
sources: ["[[capretto-bambi-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Constructing default weakly informative priors from observed data scales without requiring explicit user specification: in Bambi, slope priors are Normal(0, σ) with σ scaled to the ratio of response variance to predictor variance; intercept priors are centered at the response mean; variance terms use HalfStudentT — aiming to be vague enough for a wide range of use cases while preventing improper posteriors.

## Reading Path
- [[capretto-bambi-2022]] (unread) — Section 4: full description of Bambi's automatic prior construction algorithm and rationale
