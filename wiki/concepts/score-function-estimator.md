---
aliases: []
also_type: []
applies:
- policy-gradient-methods
- stochastic-vi
- elbo
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
- reinforcement-learning
generalizes:
- reinforce
id: pkis:concept:score-function-estimator
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
tags:
- gradient-estimation
- REINFORCE
- log-derivative-trick
- stochastic-optimization
- variance-reduction
title: Score Function Estimator (REINFORCE Gradient)
understanding: 0
uses:
- fisher-information
- monte-carlo-estimator
---

## Definition
The score function estimator (SFE) provides an unbiased Monte Carlo estimate of the gradient of an expectation whose sampling distribution depends on the parameters:
$$\nabla_\theta \mathbb{E}_{q_\theta(z)}[\tilde{L}(\theta,z)] = \mathbb{E}_{q_\theta(z)}\!\left[\tilde{L}(\theta,z)\,\nabla_\theta \log q_\theta(z)\right]$$
derived via the **log-derivative trick** $\nabla_\theta q_\theta(z) = q_\theta(z)\nabla_\theta \log q_\theta(z)$. An MC approximation draws $z_s \sim q_\theta$ and averages $\tilde{L}(\theta,z_s)\nabla_\theta \log q_\theta(z_s)$.

The estimator requires only that $q_\theta$ is differentiable, not $\tilde{L}$ itself, enabling **black-box** stochastic optimization.

### Why it matters
SFE (also called the likelihood-ratio estimator or REINFORCE) is the workhorse gradient estimator for discrete latent variables, reinforcement learning policy gradients, and black-box variational inference. Its main weakness is high variance, addressed via control variates (baselines) and Rao-Blackwellization.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[elbo]] — applies
- [[stochastic-vi]] — applies
- [[policy-gradient-methods]] — applies
- [[monte-carlo-estimator]] — uses
- [[fisher-information]] — uses
- [[reinforce]] — generalizes
[To be populated during integration]