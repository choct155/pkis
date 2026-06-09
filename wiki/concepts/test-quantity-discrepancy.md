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
id: pkis:concept:test-quantity-discrepancy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch06
tags:
- test-quantity
- discrepancy
- model-checking
- posterior-predictive
- test-statistic
- bayesian-stats
title: Test Quantity (Discrepancy Measure)
understanding: 0
---

## Definition
A scalar summary T(y, θ) of data (and possibly parameters) used as the yardstick when comparing observed data to posterior predictive simulations — the Bayesian generalization of a classical test statistic. A test statistic T(y) depends on data alone; allowing dependence on the parameters under their posterior distribution gives a discrepancy measure T(y,θ) that can directly target a model feature awkward to capture with data alone (e.g. an antisymmetric measure of skewness about θ). When T depends on θ both the realized T(y,θ) and replicated T(y_rep,θ) are unknowns, each represented by S simulations; the comparison is shown as a scatterplot of T(y,θ^s) vs T(y_rep^s,θ^s) (symmetric about the 45° line under the model) or a histogram of differences (should straddle 0). Test quantities should be chosen to reflect aspects of the data relevant to the scientific use of the inference and are often features not directly addressed by the model (ranks, residual correlations, number of switches, binned residuals); even an entire ordered graphical display can serve as a test quantity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]