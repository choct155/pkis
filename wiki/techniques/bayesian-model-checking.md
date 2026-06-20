---
aliases: []
also_type: []
applies:
- hierarchical-bayesian-models
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- bayesian-model-comparison
- hypothesis-testing
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
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
- gelman-bda3
tags:
- model-checking
- model-criticism
- goodness-of-fit
- posterior-predictive
- sensitivity-analysis
- bayesian-workflow
title: Bayesian Model Checking
understanding: 0
uses:
- posterior-predictive-check
- sensitivity-analysis
---

## Definition
The third stage of a Bayesian analysis (after building a model and computing the posterior): assessing whether the fitted model is adequate for the data and for the substantive purposes it will serve. Since 'model' encompasses the sampling distribution, prior, any hierarchical structure, and which predictors are included, checking guards against the misleading inferences that prior-to-posterior reasoning can produce when the whole structure is poor. The guiding question is not 'Is the model true or false?' (real models are essentially never exactly true) but 'Do the model's deficiencies have a noticeable effect on the substantive inferences?'. Principal tools include external validation (predict future data, then collect and compare), posterior predictive checking (graphical and numerical), and sensitivity analysis; finding a misfit is never the end of analysis but a pointer toward model expansion, data correction, or a better-designed experiment.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hierarchical-bayesian-models]] — applies: hierarchical-parameter batches checked against their reference distributions; SAT 8-schools example
- [[hypothesis-testing]] — contrasts-with: checks understand model limits rather than accept/reject at a Type I error rate
- [[bayesian-model-comparison]] — contrasts-with: checking explores a model's limits; comparison chooses among models
- [[sensitivity-analysis]] — uses: complementary check on robustness to alternative models
- [[posterior-predictive-check]] — uses: PPC is the central tool of Bayesian model checking
[To be populated during integration]