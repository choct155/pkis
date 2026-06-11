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
id: pkis:concept:label-shift
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- distribution-shift
- prevalence-shift
- label-prior
- unsupervised-adaptation
title: Label Shift (Prior Shift)
understanding: 0
---

## Definition
$$q(x, y) = p(x|y)\,q(y), \quad q(y) \neq p(y)$$

Label shift (also called **prior shift** or **prevalence shift**) occurs in a generative/anticausal model when the marginal label distribution $p(y)$ changes between source and target while the class-conditional $p(x|y)$ remains the same.

### Why it matters
Because $p(x|y)$ is invariant, the confusion matrix $C_{ij} = p(\hat{y}=i|y=j)$ computed on the source distribution is also valid on the target. This allows the target label distribution to be estimated from unlabeled target predictions via the linear system $\boldsymbol{\mu} = C\,\mathbf{q}$, enabling a principled correction of a discriminative classifier.

### Correction procedure
Once $q(y)$ is estimated (e.g., via blackbox shift estimation), the posterior is adjusted as $q(y|x) \propto p(y|x)\,q(y)/p(y)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]