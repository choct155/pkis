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
id: pkis:concept:interest-and-emphasis
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- emphatic-td
- state-weighting
- value-prediction
- on-policy
title: Interest and Emphasis
understanding: 0
---

## Definition
A mechanism for steering limited function-approximation resources toward states we care about, generalizing the single on-policy distribution into a family. Interest I_t ≥ 0 is a (causally settable) random variable expressing how much we care about accurately valuing the state at time t; it reweights the distribution μ in the VE. Emphasis M_t multiplies the learning update, emphasizing or de-emphasizing the time-t update: M_t = I_t + γⁿ M_{t−n} (with M_t = 0 for t<0), and the n-step rule becomes w ← w + α M_t [G_{t:t+n} − v̂(S_t,w)] ∇v̂(S_t,w). In Example 9.4's four-state chain, ordinary methods converge to w = (3.5, 1.5), giving the only state of interest a value of 3.5, whereas interest/emphasis learn the leftmost state's value exactly (w₁ = 4) by never updating the uninteresting states. This is the on-policy precursor of the emphatic-TD methods developed for off-policy learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]