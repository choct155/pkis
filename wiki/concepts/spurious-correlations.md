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
- causality
id: pkis:concept:spurious-correlations
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- distribution-shift
- generalization
- shortcut-learning
- causality
title: Spurious Correlations (Shortcut Features)
understanding: 0
---

## Definition
Spurious correlations (also called **shortcut features**) are statistical associations between input features and labels in the training distribution that do not reflect a stable causal or generalizable relationship, and therefore fail to transfer to other distributions.

### Why it matters
Deep models tend to preferentially exploit spurious features because they are often simpler (lower-complexity solutions) under standard ERM. Classic examples include grassy backgrounds predicting 'cow', metal tokens in X-rays predicting pneumonia, and gendered pronouns flipping sentiment predictions. Spurious correlations are a root cause of covariate and domain shift failures.

### Mitigation strategies
Methods to reduce reliance on spurious features include data augmentation, distributionally robust optimization (DRO), invariant risk minimization (IRM), causal data augmentation, and domain adversarial learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]