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
id: pkis:concept:robust-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch17
tags:
- outliers
- heavy-tailed
- shrinkage
- model-expansion
title: Robust Inference
understanding: 0
---

## Definition
Inference whose conclusions are not unduly distorted by aberrant observations or by mild violations of the assumed sampling/prior model. Models built on the normal distribution are notoriously *nonrobust*: a single outlier can strongly affect estimates of all parameters, even those with little substantive connection to the outlying point. The Bayesian remedy is **model expansion** rather than outlier rejection: replace a thin-tailed family (normal, Poisson, binomial) with a longer-tailed family that places non-negligible probability far from the center. A long-tailed model reinterprets an extreme value as a draw from the tail of the data/parameter distribution rather than as evidence that the bulk distribution has high variance, so the point is shrunk toward the others much less than thin-tailed shrinkage would dictate. Crucially, in the Bayesian framework the classical distinction between *searching for outliers to delete them* and *procedures invulnerable to outliers* dissolves: a heavy-tailed or mixture model both downweights extreme points and remains an exchangeable, fully probabilistic model, so no point is treated in a fundamentally different way. Robustness is always relative to the estimand — posterior medians and 50%/95% intervals may be insensitive to tail assumptions while 99.9% intervals are highly sensitive. Robust models double as a tool for assessing model sensitivity (e.g. varying the t degrees of freedom from normal to Cauchy).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]