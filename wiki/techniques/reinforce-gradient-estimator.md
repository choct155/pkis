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
- deep-learning
- generative-models
- reinforcement-learning
- optimisation
id: pkis:technique:reinforce-gradient-estimator
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- gradient-estimator
- discrete-stochastic
- score-function
- variance-reduction
title: REINFORCE Gradient Estimator
understanding: 0
---

## Definition
A Monte Carlo estimator of gradients of an expected cost with respect to distribution parameters, applicable when the output is discrete (non-differentiable):
$$\frac{\partial}{\partial\boldsymbol{\omega}}\mathbb{E}_{y\sim p(y;\boldsymbol{\omega})}[J(y)]=\mathbb{E}_{y\sim p}\!\left[J(y)\frac{\partial\log p(y;\boldsymbol{\omega})}{\partial\boldsymbol{\omega}}\right]\approx\frac{1}{m}\sum_{i=1}^m J(y^{(i)})\frac{\partial\log p(y^{(i)})}{\partial\boldsymbol{\omega}}.$$
Variance is reduced by subtracting a baseline $b(\boldsymbol{\omega})$ that does not depend on $y$; the optimal per-parameter baseline is:
$$b^*(\boldsymbol{\omega})_i=\frac{\mathbb{E}\left[J(y)\tfrac{\partial\log p}{\partial\omega_i}\right]^2}{\mathbb{E}\left[\tfrac{\partial\log p}{\partial\omega_i}\right]^2}.$$
Intuitively, REINFORCE reinforces actions (values of $y$) proportional to their associated reward $J(y)$.

### Why it matters
REINFORCE enables gradient-based training through discrete stochastic operations—essential for sigmoid belief nets, attention mechanisms, and any model emitting discrete tokens. It generalises the policy-gradient idea from reinforcement learning to supervised/generative settings; modern uses include training hard-attention models, discrete VAEs, and neural program synthesis.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]