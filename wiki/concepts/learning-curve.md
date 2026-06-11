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
id: pkis:concept:learning-curve
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch04
tags:
- overfitting
- underfitting
- sample-complexity
- Bayes-error
title: Learning Curve
understanding: 0
uses:
- overfitting-and-underfitting
- bias-variance-tradeoff
- empirical-risk-minimization
---

## Definition
A learning curve plots model performance (e.g., MSE, misclassification rate) on training and test sets as a function of training set size $N$, for a fixed model class and hyperparameters.

### Key patterns
- **Training error** initially increases with $N$ (harder to perfectly fit more diverse data) then plateaus.
- **Test error** decreases with $N$ and converges toward the **Bayes error** (irreducible noise floor) from above.
- The gap between training and test error decreases as $N \to \infty$ and is larger for more complex models.
- An **underfitting** model shows high, flat test error even as $N$ grows.

### Why it matters
Learning curves diagnose whether a model suffers from bias (underfitting: test error plateaus above Bayes error) or variance (overfitting: large train–test gap). They guide the decision to collect more data vs increase/decrease model complexity. The Bayes error serves as a lower bound on achievable test error regardless of $N$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[empirical-risk-minimization]] — uses
- [[bias-variance-tradeoff]] — uses
- [[overfitting-and-underfitting]] — uses
[To be populated during integration]