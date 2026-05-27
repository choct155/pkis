---
id: "pkis:concept:conjugate-prior"
aliases: []
title: "Conjugate Prior"
knowledge_type: concept
also_type: []
domain: [bayesian-stats]
tags: [probability-theory]
related_concepts: ["[[probability-theory]]", "[[gaussian-distribution]]", "[[bayesian-linear-regression]]"]
sources: ["[[deisenroth-mml]]", "[[kroese-statistical-modeling]]", "[[capretto-bambi-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A prior distribution that, combined with a given likelihood, yields a posterior in the same distributional family — enabling closed-form Bayesian updating; arises naturally from the exponential family structure where the natural parameters of the prior and posterior match.

## Reading Path
- [[deisenroth-mml]] (unread) — foundational treatment: Gaussian-Gaussian conjugacy, table of conjugate pairs
- [[kroese-statistical-modeling-ch08]] (unread) — conjugate Bayesian models for normal (unknown μ and σ²), normal linear, and multinomial models; §8.5 priors and conjugacy
- [[capretto-bambi-2022]] (unread) — Bambi's automatic priors are motivated by approximate conjugacy (Normal priors for Normal likelihoods, HalfStudentT for variance)
