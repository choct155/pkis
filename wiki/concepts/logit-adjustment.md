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
id: pkis:concept:logit-adjustment
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
tags:
- class-imbalance
- long-tail
- balanced-error-rate
- softmax
- discriminative-classifier
title: Logit Adjustment for Class Imbalance
understanding: 0
---

## Definition
$$\hat{f}(x) = \arg\max_{y \in Y}\, f_y(x) - \tau \log \pi_y$$

or equivalently, training with the loss

$$\ell(y, f(x)) = -\log \frac{e^{f_y(x)+\tau\log\pi_y}}{\sum_{y'} e^{f_{y'}(x)+\tau\log\pi_{y'}}}$$

where $\pi_y = p(y)$ is the empirical label prior and $\tau>0$ is a temperature. This shifts logits to account for class frequency, recovering the class-conditional likelihood $p(x|y)$ as the optimal predictor under balanced error rate.

### Why it matters
Standard softmax cross-entropy training is dominated by frequent classes. Logit adjustment provably optimises the balanced error rate (BER), requires no re-sampling, and can be applied post-hoc or integrated into training, making it a simple yet theoretically grounded remedy for long-tail recognition.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]