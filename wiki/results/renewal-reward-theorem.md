---
aliases: []
also_type: []
applies:
- renewal-process
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:result:renewal-reward-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- long-run-average
- asymptotic-theory
- operations-research
title: Renewal Reward Theorem
understanding: 0
uses:
- elementary-renewal-theorem
---

## Definition
Attach to each cycle of a renewal process a reward R_n (a cost, claim size, occupation time, etc.), with {R_n, n>=1} i.i.d. and E|R_1|<infinity (the R_n need not be independent of the {S_n}); the accumulated-reward process is R(t) = sum_{i=0}^{N(t)-1} R_i. The renewal reward theorem states that the long-run reward rate exists almost surely and equals the ratio of expected per-cycle reward to expected cycle length: lim_{t->infinity} R(t)/t = E R_1 / mu, where mu = E Y_1 in (0,infinity). The proof factors R(t)/t = (sum R_i / (N(t)-1)) * ((N(t)-1)/t) and applies the SLLN and elementary renewal theorem. Under mild extra conditions the result also holds in expectation, E R(t)/t -> E R_1/mu. A continuous-accumulation variant (cumulative process) with reward rate I_n on the n-th interval gives C(t)/t -> E[Y_1 I_0]/mu. The 'expected reward per cycle over expected cycle length' principle is the workhorse for long-run cost rates (e.g. maintenance budgeting) and long-run proportions (e.g. fraction of time a machine is up in an alternating renewal process).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[renewal-process]] — applies
- [[elementary-renewal-theorem]] — uses
[To be populated during integration]