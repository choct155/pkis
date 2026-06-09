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
id: pkis:technique:flexible-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch12
tags:
- classification
- nonparametric-regression
- dimension-reduction
title: Flexible Discriminant Analysis (FDA)
understanding: 0
---

## Definition
A generalization of LDA that obtains nonlinear decision boundaries by replacing the linear regressions in the optimal-scoring formulation of LDA with flexible, nonparametric regression fits (generalized additive models, smoothing/additive splines, MARS, or kernel methods). Because many nonparametric regressions operate by basis expansion h(X) followed by a (penalized) linear fit, FDA amounts to performing LDA in an enlarged feature space; linear boundaries in the enlarged space map to nonlinear boundaries in the original space -- the same paradigm used by support vector machines. The criterion generalizes the average-squared-residual objective to ASR = (1/N) sum_l [ sum_i (theta_l(g_i) - eta_l(x_i))^2 + lambda J(eta_l) ], with J a roughness regularizer.

## Operational Mechanism
Replace the linear map eta_l(x) = x^T beta_l by a flexible fit eta_l(x); compute via the three-step optimal-scoring algorithm (multiresponse nonparametric regression of indicator matrix Y, eigen-decomposition for optimal scores, update). When the regression is a linear smoother S_lambda, the computation reduces to a single eigen-decomposition (a canonical-correlation problem). The reduced-rank subspace often gives the best classification, as seen on the vowel speech-recognition example.

## Connections
- Generalizes [[linear-discriminant-analysis]]
- Uses [[optimal-scoring]] as its computational engine
- Is analogous to [[support-vector-machines]] (linear boundary in an enlarged basis space)
- Often requires regularization, leading to [[penalized-discriminant-analysis]]

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]