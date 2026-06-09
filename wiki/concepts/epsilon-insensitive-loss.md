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
- optimization
id: pkis:concept:epsilon-insensitive-loss
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch12
tags:
- loss-function
- robust
- sparsity
title: Epsilon-Insensitive Loss
understanding: 0
---

## Definition
The loss function underlying support vector regression: V_epsilon(r) = 0 if |r| < epsilon, and |r| - epsilon otherwise. It ignores residuals smaller than epsilon (defining an epsilon-wide 'tube' around the fit) and grows linearly beyond, in direct analogy to how SVM classification ignores points comfortably on the correct side of the margin. Two consequences distinguish it from squared-error and from Huber's robust loss: (1) its linear tails make the fit robust to large outliers (like Huber), and (2) its flat interior makes the fit insensitive to small residuals, which induces sparsity -- only observations outside the tube become support vectors.

## Contrast
Huber's loss V_H(r) is quadratic for |r| <= c and linear beyond, so it down-weights only the *tails*; the epsilon-insensitive loss additionally zeroes the *center*. Squared error penalizes everywhere and yields no sparsity. The parameter epsilon plays the same scale-dependent role for V_epsilon that c plays for V_H.

## Connections
- Used by [[support-vector-regression]]
- Contrasts with [[hinge-loss]] (classification analogue) and with squared-error / Huber loss

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]