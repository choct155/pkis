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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
extends:
- committee-method
- adaboost
id: pkis:technique:adaboost-algorithm
instantiates:
- forward-stagewise-additive-modeling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch14
specializes:
- ensemble-learning
tags:
- boosting
- weak-learners
- ensemble
- exponential-loss
- classification
title: AdaBoost Algorithm
understanding: 0
uses:
- exponential-loss
---

## Definition
AdaBoost (Freund & Schapire, 1996) trains $M$ weak classifiers $y_m(x)\in\{-1,+1\}$ sequentially and combines them as
$$Y_M(x)=\operatorname{sign}\!\left(\sum_{m=1}^{M}\alpha_m y_m(x)\right)$$
where classifier weights are $\alpha_m = \ln\frac{1-\epsilon_m}{\epsilon_m}$ and per-sample weights are updated by $w_n^{(m+1)} = w_n^{(m)}\exp\{\alpha_m\,\mathbb{1}[y_m(x_n)\neq t_n]\}$.

### Algorithm steps
1. Initialize $w_n^{(1)}=1/N$.
2. For $m=1,\ldots,M$: (a) fit $y_m$ minimizing weighted misclassification $J_m=\sum_n w_n^{(m)}\mathbb{1}[y_m(x_n)\neq t_n]$; (b) compute weighted error rate $\epsilon_m$; (c) set $\alpha_m$ and update weights.
3. Classify by weighted majority vote.

### Why it matters
AdaBoost is equivalent to the sequential (greedy) minimization of the *exponential loss* $\sum_n \exp(-t_n f_m(x_n))$ over additive models (Friedman et al., 2000). This interpretation unifies boosting with forward stagewise additive modeling, motivates extensions to regression and multi-class settings, and explains why the algorithm concentrates effort on hard examples.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[adaboost]] — extends
- [[forward-stagewise-additive-modeling]] — instantiates
- [[exponential-loss]] — uses
- [[ensemble-learning]] — specializes
- [[committee-method]] — extends
[To be populated during integration]