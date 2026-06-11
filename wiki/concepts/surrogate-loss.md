---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:surrogate-loss
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch04
tags:
- 0-1-loss
- hinge-loss
- log-loss
- classification
- convex-optimisation
title: Surrogate Loss Function
understanding: 0
---

## Definition
A surrogate loss $\tilde{\ell}(\tilde{y}, \eta)$ is a convex, differentiable upper bound on a target loss (typically the 0-1 loss) used to enable efficient gradient-based optimisation:
$$\ell_{01}(\tilde{y}, \eta) \leq \tilde{\ell}(\tilde{y}, \eta) \quad \forall\, \tilde{y}, \eta$$
where $\eta = f(x;\theta)$ is the decision score and $\tilde{y}\eta$ is the **margin**.

Common surrogates: **log-loss** $\log(1 + e^{-\tilde{y}\eta})$ (smooth, differentiable everywhere) and **hinge-loss** $\max(0, 1-\tilde{y}\eta)$ (piecewise-linear, used in SVMs).

### Why it matters
Minimising the 0-1 loss directly is NP-hard. Surrogate losses preserve the key property (upper-bounding misclassification) while being tractable. The tightness of the bound and whether calibrated probability estimates are produced (log-loss yes, hinge-loss no) guide the choice of surrogate in practice.

### Margin
The margin $m = \tilde{y}\eta$ measures the confidence and correctness of a prediction: $m > 0$ implies a correct classification, $m < 0$ an error. Both log-loss and hinge-loss are decreasing functions of $m$, incentivising large positive margins.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]