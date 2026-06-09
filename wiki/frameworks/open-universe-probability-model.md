---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- knowledge-representation
id: pkis:framework:open-universe-probability-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch15
tags:
- existence-uncertainty
- identity-uncertainty
- number-statements
- generative-models
- first-order-probability
- BLOG
title: Open-Universe Probability Model
understanding: 0
---

## Definition
A first-order probability model on the standard (not database) semantics of first-order logic that allows uncertainty about WHICH objects exist (existence uncertainty) and WHICH terms refer to the same object (identity uncertainty), guaranteeing a unique consistent distribution over the infinite space of possible worlds. Where a Bayes net generates a world by assigning values to variables in topological order and an RPM extends this to sets of variables, an OUPM adds generative steps that create objects: number statements specify conditional distributions over how many objects of each type exist (often Poisson or order-of-magnitude/discrete-log-normal for unbounded counts), with origin functions recording each object's generation history so every world has exactly one generation sequence. The model is the triple (model, evidence, query); inference is approximate MCMC over partial worlds (minimal self-supporting instantiations) since worlds may be infinite. First realized in the BLOG language; applications include citation matching (CiteSeer/Google Scholar deduplication) and the NET-VISA seismic monitoring system deployed by the CTBTO.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]