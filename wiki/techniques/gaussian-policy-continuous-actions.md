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
contrasts-with:
- policy-parameterization-softmax
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- deep-learning
id: pkis:technique:gaussian-policy-continuous-actions
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-policy-2018
tags:
- policy-gradient
- continuous-control
- gaussian-policy
- continuous-actions
- eligibility-vector
title: Gaussian Policy for Continuous Actions
understanding: 0
uses:
- policy-gradient-methods
- gaussian-distribution
---

## Definition
A policy parameterization for continuous (even infinite) action spaces that, instead of assigning a probability to each of many actions, learns the statistics of a probability distribution over actions. For a real-valued scalar action the policy is the normal density
$$\pi(a\mid s,\theta)\doteq\frac{1}{\sigma(s,\theta)\sqrt{2\pi}}\exp\!\left(-\frac{(a-\mu(s,\theta))^2}{2\sigma(s,\theta)^2}\right),$$
where the mean and standard deviation are state-dependent parametric function approximators.

## Parameterization
The parameter vector splits as $\theta=[\theta_\mu,\theta_\sigma]^\top$. The mean is typically linear, $\mu(s,\theta)=\theta_\mu^\top x_\mu(s)$, while the standard deviation must stay positive and so is the exponential of a linear function, $\sigma(s,\theta)=\exp(\theta_\sigma^\top x_\sigma(s))$, with feature vectors $x_\mu(s),x_\sigma(s)$. With these forms every algorithm in the chapter (REINFORCE, baseline, actor-critic) applies to continuous control.

## Eligibility Vector
The eligibility vector has two parts (Exercise 13.4):
$$\nabla\ln\pi(a\mid s,\theta_\mu)=\frac{1}{\sigma(s,\theta)^2}\bigl(a-\mu(s,\theta)\bigr)x_\mu(s),\qquad \nabla\ln\pi(a\mid s,\theta_\sigma)=\left(\frac{(a-\mu(s,\theta))^2}{\sigma(s,\theta)^2}-1\right)x_\sigma(s).$$
The mean update pushes toward sampled actions in proportion to their advantage; the variance update widens or narrows exploration depending on whether realized actions deviate more or less than the current spread. First shown by Williams (1987, 1992).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[policy-parameterization-softmax]] — contrasts-with: Softmax handles discrete action sets by per-action preferences; the Gaussian policy handles continuous action sets by learning distribution statistics instead.
- [[gaussian-distribution]] — uses: The continuous-action policy IS a state-conditioned Gaussian density; mean and (log) standard deviation are the learned function approximators.
- [[policy-gradient-methods]] — uses: Parameterizing a normal density over real-valued actions lets all policy-gradient algorithms handle continuous control.
[To be populated during integration]