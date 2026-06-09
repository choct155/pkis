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
id: pkis:technique:bayesian-model-checking
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch06
tags:
- model-checking
- model-criticism
- goodness-of-fit
- posterior-predictive
- sensitivity-analysis
- bayesian-workflow
title: Bayesian Model Checking
understanding: 0
---

## Definition
The third stage of a Bayesian analysis (after building a model and computing the posterior): assessing whether the fitted model is adequate for the data and for the substantive purposes it will serve. Since 'model' encompasses the sampling distribution, prior, any hierarchical structure, and which predictors are included, checking guards against the misleading inferences that prior-to-posterior reasoning can produce when the whole structure is poor. The guiding question is not 'Is the model true or false?' (real models are essentially never exactly true) but 'Do the model's deficiencies have a noticeable effect on the substantive inferences?'. Principal tools include external validation (predict future data, then collect and compare), posterior predictive checking (graphical and numerical), and sensitivity analysis; finding a misfit is never the end of analysis but a pointer toward model expansion, data correction, or a better-designed experiment.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]