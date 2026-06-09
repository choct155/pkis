---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- information-theory
id: pkis:principle:robustness-implies-optimality
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch21
tags:
- robustness
- optimality
- decision-theory
- jaynes
- methodology
title: Any Well-Defined Inference Property Implies an Optimality Principle
understanding: 0
---

## Definition
Jaynes's logical rebuttal to the exploratory/robustness school (Tukey, Mosteller) that deprecates optimality criteria. The argument: as soon as any intuitively desirable inference property — 'robustness', 'resistance', etc. — is defined precisely enough to permit **transitive comparisons** between estimators (so that one can be said to be 'more robust' than another), then within any feasible set of estimators there must exist an optimally-robust one. Hence an optimality principle follows inexorably; one cannot consistently advocate a well-defined inference property while rejecting optimality.

Two corollaries sharpen the point. (1) **Robustness has a price**: robust/resistant qualities are bought with poorer performance when the model is correct, since the most robust procedure of all — ignoring data, model, and prior alike — is useless. Advocates therefore owe a statement of the trade-off they ask us to accept. (2) **Robustness trades information for insensitivity**: the sample median is 'more robust' than the mean only because it is insensitive to most of the data (values above/below it can move arbitrarily without changing it), discarding relevant information. Combined with Cox's theorems (a consistent normative theory of rational inference must be Bayesian), this implies the proper response to model uncertainty is not ad hoc robust recipes but a sufficiently flexible Bayesian model, which delivers robustness automatically when desirable and optimal performance when the model is trusted.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]