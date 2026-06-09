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
- statistical-learning
- bayesian-stats
id: pkis:concept:family-wise-error-rate
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch18
tags:
- multiple-testing
- fwer
- bonferroni
- type-i-error
title: Family-Wise Error Rate (FWER)
understanding: 0
uses:
- hypothesis-testing
---

## Definition
In a family of M hypothesis tests, the family-wise error rate is the probability of making at least one false rejection: FWER = Pr(∪_j A_j) = Pr(V ≥ 1), where A_j is the event that the j-th true null is rejected. For independent level-α tests FWER = 1−(1−α)^M, which approaches 1 as M grows; positive dependence between tests (common in genomics) lowers it below this bound. The Bonferroni method controls FWER ≤ α by tightening each test to threshold α/M (reject H0j if p_j < α/M), a simple union-bound guarantee that holds regardless of dependence but is too conservative for large M, calling far too few features significant. FWER control contrasts sharply with false-discovery-rate control: bounding the probability of any error is much stricter than bounding the expected fraction of erroneous discoveries.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hypothesis-testing]] — uses
[To be populated during integration]