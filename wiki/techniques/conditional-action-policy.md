---
aliases: []
also_type: []
applies:
- markov-decision-processes
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
- causal-analysis
- bayesian-stats
extends:
- do-calculus
id: pkis:technique:conditional-action-policy
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch04
tags:
- causality
- interventions
- policy
- do-calculus
- decision-analysis
- pearl
title: Conditional and Stochastic Action Policies
understanding: 0
uses:
- do-calculus
---

## Definition
An extension of the primitive intervention do(X=x) to interventions where X is made to respond to other variables — 'do x if you see z' (deterministic policy X=g(z)) or 'do x with probability p if you see z' (stochastic policy P*(x|z)). Pearl (1994b) shows their evaluation reduces to the same identifiable kernel as primitive interventions, P(y|x̂,z): for a deterministic policy, P(y|do(X=g(z))) = E_z[P(y|x̂,z)|_{x=g(z)}], because Z (a nondescendant of X) keeps its observed distribution P(z) under the policy. For a stochastic policy, P(y)|_{P*(x|z)} = Σ_{x,z} P(y|x̂,z) P*(x|z) P(z). Thus identifiability of P(y|x̂,z) is necessary and sufficient for identifying any such policy; the conditional criterion is strictly stronger than for unconditional do(x), since conditioning on Z can create dependencies that block reduction to a hat-free expression. STRIPS-like planning actions whose effect X=x is gated by an enabling precondition C(w) are a special case, encoded by setting P*(x|z) to the natural mechanism when C is false and to a point mass when C is true.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — applies
- [[do-calculus]] — uses
- [[do-calculus]] — extends
[To be populated during integration]