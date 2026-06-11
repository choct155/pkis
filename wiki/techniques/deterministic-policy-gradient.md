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
- reinforcement-learning
- optimization
id: pkis:technique:deterministic-policy-gradient
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch35
tags:
- continuous-actions
- off-policy
- policy-gradient
- actor-critic
title: Deterministic Policy Gradient (DPG)
understanding: 0
---

## Definition
For a deterministic policy $a=\mu_\theta(s)$ in continuous action spaces, the gradient of the expected return is
$$\nabla_\theta J(\mu_\theta) = \frac{1}{1-\gamma}\mathbb{E}_{p_{\mu_\theta}^\infty(s)}\!\left[\nabla_\theta\mu_\theta(s)\,\nabla_a Q_{\mu_\theta}(s,a)\big|_{a=\mu_\theta(s)}\right]$$
The gradient integrates over states but *not* over actions, reducing variance compared to stochastic policy gradients. Because the deterministic policy does not explore, data must be collected by a separate stochastic behaviour policy $\beta$ (off-policy).

### Why it matters
DPG (Silver et al. 2014) enables efficient gradient-based policy optimisation in high-dimensional continuous action spaces where argmax over actions is intractable and stochastic policy gradients suffer from high variance. It is the theoretical foundation of DDPG, TD3, D4PG, and SAC (in its deterministic limit).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]