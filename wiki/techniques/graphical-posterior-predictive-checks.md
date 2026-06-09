---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:graphical-posterior-predictive-checks
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch06
tags:
- posterior-predictive
- graphical-checking
- exploratory-data-analysis
- residuals
- binned-residuals
- visualization
- bayesian-stats
title: Graphical Posterior Predictive Checks
understanding: 0
---

## Definition
Model checking by displaying observed data alongside simulated data from the fitted model and looking for systematic discrepancies; the graphical display itself plays the role of a test quantity. BDA3 distinguishes three kinds of display: (1) direct display of all the data next to several replications y_rep (e.g. histograms of the speed-of-light replications, or aligned three-way binary arrays where real data show rectilinear structure absent from fuzzy replications); (2) display of data summaries or parameter inferences, including comparing a single posterior draw of a batch of hierarchical parameters to its reference (prior) distribution — the replication being a new draw of the batch; (3) graphs of residuals or other discrepancy measures. Effective displays exploit regular structure (the key is ordering rows/columns by average response, which makes patterns visible). For regression it uses Bayesian (realized) residuals y_i − g(x_i,ω) from a posterior draw of ω — classical residual plots are point-estimate approximations — and, for discrete data whose raw residuals have distracting discrete stripes, binned/smoothed residuals ī_k vs w̄_k that become approximately normal by the CLT and can be assessed against implicit 95% reference bounds.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]