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
id: pkis:technique:softmax-action-selection
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- action-selection
- softmax
- boltzmann
- policy
- preferences
title: Softmax (Boltzmann) Action Selection
understanding: 0
---

## Definition
$$\Pr\{A_t = a\} \doteq \frac{e^{H_t(a)}}{\sum_{b=1}^k e^{H_t(b)}} \doteq \pi_t(a)$$

A stochastic policy that maps real-valued *action preferences* $H_t(a)$ to selection probabilities via the soft-max (Gibbs/Boltzmann) distribution: higher-preference actions are chosen more often, in a graded probabilistic manner.

### Preferences vs. values
Preferences $H_t(a) \in \mathbb{R}$ carry no reward interpretation; only *relative* preferences matter, since adding a constant to all $H_t(a)$ leaves $\pi_t$ unchanged. Initializing all preferences equal (e.g. $H_1(a)=0$) gives a uniform policy. The exponential form guarantees a valid probability distribution over actions.

### Relation to logistic/sigmoid
With two actions the soft-max reduces to the logistic (sigmoid) function used pervasively in statistics and neural networks, making it the multi-action generalization of the logistic link.

### Why it matters
Soft-max action selection is the bridge from value-based bandit methods to *policy-based* reinforcement learning. A parameterized policy expressed as a soft-max over preferences is exactly what policy-gradient and actor–critic methods optimize, and the same distribution appears in Boltzmann exploration, energy-based models, and the output layer of classifiers. It supplies a differentiable policy whose preferences can be trained by gradient ascent on expected reward.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]