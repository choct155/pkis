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
id: pkis:technique:reparameterization-gradient
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
tags:
- gradient-estimation
- pathwise-derivative
- VAE
- stochastic-optimization
- continuous-relaxation
title: Reparameterization Gradient (Pathwise Derivative)
understanding: 0
---

## Definition
When $z \sim q_\theta(z)$ can be written as $z = g(\theta, \epsilon)$ for $\epsilon \sim q_0$ independent of $\theta$, the gradient of an expected loss can be pushed inside the expectation:
$$\nabla_\theta \mathbb{E}_{q_\theta(z)}[\tilde{L}(\theta,z)] = \mathbb{E}_{q_0(\epsilon)}\!\left[\nabla_\theta \tilde{L}(\theta, g(\theta,\epsilon))\right]$$
approximated by averaging $\nabla_\theta \tilde{L}(\theta, g(\theta,\epsilon_s))$ over samples $\epsilon_s \sim q_0$.

For a Gaussian, the canonical reparameterization is $z = \mu + \sigma\epsilon$, $\epsilon \sim \mathcal{N}(0,1)$.

### Why it matters
The reparameterization gradient has substantially lower variance than the score function estimator when $\tilde{L}$ is differentiable w.r.t. $z$. It is the core gradient estimator in variational autoencoders (VAEs) and normalizing flows. It requires differentiability of both $\tilde{L}$ and the transformation $g$, restricting direct use to continuous distributions.

### Total derivative
The gradient inside the expectation uses the **total derivative** accounting for both the direct dependence of $\tilde{L}$ on $\theta$ and the indirect path through $z=g(\theta,\epsilon)$: $\nabla_\theta^{\text{TD}}\tilde{L} = \nabla_z \tilde{L}\cdot J + \nabla_\theta \tilde{L}$ where $J = \partial z^\top/\partial\theta$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]