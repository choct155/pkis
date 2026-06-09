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
contrasts-with:
- collider-bias
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- bayesian-stats
id: pkis:concept:simpsons-paradox
instantiates:
- confounding
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch06
tags:
- causality
- association-vs-causation
- stratification
- aggregation
- reversal-effect
- contingency-tables
title: Simpson's Paradox
understanding: 0
uses:
- do-calculus
---

## Definition
Simpson's paradox (Simpson 1951; Blyth 1972; first noted by Pearson 1899) is the phenomenon in which an event C raises the probability of an event E in a population yet lowers it in every subpopulation: e.g. P(E|C) > P(E|¬C) while P(E|C,F) < P(E|¬C,F) and P(E|C,¬F) < P(E|¬C,¬F). Numerically this is unremarkable—conditional probabilities routinely change and even reverse sign under partitioning—so the 'paradox' is purely a clash of *causal* intuitions, not of probability calculus.

Pearl's resolution rests on the seeing/doing distinction: the inequality P(E|C) > P(E|¬C) reports that C is positive *evidence* for E, not that do(C) raises E. Reversal is shocking only because humans involuntarily read proportions as causal effects. Crucially, which table to consult—the aggregated or the stratified—is *not* decidable from the numbers: it depends on the causal role of the stratifying variable F. If F is a confounder (a common cause of C and E, e.g. F=gender) one must condition on F and read the subpopulation tables; if F is an intermediate variable affected by C (e.g. F=post-treatment blood pressure) one must *not* condition on F and should read the aggregated table. Two observationally equivalent causal models (Figs. 6.2a/b) yielding identical data can demand opposite decisions, proving the choice is driven by causal, not statistical, considerations—a special case of the covariate-selection / back-door problem. The non-existence of a 'miracle drug' harmful to every subpopulation yet beneficial overall is guaranteed by the Sure-Thing Principle, provided the action does not change the subpopulation distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[collider-bias]] — contrasts-with: whether to stratify depends on the variable's causal role: confounder (condition) vs collider/intermediate (do not condition)
- [[confounding]] — instantiates: the reversal under stratification is the canonical illustration of confounding by a common cause
- [[do-calculus]] — uses: the do-operator distinguishes seeing from doing, which dissolves the paradox
[To be populated during integration]