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
id: pkis:concept:class-imbalance-long-tail
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch10
tags:
- class-imbalance
- long-tail
- resampling
- logit-adjustment
- rare-classes
title: Class Imbalance and Long-tail Distributions
understanding: 0
---

## Definition
A setting in which the class frequency distribution $p(N_1,\ldots,N_C)$ is highly skewed, with a small number of frequent classes and many rare ones (a **long tail**). Training on imbalanced data biases models toward majority classes. Mitigation strategies include:
- **Instance-balanced sampling** ($q=1$): $p_c \propto N_c$
- **Class-balanced sampling** ($q=0$): $p_c = 1/C$
- **Square-root sampling** ($q=0.5$): $p_c \propto \sqrt{N_c}$
- **Bias initialisation**: set $b_c$ so that $\text{softmax}(b)_c = N_c/N$
- **Logit adjustment** and **nearest class mean classifiers**

### Why it matters
Long-tail distributions are the norm in natural language, biology, and e-commerce. Standard cross-entropy training implicitly weights loss by class frequency, resulting in poor recall on rare classes despite high overall accuracy.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]