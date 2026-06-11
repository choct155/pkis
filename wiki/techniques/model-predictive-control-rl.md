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
- control-theory
id: pkis:technique:model-predictive-control-rl
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch35
tags:
- planning-horizon
- model-based-rl
- sample-efficiency
- robotics
title: Model Predictive Control for RL (MPC/Receding-Horizon Control)
understanding: 0
---

## Definition
At each time step $t$, solve
$$a^*_{t:t+H-1} = \arg\max_{a_{t:t+H-1}} \mathbb{E}\!\left[\sum_{h=0}^{H-1} R(s_{t+h},a_{t+h}) + \hat{V}(s_{t+H})\right]$$
execute only $a^*_t$, observe the new state, and repeat. The expectation is over stochastic dynamics, and $H$ is the planning horizon. Also known as receding-horizon control.

### Why it matters
MPC decouples the difficulty of global policy representation from local planning: a compact learned model replaces a full policy. It naturally handles constraints, adapts online as the model improves, and connects RL to classical control (LQR, DDP). GP-MPC and PETS/PILCO variants achieve remarkable sample efficiency on robotic tasks.

### Variants
Special cases include LQG (linear dynamics, quadratic cost), differential dynamic programming (DDP), MCTS for discrete actions, and trajectory optimisation (shooting, collocation) for nonlinear continuous systems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]