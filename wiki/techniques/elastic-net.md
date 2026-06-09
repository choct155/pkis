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
- optimization
id: pkis:technique:elastic-net
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch03
- hastie-esl-ch18
tags:
- regularization
- variable-selection
- regression
- sparsity
- L1
- L2
title: Elastic Net
understanding: 0
---

## Definition
A regularized regression penalty (Zou and Hastie, 2005) that combines the L1 (lasso) and L2 (ridge) penalties: lambda * sum_j ( alpha * beta_j^2 + (1 - alpha) * |beta_j| ). It was introduced as a practical and computationally tractable compromise between the lasso (q=1) and ridge regression (q=2) in the bridge L_q family, q in (1,2), of penalty (3.53). Whereas L_q penalties with 1 < q < 2 are differentiable at zero and therefore cannot set coefficients exactly to zero, and non-convex (q < 1) penalties make optimization hard, the elastic net retains the convexity of the lasso while behaving qualitatively like the L_q compromise. It does sparse variable selection like the lasso (the L1 part) while shrinking the coefficients of correlated predictors together like ridge (the L2 part), which stabilizes selection among correlated 'cousins' where the lasso would arbitrarily pick one. It has substantial computational advantages over the L_q penalties and is solvable by the same coordinate-descent and path machinery used for the lasso.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]