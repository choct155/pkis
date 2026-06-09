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
- optimization
- deep-learning
id: pkis:technique:monte-carlo-prediction
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch05
tags:
- reinforcement-learning
- monte-carlo
- policy-evaluation
- value-function
- first-visit
- every-visit
title: Monte Carlo Prediction (RL)
understanding: 0
---

## Definition
Monte Carlo prediction estimates the value function of a *fixed* policy $\pi$ purely by averaging sample returns observed from experience, with no model of the environment's dynamics. The state value is by definition the expected return, $v_\pi(s) = \mathbb{E}_\pi[G_t \mid S_t = s]$, so the natural estimator is the empirical average of returns following visits to $s$:
$$V(s) = \text{average of returns } G_t \text{ observed after visits to } s.$$
Returns are accumulated backward through each completed (episodic) trajectory via $G \leftarrow \gamma G + R_{t+1}$. Two variants differ in which visits count: **first-visit MC** averages the return following the *first* occurrence of $s$ in each episode; **every-visit MC** averages returns following *all* occurrences. First-visit returns are i.i.d. unbiased estimates of $v_\pi(s)$ with finite variance, so by the law of large numbers $V(s)\to v_\pi(s)$ and the standard error shrinks as $1/\sqrt{n}$; every-visit estimates are not independent but also converge. The same scheme estimates action values $q_\pi(s,a)$ by averaging returns following visits to a state-action pair.

### Why it matters
This is the foundational RL learning method: it shows you can learn value functions from raw sampled experience alone, with no transition probabilities. Crucially, MC prediction does **not bootstrap** — each state's estimate is independent of every other state's estimate — which (a) decouples computational cost from the size of the state space (you can evaluate a single state of interest by sampling only episodes through it), and (b) makes the method robust to violations of the Markov property. It is the policy-evaluation half of every Monte Carlo control method and the conceptual baseline against which bootstrapping methods (temporal-difference learning) are contrasted.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]