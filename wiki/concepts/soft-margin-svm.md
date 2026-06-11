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
extends:
- support-vector-machine
id: pkis:concept:soft-margin-svm
instantiates:
- regularization
- bias-variance-tradeoff
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
- murphy-pml1-intro-ch17
specializes:
- support-vector-machine
tags:
- classification
- slack-variables
- regularization
- margin
- svm
title: Soft-Margin SVM and Slack Variables
understanding: 0
uses:
- hinge-loss-svm
- hinge-loss
- regularization
---

## Definition
The soft-margin SVM relaxes the hard-margin constraint by introducing slack variables $\xi_n \geq 0$ for each training point, replacing the constraint $t_n y(\mathbf{x}_n) \geq 1$ with
$$t_n y(\mathbf{x}_n) \geq 1 - \xi_n, \quad \xi_n \geq 0,$$
and minimising
$$C\sum_{n=1}^{N}\xi_n + \frac{1}{2}\|\mathbf{w}\|^2,$$
where $C > 0$ trades off margin width against training misclassification penalty. Points with $0 < \xi_n \leq 1$ lie inside the margin on the correct side; points with $\xi_n > 1$ are misclassified. The dual variables satisfy the box constraints $0 \leq a_n \leq C$.

Soft-margin SVMs tolerate overlapping class distributions while retaining sparsity and convexity.

### Why it matters
The hard-margin SVM is infeasible when classes are not linearly separable in feature space. Slack variables provide a principled way to allow margin violations, with $C$ playing the role of an inverse regularisation parameter. As $C \to \infty$ the hard-margin limit is recovered.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bias-variance-tradeoff]] — instantiates
- [[regularization]] — uses
- [[hinge-loss]] — uses
- [[support-vector-machine]] — specializes
- [[regularization]] — instantiates: C controls trade-off between margin and training error
- [[hinge-loss-svm]] — uses
- [[support-vector-machine]] — extends
[To be populated during integration]