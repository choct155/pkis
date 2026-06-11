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
id: pkis:concept:nu-svm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
tags:
- svm
- model-selection
- soft-margin
- classification
- regression
title: ν-SVM
understanding: 0
---

## Definition
The $\nu$-SVM (Schölkopf et al., 2000) re-parameterises the soft-margin SVM by replacing the cost parameter $C$ with $\nu \in (0,1]$, which simultaneously serves as:
- an **upper bound** on the fraction of margin errors (points with $\xi_n > 0$), and
- a **lower bound** on the fraction of support vectors.

For classification the dual maximises $-\frac{1}{2}\sum_{n,m}a_n a_m t_n t_m k(\mathbf{x}_n,\mathbf{x}_m)$ subject to $0 \leq a_n \leq 1/N$, $\sum_n a_n t_n = 0$, $\sum_n a_n \geq \nu$. An analogous $\nu$-SVR variant fixes the fraction of points outside the $\varepsilon$-tube.

### Why it matters
The parameter $\nu$ has a direct and intuitive interpretation in terms of the data distribution, making model selection more transparent than choosing $C$. It is also used in one-class SVMs for novelty/outlier detection.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]