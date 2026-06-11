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
contrasts-with:
- overfitting-and-underfitting
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- learning-theory
extends:
- bias-variance-tradeoff
id: pkis:concept:bayes-error-rate
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch11
tags:
- irreducible-error
- fundamental-limits
- learning-theory
title: Bayes Error Rate
understanding: 0
uses:
- cover-hart-theorem
---

## Definition
The **Bayes error rate** is the irreducible minimum error achievable by any classifier on a given input distribution:

$$\epsilon^* = 1 - \mathbb{E}_{\mathbf{x}}\left[\max_y P(Y = y \mid \mathbf{x})\right].$$

It arises from label noise, overlapping class-conditional distributions, or features that do not fully determine the output, and cannot be reduced by any amount of data or algorithmic improvement.

### Why it matters
Setting a realistic performance target requires knowing the floor set by the Bayes error. If a model's error approaches this floor, gathering more data or increasing capacity will not help; the task itself is intrinsically ambiguous. In practice, human-level performance serves as a proxy for the Bayes error when the true distribution is unknown.

### Relationship to human-level performance
Human performance on perceptual tasks is often used as a practical upper bound on what is learnable, motivating metrics like 98% accuracy (human-level) in the Street View transcription example.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[overfitting-and-underfitting]] — contrasts-with
- [[cover-hart-theorem]] — uses: Cover-Hart theorem bounds the nearest-neighbour error relative to Bayes error
- [[bias-variance-tradeoff]] — extends: Bayes error is the irreducible component not captured by bias-variance decomposition
[To be populated during integration]