---
aliases: []
also_type: []
analogous-to:
- bias-variance-tradeoff
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
- statistical-learning-theory
id: pkis:concept:generalization-gap
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch01
specializes:
- overfitting-and-underfitting
tags:
- overfitting
- generalization
- test-error
- model-selection
title: Generalization Gap
understanding: 0
uses:
- empirical-risk-minimization
- population-risk
- vc-dimension
---

## Definition
The difference between a model's population risk (expected loss under the true data distribution $p^*(x,y)$) and its empirical risk on the training set:
$$\text{Generalization Gap}(\theta) = \mathcal{L}(\theta; p^*) - \mathcal{L}(\theta; \mathcal{D}_{\text{train}})$$
where $\mathcal{L}(\theta; p^*) = \mathbb{E}_{p^*(x,y)}[\ell(y, f(x;\theta))]$. A large positive gap indicates overfitting.

### Why it matters
The generalization gap is the operational definition of the overfitting/underfitting tradeoff. It motivates train/validation/test splits, cross-validation, regularization, and PAC-learning bounds. Controlling it is the central challenge of statistical learning theory.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[vc-dimension]] — uses
- [[bias-variance-tradeoff]] — analogous-to
- [[population-risk]] — uses
- [[empirical-risk-minimization]] — uses
- [[overfitting-and-underfitting]] — specializes
[To be populated during integration]