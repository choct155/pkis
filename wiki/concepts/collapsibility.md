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
- bayesian-stats
- statistical-learning
id: pkis:concept:collapsibility
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch06
tags:
- causality
- confounding
- effect-measures
- association-measures
- change-in-parameter
- noncollapsibility
title: Collapsibility
understanding: 0
---

## Definition
An association measure g[P(x,y)] is *collapsible* on a variable Z if its Z-stratified value, averaged over Z, equals its marginal value: E_z g[P(x,y|z)] = g[P(x,y)] (Definition 6.5.1). For any linear functional of P(y|x)—e.g. the risk difference P(y|x1) − P(y|x2)—collapsibility holds whenever Z is unassociated with X or unassociated with Y given X; hence any *violation* of collapsibility implies violation of both associational no-confounding conditions (U1) and (U2).

This near-coincidence led many to identify noncollapsibility with confounding, but Pearl shows the two are *distinct notions, neither implying the other*, even for linear effect measures (refuting the common belief that the divergence is peculiar to nonlinear measures such as odds or likelihood ratios). In Figure 6.3 the risk difference is *not* collapsible on Z (a barren proxy) for almost every parameterization, yet the effect is unconfounded for every parameterization. The genuine logical link runs through *stable* no-confounding: because noncollapsibility implies violation of (U1) and (U2), Theorem 6.4.4 yields Corollary 6.5.2—stable no-confounding implies collapsibility (contrapositive: noncollapsibility implies the effect is not stably unconfounded). This justifies the widespread change-in-parameter / change-in-estimate test for confounders as a quest for stable, not incidental, unbiasedness.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]