---
aliases: []
also_type:
- framework
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- causal-analysis
id: pkis:concept:identification-strategy
knowledge_type: concept
maturity: settled
related_concepts:
- '[[potential-outcomes-framework]]'
- '[[selection-bias]]'
- '[[regression-discontinuity]]'
- '[[instrumental-variables]]'
- '[[difference-in-differences]]'
- '[[synthetic-control]]'
- '[[matching-estimators]]'
sources:
- '[[cunningham-causal-inference-mixtape]]'
- cunningham-causal-inference-mixtape-ch12
tags:
- causal-inference
- identification
- research-design
- econometrics
- credibility-revolution
title: Identification Strategy
understanding: 0
---

An identification strategy is the set of assumptions and research design choices that justify interpreting a statistical estimator as a causal quantity — the argument that links E[Y|D] (observational) to E[Y(1)−Y(0)] (causal) under stated conditions; different strategies (RDD, IV, DiD, matching, synthetic control) exploit different sources of exogenous variation.

## Reading Path
- [[cunningham-causal-inference-mixtape]] (unread) — the book's central organizing concept: each chapter presents a distinct identification strategy
- [[cunningham-causal-inference-mixtape-ch01]] (unread) — motivates identification strategy thinking relative to structural modeling approaches