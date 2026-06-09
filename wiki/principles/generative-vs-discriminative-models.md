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
- statistical-learning
- deep-learning
id: pkis:principle:generative-vs-discriminative-models
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch20
tags:
- classification
- modeling-paradigm
- decision-boundary
- joint-vs-conditional
title: Generative vs Discriminative Models
understanding: 0
---

## Definition
A distinction between two families of classifiers. A generative model learns the full joint distribution by modeling each class's distribution P(Inputs | Category) together with the class prior P(Category), from which the joint and hence anything can be computed (and samples generated). A discriminative model directly learns the decision boundary, i.e. the conditional P(Category | Inputs), and cannot generate inputs. Discriminative models tend to win in the large-data limit; generative models often win with little data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]