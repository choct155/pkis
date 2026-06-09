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
id: pkis:concept:bayesian-anova
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch15
tags:
- multilevel-models
- variance-components
- experimental-design
title: Bayesian Analysis of Variance
understanding: 0
---

## Definition
Gelman's reframing of analysis of variance as a hierarchical regression in which predictors and their coefficients are organized into batches ('sources of variation'), each batch corresponding to one row of an ANOVA table and modeled as exchangeable draws beta_j^(m) ~ N(0, sigma_m^2) with its own variance component. Main effects, interactions, and the residual all become batches; each row is summarized not by an F-test but by the estimated standard deviation of its coefficients, with uncertainty intervals (the Bayesian ANOVA display). A flat prior on sigma_m lets batches with many coefficients estimate their variance from data while batches with few coefficients are allowed large values (minimal shrinkage). This view treats ANOVA as a tool for structuring many predictors into exchangeable groups and for data exploration / model building, rather than as a fixed inferential ritual.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]