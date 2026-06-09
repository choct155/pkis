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
id: pkis:technique:stacking
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch08
tags:
- ensemble-methods
- model-combination
- cross-validation
- model-averaging
- leave-one-out
title: Stacked Generalization (Stacking)
understanding: 0
---

## Definition
Stacking combines the predictions of M models into a single prediction using estimated weights, but determines those weights from cross-validated (leave-one-out) predictions so that more complex models are not unfairly favored. With f-hat^{-i}_m(x) the prediction of model m fit with the i-th observation removed, the stacking weights solve w-hat^{st} = argmin_w sum_i [ y_i - sum_m w_m f-hat^{-i}_m(x_i) ]^2, and the final prediction is sum_m w-hat^{st}_m f-hat_m(x).

## Operational Mechanism
Fit each base model with each training point held out, regress the held-out targets y_i on the leave-one-out predictions, and apply the resulting weights to the full-data models. Using cross-validated predictions is what prevents the naive full-data regression (8.57) from collapsing all weight onto the largest / most complex model. Better results are obtained by constraining the weights to be nonnegative and to sum to 1 (a tractable quadratic program), which lets them be read as posterior model probabilities. The idea generalizes: any learner — not just linear regression — can be 'stacked' on top of the base models, and weights may depend on the input location x.

## Conditions
Stacking addresses the frequentist model-averaging problem (8.56): seeking weights minimizing E_P[Y - sum_m w_m f-hat_m(x)]^2, where the unavailable population regression (8.57) must be replaced by a training-set estimate. Restricting (8.59) to a single unit weight recovers leave-one-out cross-validation model selection; stacking instead combines models with optimal weights, typically improving prediction at the cost of interpretability.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]