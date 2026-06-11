---
aliases: []
also_type: []
analogous-to:
- hinge-loss
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
- cross-entropy-loss
- hinge-loss
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:exponential-loss
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch14
- murphy-pml1-intro-ch18
tags:
- loss-function
- boosting
- margin
- classification
title: Exponential Loss Function
understanding: 0
uses:
- adaboost
---

## Definition
$$L(y, t) = \exp(-t\,y), \quad t\in\{-1,+1\}$$

A margin-based loss that penalises misclassified examples ($ty < 0$) exponentially while rewarding confident correct predictions.

### Why it matters
The exponential loss is the objective implicitly minimised by AdaBoost through sequential greedy optimisation. Its population minimiser is $y^*(x)=\frac{1}{2}\ln\frac{p(t=1|x)}{p(t=-1|x)}$, i.e. half the log-odds, so the sign of the combined classifier recovers the Bayes decision boundary. Compared with cross-entropy, the exponential loss is far less robust to outliers (it grows exponentially rather than linearly for large $|ty|$) and cannot be interpreted as the log-likelihood of any valid probabilistic model, nor does it extend naturally to $K>2$ classes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hinge-loss]] — contrasts-with: both are margin-based surrogates for 0-1 loss
- [[adaboost]] — uses
- [[hinge-loss]] — analogous-to
- [[cross-entropy-loss]] — contrasts-with
[To be populated during integration]