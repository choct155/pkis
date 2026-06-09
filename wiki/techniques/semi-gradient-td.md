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
id: pkis:technique:semi-gradient-td
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
- sutton-reinforcement-2018-ch10
- sutton-reinforcement-2018-ch11
tags:
- temporal-difference
- bootstrapping
- value-prediction
- td-0
title: Semi-gradient TD Methods
understanding: 0
---

## Definition
Gradient-style value-prediction updates whose target is a bootstrapped estimate that itself depends on the current weight vector w_t—e.g. semi-gradient TD(0) with target U_t = R_{t+1} + γ v̂(S_{t+1},w), or the n-step variant with target G_{t:t+n}. Because the target depends on w_t, these are not true gradient-descent methods: they account for the effect of changing w on the estimate v̂(S_t,w) but ignore its effect on the target, so they include only part of the gradient—hence 'semi-gradient' (Barnard 1993). They sacrifice the robust convergence guarantees of true SGD but offer decisive practical advantages: substantially faster learning (lower variance, as in tabular TD), and the ability to learn continually and online without waiting for episode end, enabling use on continuing problems. n-step semi-gradient TD subsumes gradient Monte Carlo (n=∞) and semi-gradient TD(0) (n=1) as special cases.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]