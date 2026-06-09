---
aliases: []
also_type: []
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
id: pkis:result:elementary-renewal-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch03
tags:
- renewal-theory
- asymptotic-theory
- law-of-large-numbers
- central-limit-theorem
title: Elementary Renewal Theorem
understanding: 0
---

## Definition
Let mu = E Y_1 be the mean interarrival time. The elementary renewal theorem states that the renewal rate converges to 1/mu in two senses. (1) Strong-law form: if P[Y_0<infinity]=1 then N(t)/t -> 1/mu almost surely as t->infinity, obtained by sandwiching t/N(t) between S_{N(t)-1}/(N(t)-1) and S_{N(t)}/N(t) and applying the SLLN to {S_n}. (2) Mean form: t^{-1} U(t) -> 1/mu (and t^{-1} V(t) -> 1/mu in the delayed case) provided Y_0 < infinity a.s.; one direction uses Fatou's lemma, the reverse uses a truncation argument together with Wald's identity. If additionally sigma^2 = Var(Y_1) < infinity, a central limit theorem holds: N(t) is asymptotically normal, AN(mu^{-1}, t sigma^2 mu^{-3}). The mean form is the Cesaro-average counterpart of the sharper Blackwell theorem.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]