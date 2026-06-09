---
aliases: []
also_type: []
applies:
- linear-discriminant-analysis
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
id: pkis:technique:optimal-scoring
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch12
tags:
- classification
- regression
- canonical-correlation
title: Optimal Scoring
understanding: 0
---

## Definition
A device that recasts linear discriminant analysis as a sequence of (multi-)linear regressions by assigning real-valued *scores* theta(g) to the class labels and choosing scores and regression coefficients jointly to minimize average squared residual. One solves min_{beta,theta} sum_i (theta(g_i) - x_i^T beta)^2 subject to normalization of theta (zero mean, unit variance) to avoid the trivial solution. Up to L <= K-1 mutually orthogonal score-and-coefficient pairs are extracted; the resulting discriminant directions equal the LDA canonical vectors up to scale, and the canonical distances reconstruct the Mahalanobis distance to each class centroid plus a class-independent term.

## Operational Mechanism
Form the N x K indicator response matrix Y. Fit a (possibly nonparametric) regression of Y on X giving linear smoother S_lambda with Y_hat = S_lambda Y. Compute the eigen-decomposition of Y^T Y_hat = Y^T S_lambda Y, normalizing eigenvectors Theta by Theta^T D_pi Theta = I where D_pi = Y^T Y / N is the diagonal of class priors. Update fits by eta(x) = Theta^T eta*(x); the first (trivial) function is constant, the remaining K-1 are the discriminant functions. When S_lambda is the linear projection H_X, optimal scoring reproduces LDA exactly.

## Why it matters
The regression formulation is modular: replacing the linear fit by any flexible regression (additive splines, MARS, kernels) immediately yields a more flexible discriminant analysis (FDA). It also sidesteps the masking pathology of naive indicator-regression classification, because the fits are transformed via the eigen-decomposition before classification.

## Connections
- [[linear-discriminant-analysis]] — applies: optimal scoring recasts LDA as a sequence of linear regressions
- Recasts [[linear-discriminant-analysis]] as regression
- Is the engine of [[flexible-discriminant-analysis]] and the M-step regression of [[mixture-discriminant-analysis]]
- Reduces to a [[singular-value-decomposition]]/canonical-correlation eigenproblem

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]