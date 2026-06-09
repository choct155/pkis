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
- statistical-learning
id: pkis:technique:structural-risk-minimization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch07
tags:
- model-selection
- vc-theory
- generalization-bounds
- complexity-control
title: Structural Risk Minimization (SRM)
understanding: 0
---

## Definition
Vapnik's model-selection procedure that controls generalization error by exploiting VC-dimension bounds rather than estimating optimism analytically (AIC/BIC) or by resampling (CV/bootstrap). SRM fits a nested sequence of model classes of increasing VC dimension h₁ < h₂ < ···, computes for each the probabilistic upper bound on test error Err_T (of the form err + correction(h, N, η) from VC theory), and selects the class minimizing that upper bound — trading training-error reduction against the complexity penalty implied by larger h. The bounds hold simultaneously over all functions in each class, so the search over the class is accounted for. Because VC bounds are typically very loose in absolute terms, SRM relies on the relative ordering of the bound across classes being informative; this can succeed for model selection even when the absolute error estimate is poor. Its principal limitation is computing (or even bounding) the VC dimension of each class. The support vector classifier is a notable case where the SRM program can be carried out successfully. Empirically (Hastie ESL), SRM's performance is mixed relative to AIC/BIC and to cross-validation/bootstrap, and is sensitive to the bound's tuning constants.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]