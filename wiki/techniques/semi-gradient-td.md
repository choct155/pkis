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
- gradient-monte-carlo
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
id: pkis:technique:semi-gradient-td
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
- sutton-reinforcement-2018-ch10
- sutton-reinforcement-2018-ch11
specializes:
- markov-decision-processes
tags:
- temporal-difference
- bootstrapping
- value-prediction
- td-0
title: Semi-gradient TD Methods
understanding: 0
uses:
- stochastic-gradient-descent
- linear-function-approximation-rl
- function-approximation-rl
- importance-sampling
---

## Definition
Gradient-style value-prediction updates whose target is a bootstrapped estimate that itself depends on the current weight vector w_t—e.g. semi-gradient TD(0) with target U_t = R_{t+1} + γ v̂(S_{t+1},w), or the n-step variant with target G_{t:t+n}. Because the target depends on w_t, these are not true gradient-descent methods: they account for the effect of changing w on the estimate v̂(S_t,w) but ignore its effect on the target, so they include only part of the gradient—hence 'semi-gradient' (Barnard 1993). They sacrifice the robust convergence guarantees of true SGD but offer decisive practical advantages: substantially faster learning (lower variance, as in tabular TD), and the ability to learn continually and online without waiting for episode end, enabling use on continuing problems. n-step semi-gradient TD subsumes gradient Monte Carlo (n=∞) and semi-gradient TD(0) (n=1) as special cases.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — specializes: Semi-gradient value-function approximation is a solution method for prediction in MDPs.
- [[importance-sampling]] — uses: Off-policy semi-gradient variants weight updates by the per-step IS ratio rho_t.
- [[function-approximation-rl]] — uses: Semi-gradient TD learns a parameterized value function, the core object of RL function approximation.
- [[linear-function-approximation-rl]] — uses: linear features give the simple update and the only setting with semi-gradient convergence guarantees
- [[stochastic-gradient-descent]] — uses: semi-gradient methods take an SGD-style step but include only part of the gradient
- [[gradient-monte-carlo]] — contrasts-with: semi-gradient bootstrapping targets depend on w so are not true gradient descent, unlike unbiased MC targets
[To be populated during integration]