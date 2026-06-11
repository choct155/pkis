---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- recommender-systems
id: pkis:problem:cold-start-problem
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- factorization-machines
related_concepts: []
sources:
- murphy-pml1-intro-ch22
specializes:
- distribution-shift
tags:
- side-information
- generalisation
- new-user
- new-item
title: Cold Start Problem
understanding: 0
---

## Definition
The **cold start problem** arises in recommender systems when a new user or new item has no (or very few) prior interaction records, making it impossible for pure collaborative-filtering models (which rely solely on the user/item id) to produce useful predictions.

### Why it matters
Cold start is a fundamental practical limitation: a pure matrix-factorisation model cannot embed an entity it has never seen. Solving it requires **side information** (content features, demographics, context) or meta-learning strategies so that predictions can be made from item/user attributes alone, motivating factorisation machines, content-based methods, and hybrid models.

### Connections
- [[distribution-shift]] — specializes
- [[factorization-machines]] — prerequisite-of
The cold start problem is an instance of distribution-shift / extrapolation failure and is directly addressed by factorisation machines and neural MF models that accept feature vectors rather than bare integer IDs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]