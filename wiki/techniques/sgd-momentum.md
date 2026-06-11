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
- optimization
- deep-learning
id: pkis:technique:sgd-momentum
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
tags:
- gradient-descent
- momentum
- accelerated-optimization
- deep-learning
title: SGD with Momentum
understanding: 0
---

## Definition
The momentum algorithm augments SGD with a velocity variable $\mathbf{v}$ that accumulates an exponentially decaying moving average of past gradients:
$$\mathbf{v} \leftarrow \alpha\mathbf{v} - \epsilon\nabla_{\theta}\hat{J}(\theta), \qquad \theta \leftarrow \theta + \mathbf{v},$$
where $\alpha \in [0,1)$ is the momentum coefficient and $\epsilon$ is the learning rate. Terminal velocity in direction $-\mathbf{g}$ is $\frac{\epsilon\|\mathbf{g}\|}{1-\alpha}$, so $\alpha=0.9$ multiplies maximum speed by 10 relative to vanilla SGD.

Intuition: the particle analogy — a particle sliding on a frictionless surface accumulates speed in consistent gradient directions and damps oscillations across high-curvature directions, like viscous drag.

### Why it matters
Momentum accelerates convergence through high-curvature ravines (common in deep networks), where the gradient direction oscillates. Common values $\alpha \in \{0.5, 0.9, 0.99\}$ are typically ramped up during training. The Nesterov variant evaluates the gradient at the *lookahead* position $\theta + \alpha\mathbf{v}$, which improves the convergence rate from $O(1/k)$ to $O(1/k^2)$ in the convex batch case.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]