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
- statistics
id: pkis:concept:logit-pre-activation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- binary-logistic-regression
- multinomial-logistic-regression
related_concepts: []
sources:
- murphy-pml1-intro-ch10
tags:
- log-odds
- pre-activation
- softmax-input
- linear-classifier
- numerical-stability
title: Logit (Pre-activation)
understanding: 0
uses:
- activation-functions
---

## Definition
In the binary case, the **logit** is
$$a = w^Tx + b = \log\frac{p(y=1|x)}{p(y=0|x)}$$
the log-odds of the positive class. In the multiclass case the logit vector is $a = Wx + b\in\mathbb{R}^C$, with $a_c = \log p(y=c|x) + \text{const}$. The sigmoid or softmax transforms logits to probabilities.

### Why it matters
Logits are the natural output space for linear models and neural network classifier heads. Working in logit space (e.g., the log-sum-exp trick, hierarchical softmax, logit adjustment for class imbalance) is numerically stable and conceptually clean. Many loss functions (e.g., `CrossEntropyLoss` in PyTorch) accept unnormalised logits directly.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[activation-functions]] — uses
- [[multinomial-logistic-regression]] — prerequisite-of
- [[binary-logistic-regression]] — prerequisite-of
[To be populated during integration]