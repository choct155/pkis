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
- probabilistic-methods
- robotics
id: pkis:technique:pilco
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch35
tags:
- gaussian-process
- model-based-rl
- sample-efficiency
- continuous-control
title: PILCO (Probabilistic Inference for Learning Control)
understanding: 0
---

## Definition
PILCO models the transition function $f$ with a Gaussian process: $s_{t+1} = f(s_t, a_t) + \epsilon_t$, $\epsilon_t\sim\mathcal{N}(0,\Sigma)$. The policy objective
$$J(\pi_\theta) = \sum_{t=1}^T \mathbb{E}[c(s_t)]$$
and its gradient $\nabla_\theta J$ are computed *deterministically* by propagating Gaussian belief states through the GP via moment matching, enabling gradient-based (Levenberg-Marquardt) policy optimisation without stochastic rollouts.

### Why it matters
PILCO achieves extraordinary sample efficiency on continuous control tasks (e.g., cart-pole swing-up learned from ~17 seconds of real interaction), because the GP captures uncertainty over dynamics and the deterministic gradient propagation avoids Monte Carlo noise. It established GP-based MBRL as a leading approach for low-data robotics settings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]