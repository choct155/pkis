---
aliases: []
also_type: []
applies:
- clustering
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
- information-theory
- machine-learning
extends:
- mutual-information
id: pkis:concept:normalized-mutual-information
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
tags:
- mutual-information
- normalisation
- feature-selection
- clustering
title: Normalized Mutual Information
understanding: 0
uses:
- entropy
---

## Definition
$$\text{NMI}(X,Y) = \frac{\mathbb{I}(X;Y)}{\min(\mathbb{H}(X),\mathbb{H}(Y))} \in [0,1]$$

A normalised dependence measure that equals 0 when $X\perp Y$ and 1 when the lower-entropy variable is a deterministic function of the other.

### Why it matters
Raw mutual information is hard to compare across variable pairs with different marginal entropies. NMI rescales MI to a unit interval, enabling direct comparison. It is widely used in clustering evaluation (comparing a predicted cluster assignment to ground-truth labels) and feature selection. The denominator choice (min, max, mean, or geometric mean of entropies) varies by application; the min-based version gives the tightest bound ensuring NMI$\le1$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[entropy]] — uses
- [[clustering]] — applies
- [[mutual-information]] — extends
[To be populated during integration]