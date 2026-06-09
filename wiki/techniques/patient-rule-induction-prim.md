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
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:patient-rule-induction-prim
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch09
tags:
- rule-induction
- exploratory-analysis
- feature-space-partitioning
title: Patient Rule Induction Method (PRIM)
understanding: 0
---

## Definition
PRIM finds axis-aligned boxes in the feature space within which the response average is high (bump hunting); minima are found by negating the response. Unlike tree methods, the boxes are not defined by a binary tree, which complicates interpreting the collection but makes individual rules simpler. The core top-down peeling starts with a box containing all data and repeatedly compresses one face, peeling off a small proportion alpha (typically 0.05-0.10) of observations from whichever face (highest or lowest values of some X_j) leaves the largest box mean; peeling stops at a minimum box occupancy (say 10). A bottom-up pasting pass then expands any face that increases the box mean, recovering from the greedy peeling. Cross-validation plus analyst judgment selects the box size from the resulting sequence. The observations in the chosen box B_1 are removed and the whole top-down/bottom-up process is repeated to yield further boxes B_2, B_3, ..., each described by a conjunction of interval rules on a subset of predictors. PRIM's principal advantage over CART is patience: with N points and split fraction alpha it can take roughly -log(N)/log(1-alpha) peeling steps versus CART's log_2(N)-1 binary splits before exhausting data, helping the greedy search find better solutions. Handles categorical predictors and missing values like CART; designed for quantitative response (two-class handled by 0/1 coding, multiclass only via one-vs-baseline runs).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]