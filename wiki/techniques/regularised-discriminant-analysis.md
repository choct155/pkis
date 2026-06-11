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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:regularised-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- classification
- regularisation
- covariance-estimation
- LDA
title: Regularised Discriminant Analysis (RDA)
understanding: 0
---

## Definition
$$\hat{\Sigma}_{\text{map}} = \lambda\,\text{diag}(\hat{\Sigma}_{\text{mle}}) + (1-\lambda)\hat{\Sigma}_{\text{mle}}, \quad \lambda \in [0,1]$$

RDA interpolates between the full MLE covariance and its diagonal, acting as a MAP estimator of a shared Gaussian covariance in LDA. The scalar $\lambda$ controls regularisation strength, shrinking the off-diagonal entries towards zero to improve conditioning when $N_c \ll D$.

### Why it matters
The MLE covariance $\hat{\Sigma}$ is ill-conditioned whenever the number of examples per class is small relative to feature dimensionality. RDA provides a one-parameter family that spans naive diagonal LDA ($\lambda=1$) to full LDA ($\lambda=0$), and can be tuned by cross-validation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]