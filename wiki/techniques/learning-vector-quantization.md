---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- k-means-clustering
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
extends:
- k-means-clustering
id: pkis:technique:learning-vector-quantization
instantiates:
- prototype-methods
- vector-quantization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch13
tags:
- classification
- online-learning
- prototype-methods
- competitive-learning
title: Learning Vector Quantization (LVQ)
understanding: 0
---

## Definition
An online prototype-classification method (Kohonen, 1989) that places prototypes strategically with respect to the decision boundaries: training points attract prototypes of their own class and repel prototypes of competing classes, so when iterations settle the prototypes lie near same-class training points but away from boundaries. LVQ1 starts with R prototypes per class (e.g. R random training points per class, or the K-means solution as initial values), then repeatedly samples a training point x_i, finds its closest prototype m_j(k), and updates it: if classes match (g_i = k) move toward the point, m_j(k) <- m_j(k) + eps(x_i - m_j(k)); if they differ move away, m_j(k) <- m_j(k) - eps(x_i - m_j(k)). The learning rate eps is decreased toward zero with each iteration following stochastic-approximation guidelines. Variants LVQ2, LVQ3 can improve performance. Unlike K-means classification, all data influence all prototype positions, so prototypes migrate away from boundaries. A key drawback: LVQ is defined by an algorithm rather than the optimization of a fixed criterion, making its statistical properties hard to characterize. Empirically it performs nearly identically to K-means classification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[vector-quantization]] — instantiates: LVQ is the supervised, label-aware form of vector quantization.
- [[k-means-clustering]] — contrasts-with: LVQ positions prototypes away from boundaries using inter-class repulsion; per-class K-means ignores other classes.
- [[k-means-clustering]] — extends: LVQ refines K-means prototype placement using all classes' data, often initialized from the K-means solution.
- [[prototype-methods]] — instantiates: LVQ is a prototype-classification method.
[To be populated during integration]