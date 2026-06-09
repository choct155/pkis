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
- deep-learning
id: pkis:technique:policy-parameterization-softmax
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-policy-2018
tags:
- policy-gradient
- softmax
- action-preferences
- discrete-actions
- eligibility-vector
title: Softmax Policy Parameterization in Action Preferences
understanding: 0
---

## Definition
The standard policy parameterization for discrete (and not-too-large) action spaces: define parameterized numerical action preferences $h(s,a,\theta)\in\mathbb{R}$ and convert them to a policy via an exponential soft-max distribution,
$$\pi(a\mid s,\theta)\doteq\frac{e^{h(s,a,\theta)}}{\sum_b e^{h(s,b,\theta)}}.$$
The preferences themselves may be parameterized arbitrarily, e.g. linearly in features $h(s,a,\theta)=\theta^\top x(s,a)$, or by a deep neural network (as in AlphaGo).

## Advantages over Action-Value epsilon-Greedy
(1) The policy can approach determinism: action preferences are driven to produce the optimal stochastic policy, and if the optimal policy is deterministic the optimal actions' preferences are driven arbitrarily high, whereas epsilon-greedy always retains an epsilon floor of random actions. (2) It can represent arbitrary action probabilities, enabling genuinely stochastic optimal policies (e.g. bluffing in Poker) that action-value methods cannot naturally find. (3) Note that taking a soft-max over action VALUES (rather than preferences) does NOT achieve this, since action values converge to fixed finite quantities yielding non-extreme probabilities.

## Eligibility Vector
For linear soft-max preferences, the eligibility vector (Exercise 13.3) is
$$\nabla\ln\pi(a\mid s,\theta)=x(s,a)-\sum_b\pi(b\mid s,\theta)\,x(s,b),$$
i.e. the feature of the taken action minus its expected feature under the current policy. The Bernoulli-logistic unit (Exercise 13.5) is the two-action special case, yielding the logistic function $P_t=1/(1+e^{-\theta^\top x})$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]