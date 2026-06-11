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
- decision-theory
generalizes:
- maximum-a-posteriori-estimation-map
id: pkis:technique:cost-sensitive-classification
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- classification-reject-option
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- classification
- loss
- threshold
- asymmetric-cost
- decision-rule
title: Cost-Sensitive Classification
understanding: 0
uses:
- loss-function-posterior-expected-loss
- receiver-operating-characteristic-curve
- class-confusion-matrix
---

## Definition
In binary classification with asymmetric misclassification costs $\ell_{01}$ (cost of predicting 0 when truth is 1, i.e., false negative) and $\ell_{10}$ (false positive cost), the Bayes-optimal rule is to predict class 1 iff the posterior probability exceeds a threshold derived from the cost ratio:

$$p(y^*=1|x) \geq \frac{\ell_{01}}{\ell_{01}+\ell_{10}}$$

When a false negative costs $c$ times more than a false positive, the threshold simplifies to $1/(1+c)$. This subsumes the zero-one-loss MAP rule as the special case $c=1$ (threshold 0.5).

### Why it matters
Most real classification tasks (medical diagnosis, fraud detection, autonomous driving) have strongly asymmetric costs. Ignoring cost asymmetry and using a 0.5 threshold is equivalent to implicitly assuming equal costs, which is often wrong. Cost-sensitive classification makes the trade-off explicit and derives the threshold from principled Bayesian decision theory rather than ad-hoc calibration.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[class-confusion-matrix]] — uses
- [[classification-reject-option]] — prerequisite-of
- [[maximum-a-posteriori-estimation-map]] — generalizes
- [[receiver-operating-characteristic-curve]] — uses: Threshold selection in cost-sensitive classification maps to points on the ROC curve
- [[loss-function-posterior-expected-loss]] — uses
[To be populated during integration]