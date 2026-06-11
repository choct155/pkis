---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
id: pkis:technique:inverse-transform-sampling
knowledge_type: technique
maturity: settled
prerequisite-of:
- rejection-sampling
related_concepts:
- '[[probability-distribution-relationships]]'
- '[[mcmc]]'
- '[[probability-theory]]'
sources:
- '[[abdelkader-distribution-relationships-2010]]'
tags:
- probability-theory
- simulation
- monte-carlo
title: Inverse Transform Sampling
understanding: 0
---

Generating random variates from a target distribution F by computing x = F^{-1}(U) where U ~ Uniform(0,1); requires a tractable closed-form CDF inverse; when the inverse is unavailable (e.g., normal), related distributions with simple inverses are exploited (e.g., summing exponentials to get Erlang), motivating the study of inter-distribution relationships.

## Reading Path
- [[abdelkader-distribution-relationships-2010]] (unread) — motivates inter-distribution relationships via simulation needs; Erlang deviate construction as worked example

## Connections
- [[rejection-sampling]] — prerequisite-of