---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:concept:n-step-return
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch07
tags:
- reinforcement-learning
- return
- bootstrapping
- value-estimation
title: n-step Return
understanding: 0
---

## Definition
The n-step return is the update target used by n-step bootstrapping methods: G_{t:t+n} = R_{t+1} + gamma*R_{t+2} + ... + gamma^{n-1}*R_{t+n} + gamma^n * V_{t+n-1}(S_{t+n}). It is the actual discounted reward accumulated over n steps, truncated after n steps and then corrected for the missing remainder of the full return by the bootstrapped estimate gamma^n * V_{t+n-1}(S_{t+n}). If t+n >= T (the truncation reaches or passes termination) the missing terms are zero and G_{t:t+n} equals the ordinary full return G_t. The n-step return generalizes both the one-step TD target (n=1) and the Monte Carlo target (full return). A key theoretical property is the error reduction property: the worst-state error of the expected n-step return is at most gamma^n times the worst-state error of V_{t+n-1}, which guarantees that all n-step TD methods converge to the correct values under appropriate conditions. The return can be written recursively, G_{t:h} = R_{t+1} + gamma*G_{t+1:h}, a form exploited to derive per-decision and control-variate off-policy variants.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]