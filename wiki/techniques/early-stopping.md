---
aliases: []
also_type: []
analogous-to:
- weight-decay-as-prior
- cross-validation
- ridge-regression
applies:
- overfitting-and-underfitting
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
- optimisation
id: pkis:technique:early-stopping
instantiates:
- regularization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
- goodfellow-deeplearning-ch07
- murphy-pml1-intro-ch04
- murphy-pml1-intro-ch13
specializes:
- regularization
tags:
- overfitting
- regularisation
- validation
- weight-decay
title: Early Stopping as Regularisation
understanding: 0
uses:
- gradient-descent
- validation-set-method
---

## Definition
A regularisation strategy for iterative training algorithms in which training is halted at the iteration $\tau^*$ that minimises error on a held-out **validation set**, rather than at the global minimum of the training loss.

For a quadratic error surface, early stopping with learning rate $\eta$ and iteration $\tau$ is approximately equivalent to L2 regularisation (weight decay) with coefficient $\lambda \approx 1/(\eta\tau)$: both constrain the effective number of degrees of freedom. The weight vector follows the gradient path from the origin, moving first along high-curvature directions (large Hessian eigenvalues) before exploring flat directions.

### Why it matters
Requires no modification to the loss function or model architecture, and is computationally free (validation error is monitored throughout training). It is widely used in practice as a first-line defence against overfitting, often combined with other regularisers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ridge-regression]] — analogous-to: For linear models, early stopping ≈ L2 regularization
- [[validation-set-method]] — uses
- [[cross-validation]] — analogous-to: Both use held-out data to select model complexity
- [[regularization]] — specializes
- [[gradient-descent]] — uses
- [[weight-decay-as-prior]] — analogous-to
- [[overfitting-and-underfitting]] — applies
- [[regularization]] — instantiates
[To be populated during integration]