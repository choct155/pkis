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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
id: pkis:technique:actor-critic
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-policy-2018
tags:
- policy-gradient
- temporal-difference
- bootstrapping
- actor
- critic
- advantage
- A2C
- eligibility-traces
title: Actor-Critic Methods
understanding: 0
---

## Definition
Policy-gradient methods that learn BOTH a parameterized policy (the 'actor') and a parameterized state-value function (the 'critic'), where the critic is used to assess (criticize) the actor's action selections via bootstrapping. The defining move beyond REINFORCE-with-baseline is that the value function is applied to the SECOND state of a transition, so the discounted bootstrapped one-step return $G_{t:t+1}=R_{t+1}+\gamma\hat{v}(S_{t+1},w)$ is used to evaluate the action. The one-step actor-critic update is
$$\theta_{t+1}\doteq\theta_t+\alpha\bigl(R_{t+1}+\gamma\hat{v}(S_{t+1},w)-\hat{v}(S_t,w)\bigr)\frac{\nabla\pi(A_t\mid S_t,\theta_t)}{\pi(A_t\mid S_t,\theta_t)} = \theta_t+\alpha\,\delta_t\,\nabla\ln\pi(A_t\mid S_t,\theta_t),$$
with TD error $\delta_t$, paired with semi-gradient TD(0) for the critic.

## Baseline vs. Critic
In REINFORCE-with-baseline the value function estimates only the first state of a transition: it sets a baseline but, being computed before the action, cannot assess that action, so no bias is introduced. A true critic uses the second state's value through bootstrapping, which DOES introduce bias but, like all TD methods, trades it for substantially reduced variance and the benefits of online, incremental, fully bootstrapped learning. The actor would be biased even if the critic were learned by Monte Carlo; the bias comes from bootstrapping in the gradient estimate, not from how the critic is trained.

## Variants
One-step actor-critic generalizes to n-step returns ($G_{t:t+n}$), to a $\lambda$-return forward view, and to a backward view using separate eligibility traces $z^\theta$ and $z^w$ for actor and critic. The continuing case uses the differential (average-reward) return with an estimated $\bar{R}$. In modern literature these are often called advantage actor-critic (A2C) methods, since $\delta_t$ estimates the advantage. The presentation follows Degris, White, and Sutton (2012).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]