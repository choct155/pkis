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
id: pkis:technique:reinforce-with-baseline
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-policy-2018
tags:
- policy-gradient
- variance-reduction
- baseline
- control-variate
- monte-carlo
title: REINFORCE with Baseline
understanding: 0
---

## Definition
A strict generalization of REINFORCE that subtracts a state-dependent baseline $b(s)$ from the return to reduce variance without introducing bias. The policy gradient theorem generalizes to
$$\nabla J(\theta)\propto\sum_s\mu(s)\sum_a\bigl(q_\pi(s,a)-b(s)\bigr)\nabla\pi(a\mid s,\theta),$$
valid for any $b(s)$ not depending on $a$, because $\sum_a b(s)\nabla\pi(a\mid s,\theta)=b(s)\nabla 1=0$. The resulting update is
$$\theta_{t+1}\doteq\theta_t+\alpha\bigl(G_t-b(S_t)\bigr)\frac{\nabla\pi(A_t\mid S_t,\theta_t)}{\pi(A_t\mid S_t,\theta_t)}.$$

## Why a Baseline Helps
The baseline leaves the expected update unchanged but can sharply reduce its variance, speeding learning (analogous to the average-reward baseline in gradient bandit algorithms, Section 2.8). Unlike the bandit case where the baseline is a scalar, for MDPs it should vary with state: in states where all actions have high value a high baseline is needed to distinguish them, and conversely for low-value states. A natural choice is a learned state-value estimate $\hat{v}(S_t,w)$, typically learned by a Monte Carlo method to match REINFORCE.

## Algorithm
The boxed algorithm maintains two step sizes, $\alpha^\theta$ and $\alpha^w$. Per episode step it computes $\delta\leftarrow G-\hat{v}(S_t,w)$, then $w\leftarrow w+\alpha^w\delta\nabla\hat{v}(S_t,w)$ and $\theta\leftarrow\theta+\alpha^\theta\gamma^t\delta\nabla\ln\pi(A_t\mid S_t,\theta)$.

## Connection
The baseline is precisely a control variate for the score-function (REINFORCE) gradient estimator; the same device appears in variational-inference gradient estimation. Greensmith, Bartlett, and Baxter (2004) analyze variance-optimal baselines.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]