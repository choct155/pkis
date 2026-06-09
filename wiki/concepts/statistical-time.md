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
- causal-analysis
- time-series
id: pkis:concept:statistical-time
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch02
tags:
- temporal-bias
- arrow-of-time
- markov-chain
- screening-off
- reichenbach
title: Statistical Time
understanding: 0
uses:
- minimal-model-causation
---

## Definition
Pearl's device (Definition 2.8.1) for explaining why causal directions inferred from purely statistical dependencies tend to agree with physical time. Given an empirical distribution P, a *statistical time* of P is any ordering of the variables that agrees with at least one minimal causal structure consistent with P. Some processes admit many statistical times -- a scalar Markov chain can be oriented away from any chosen root, so its statistical time runs either with or against physical time -- while richer processes pin it down: a system of two coupled Markov chains (X_t,Y_t depending on X_{t-1},Y_{t-1}) has a *unique* statistical time, coinciding with physical time, and running IC on its samples (temporal labels suppressed) recovers the correct arrow of time. The concept formalizes the observed *temporal bias* of natural statistics: knowing the present commonly screens off the future (renders future components conditionally independent), but rarely screens off the past. The clashless coexistence over centuries of the temporal expectation (cause precedes effect) and the statistical expectation (a complete cause screens off its effects) is taken as evidence that natural statistics carry a built-in temporal asymmetry, linking the chapter's nontemporal inference machinery back to the arrow of time and Reichenbach's program.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[minimal-model-causation]] — uses: A statistical time is an ordering agreeing with some minimal causal structure consistent with P.
[To be populated during integration]