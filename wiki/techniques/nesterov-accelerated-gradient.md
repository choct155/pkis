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
- optimization
- machine-learning
extends:
- gradient-descent
id: pkis:technique:nesterov-accelerated-gradient
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- adam-optimizer
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- momentum
- accelerated-gradient
- convex-optimization
- first-order
title: Nesterov Accelerated Gradient
understanding: 0
uses:
- strong-convexity
---

## Definition
**Nesterov accelerated gradient (NAG)** modifies gradient descent with a momentum look-ahead step:

$$\tilde{\theta}_{t+1} = \theta_t + \beta(\theta_t - \theta_{t-1})$$
$$\theta_{t+1} = \tilde{\theta}_{t+1} - \eta_t \nabla L(\tilde{\theta}_{t+1})$$

Equivalently, the momentum vector is updated using the gradient at the *predicted* next location $\theta_t + \beta m_t$:

$$m_{t+1} = \beta m_t - \eta_t \nabla L(\theta_t + \beta m_t), \quad \theta_{t+1} = \theta_t + m_{t+1}$$

For convex objectives with Lipschitz-continuous gradients and appropriately chosen $\beta, \eta_t$, NAG achieves a convergence rate of $O(1/t^2)$ vs. $O(1/t)$ for vanilla gradient descent — the optimal rate for first-order methods on this function class.

### Why it matters
NAG is the theoretical gold-standard for first-order convex optimization, and the look-ahead intuition is directly carried into Adam and other adaptive methods used in deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[adam-optimizer]] — prerequisite-of
- [[strong-convexity]] — uses
- [[gradient-descent]] — extends
[To be populated during integration]