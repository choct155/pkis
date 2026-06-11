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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- recommender-systems
id: pkis:concept:implicit-feedback-recommendation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-personalized-ranking
related_concepts: []
sources:
- murphy-pml1-intro-ch22
tags:
- positive-only
- pairwise-ranking
- BPR
- user-behavior
title: Implicit Feedback in Recommendation
understanding: 0
---

## Definition
Implicit feedback encodes user preferences indirectly through observed behaviour (clicks, watches, purchases) rather than explicit ratings. The resulting data are **positive-only**: interaction $(u, i)$ signals that user $u$ prefers item $i$ over unobserved items, but the absence of interaction is ambiguous — it could indicate dislike or merely lack of exposure.

### Why it matters
Implicit feedback is far more abundant than explicit ratings in real systems. Treating all unobserved pairs as negatives introduces systematic bias, so methods like BPR that sample negatives or weight observations are essential. The positive-only nature also connects to semi-supervised and PU (positive-unlabelled) learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-personalized-ranking]] — prerequisite-of
[To be populated during integration]