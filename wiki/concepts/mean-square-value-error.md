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
- reinforcement-learning
- optimization
id: pkis:concept:mean-square-value-error
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- objective-function
- prediction
- value-function
title: Mean Square Value Error (VE)
understanding: 0
---

## Definition
The objective for value prediction under approximation: VE(w) = Σ_s μ(s) [v_π(s) − v̂(s,w)]², the μ-weighted squared difference between the true and approximate state values. The state distribution μ(s) ≥ 0, Σ_s μ(s) = 1, encodes how much we care about error at each state; under on-policy training it is the on-policy distribution (fraction of time spent in s). A continuous objective is necessary precisely because, with d ≪ |S|, no w makes every state exactly correct—improving one state's estimate necessarily worsens others, so we must declare which states matter. The square root (root VE) is used in plots. The global optimum w* minimizes VE over all w; for nonlinear approximators only a local optimum (or, in some RL cases, no convergence guarantee at all) is typically achievable. VE is not provably the right objective—the goal is ultimately a better policy—but no clearly better surrogate is known.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]