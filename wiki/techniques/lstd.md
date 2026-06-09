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
id: pkis:technique:lstd
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- temporal-difference
- linear-methods
- data-efficiency
- sherman-morrison
title: Least-Squares TD (LSTD)
understanding: 0
---

## Definition
The most data-efficient linear TD(0) prediction method (Bradtke & Barto 1996): rather than iterating toward the TD fixed point w_TD = A⁻¹ b, it forms direct estimates Â_t = Σ x_k (x_k − γ x_{k+1})ᵀ + εI and b̂_t = Σ R_{k+1} x_k, then computes w_t = Â_t⁻¹ b̂_t (the εI term guarantees invertibility; the 1/t normalizations cancel). The inverse is maintained incrementally via the Sherman–Morrison formula in O(d²) per step, versus O(d) for semi-gradient TD. LSTD needs no step-size α (only ε), but its O(d²) cost and the fact that it 'never forgets' are drawbacks: in control/GPI where π changes it must be paired with an explicit forgetting mechanism, mooting the no-step-size advantage. Worth its cost only when d is moderate, fast learning matters, and other system costs dominate.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]