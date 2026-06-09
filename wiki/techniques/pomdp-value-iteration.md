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
id: pkis:technique:pomdp-value-iteration
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch17
tags:
- pomdp
- value-iteration
- alpha-vectors
- conditional-plans
- piecewise-linear-convex
- dynamic-programming
title: POMDP Value Iteration (α-vectors)
understanding: 0
---

## Definition
An exact value-iteration algorithm for POMDPs that, instead of storing one utility number per state, maintains a set of undominated conditional plans, each represented by an α-vector α_p giving the utility α_p(s) of executing fixed conditional plan p from each physical state s. Two facts make this work: (1) the expected utility of a fixed depth-bounded conditional plan in belief state b is the linear function b·α_p, so it is a hyperplane over belief space; and (2) the optimal value function is the upper envelope U(b)=max_p b·α_p, which is therefore piecewise-linear and convex. The algorithm builds depth-(d+1) plans from depth-d plans via α_p(s)=Σ_{s'}P(s'|s,a)[R(s,a,s')+γΣ_e P(e|s')α_{p.e}(s')], then prunes plans dominated everywhere in belief space (the REMOVE-DOMINATED-PLANS step, typically solved as a linear program). Pruning is essential: the number of depth-d plans grows doubly exponentially (|A|^{O(|E|^{d-1})}), but most are dominated. The method is exact but hopelessly inefficient for realistic problems (even the 4×3 POMDP is too hard); it is the conceptual ancestor of the practical point-based value iteration methods (Pineau et al. 2003) that solve only for a finite reachable set of belief points.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]