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
- statistics
- machine-learning
- deep-learning
id: pkis:concept:stochastic-gradient-langevin-dynamics
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
tags:
- mcmc
- langevin
- stochastic-gradient
- scalable-bayes
- sgd-connection
title: Stochastic Gradient Langevin Dynamics (SGLD)
understanding: 0
---

## Definition
An MCMC algorithm that replaces exact gradients in the Langevin update with mini-batch stochastic gradients:
$$\theta_{t+1} = \theta_t - \frac{\eta_t}{2}\nabla_B\mathcal{L}(\theta_t) + \epsilon_t, \quad \epsilon_t \sim \mathcal{N}(0, \eta_t I)$$
where $\nabla_B\mathcal{L}$ is the gradient estimated on a mini-batch of size $B$ and $\eta_t$ is a decaying step size.

### Why it matters
SGLD unifies stochastic optimisation and Bayesian posterior sampling: with decreasing step sizes and the MH step omitted (ULA regime), the iterates converge in distribution to the posterior $p(\theta|\mathcal{D})$. The mini-batch gradient noise plays the role of the injected Langevin noise, enabling posterior sampling at the cost of $O(B)$ gradient evaluations per step rather than $O(N)$, making approximate Bayesian inference scalable to large datasets. The connection formalises the sense in which SGD implicitly performs Bayesian inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]