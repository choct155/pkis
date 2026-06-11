---
aliases: []
also_type: []
applies:
- uncertainty-quantification
- predictive-model
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
extends:
- calibration
id: pkis:framework:conformal-prediction
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch14
tags:
- uncertainty-quantification
- coverage
- distribution-free
- prediction-intervals
- exchangeability
title: Conformal Prediction
understanding: 0
uses:
- exchangeability
---

## Definition
Given a **conformal score** $s(x,y) \in \mathbb{R}$ (large = less conforming) and $n$ exchangeable calibration examples, compute the adjusted $(1-\alpha)$-quantile
$$\hat{q} = \mathrm{Quantile}\!\left(\{s_i\}_{i=1}^n,\; \frac{\lceil(n+1)(1-\alpha)\rceil}{n}\right).$$
The **prediction set** for a new input $x_{n+1}$ is
$$\mathcal{T}(x_{n+1}) = \{y : s(x_{n+1},y) \leq \hat{q}\}.$$
**Coverage guarantee (finite-sample, distribution-free):**
$$1-\alpha \;\leq\; P^*(y_{n+1}\in\mathcal{T}(x_{n+1})) \;\leq\; 1-\alpha+\frac{1}{n+1}.$$
The only assumption is exchangeability of $(x_i,y_i)$.

### Why it matters
Conformal prediction is the leading framework for distribution-free, finite-sample valid uncertainty quantification. It wraps any base predictor and converts it into a set/interval predictor with certified coverage, without retraining, making it practically indispensable for safety-critical ML.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[predictive-model]] — applies
- [[calibration]] — extends
- [[exchangeability]] — uses
- [[uncertainty-quantification]] — applies
[To be populated during integration]