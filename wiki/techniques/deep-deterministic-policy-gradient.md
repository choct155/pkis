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
id: pkis:technique:deep-deterministic-policy-gradient
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch35
tags:
- continuous-actions
- off-policy
- actor-critic
- deterministic-policy
title: Deep Deterministic Policy Gradient (DDPG)
understanding: 0
---

## Definition
DDPG combines the deterministic policy gradient theorem with DQN-style tricks for continuous action spaces. The actor $\mu_\theta$ is updated via
$$\theta \leftarrow \theta + \eta_\theta\, \nabla_\theta \mu_\theta(s)\, \nabla_a Q_w(s,a)\big|_{a=\mu_\theta(s)}$$
and the critic $Q_w$ is updated by minimising
$$\mathcal{L}_{\mathrm{TD}}(s,a,r,s') = \left[Q_w(s,a) - \left(r + \gamma\, \overline{Q}(s',\bar{\mu}(s'))\right)\right]^2$$
where $\overline{Q}$ and $\bar{\mu}$ are slowly updated target networks. Experience replay and target networks (from DQN) are used to stabilise training.

### Why it matters
DDPG is the canonical off-policy, continuous-action actor-critic algorithm and is the foundation of TD3, D4PG, SAC, and many robotics learning systems. It avoids the argmax-over-actions computation intractable for continuous spaces by instead differentiating through the critic.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]