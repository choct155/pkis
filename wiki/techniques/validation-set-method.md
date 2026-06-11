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
- statistics
- machine-learning
id: pkis:technique:validation-set-method
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch04
tags:
- hyperparameter-selection
- model-selection
- LOO-CV
- one-SE-rule
title: Validation Set and Cross-Validation
understanding: 0
---

## Definition
$$R^{\text{cv}}_\lambda \triangleq \frac{1}{K}\sum_{k=1}^{K} R_0\!\left(\hat{\theta}_\lambda(\mathcal{D}_{-k}),\, \mathcal{D}_k\right)$$

Cross-validation (CV) estimates population risk by partitioning the training data into $K$ folds, training on $K-1$ folds and evaluating on the held-out fold, rotating through all folds; the hyperparameter $\lambda^* = \operatorname{argmin}_\lambda R^{\text{cv}}_\lambda$ is selected to minimise this averaged risk.

### Why it matters
CV is the standard method for hyperparameter selection (regularisation strength, model architecture choices) when a dedicated test set is unavailable or data is scarce. Leave-one-out CV ($K=N$) is nearly unbiased but expensive; $K=5$ or $K=10$ offers a practical bias-variance trade-off. The **one-standard-error rule** selects the simplest model whose CV risk is within one standard error of the best model's risk, adding robustness against noise in the CV estimates.

### Population risk
The validation risk $R^{\text{val}}_\lambda = R_0(\hat{\theta}_\lambda(\mathcal{D}_{\text{train}}), \mathcal{D}_{\text{valid}})$ estimates population risk $\mathbb{E}_{p^*}[\ell(y, f(x;\hat{\theta}))]$; CV aggregates this estimate across multiple held-out folds to reduce variance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]