---
aliases: []
also_type: []
analogous-to:
- vc-dimension
applies:
- overfitting-and-underfitting
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
- learning-theory
id: pkis:concept:effective-model-capacity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch11
tags:
- capacity
- overfitting
- underfitting
- hyperparameters
- U-shaped-curve
title: Effective Model Capacity
understanding: 0
uses:
- bias-variance-tradeoff
- regularization
- dropout
- weight-decay-as-prior
---

## Definition
The **effective capacity** of a model is its actual ability to fit diverse functions, constrained jointly by (1) **representational capacity** (architecture expressiveness), (2) **optimisation capacity** (the learning algorithm's ability to minimise the training objective), and (3) **regularisation** (penalties or constraints that restrict the solution space):

$$\text{effective capacity} \propto \text{repr. capacity} \times \text{opt. success} \times (1 - \text{regularisation strength}).$$

Generalisation error traces a U-shaped curve as effective capacity increases: high error from underfitting at low capacity, high error from overfitting at high capacity, with a minimum at the optimal capacity.

### Why it matters
Manual hyperparameter tuning reduces to controlling effective capacity. The learning rate, weight decay, number of layers, hidden units, and dropout rate all modulate different facets of effective capacity. Understanding their joint effect prevents wasted search — e.g., increasing weight decay only reduces capacity, so it cannot cure underfitting.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[weight-decay-as-prior]] — uses
- [[dropout]] — uses: Dropout reduces effective capacity
- [[overfitting-and-underfitting]] — applies
- [[regularization]] — uses
- [[bias-variance-tradeoff]] — uses
- [[vc-dimension]] — analogous-to: VC dimension is a formal measure; effective capacity is the practitioner's operational concept
[To be populated during integration]