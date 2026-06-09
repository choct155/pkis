---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
- forecasting
id: pkis:concept:scoring-rules
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch07
tags:
- predictive-accuracy
- log-score
- proper-scoring-rule
- probabilistic-forecasting
- decision-theory
title: Scoring Rules
understanding: 0
---

## Definition
Measures of the quality of a probabilistic (or point) prediction against a realized outcome. For point prediction, a scoring function (e.g. squared error / mean squared error) assesses a single reported value. For probabilistic prediction, a scoring rule (e.g. quadratic, logarithmic, or zero-one score) assesses an entire predictive distribution, rewarding forecasts that place high density on what actually occurs.

Two desiderata characterize good rules: propriety — the expected score is optimized by reporting one's true beliefs, so the rule motivates honest probability assessments; and locality — the score for outcome ỹ depends only on the predictive density at ỹ. The logarithmic score, log p(y|ω), is the unique (up to affine transformation) rule that is both local and proper, which is precisely why it underlies the log predictive density used throughout Bayesian model evaluation. The log score is proportional to mean squared error when the predictive model is normal with constant variance, linking the probabilistic and point-prediction views.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]