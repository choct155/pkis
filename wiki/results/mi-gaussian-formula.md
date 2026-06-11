---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- information-theory
- statistics
id: pkis:result:mi-gaussian-formula
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
tags:
- mutual-information
- Gaussian
- correlation
- closed-form
title: Mutual Information for Jointly Gaussian Variables
understanding: 0
---

## Definition
For jointly Gaussian $(X,Y)$ with correlation $\rho$:
$$\mathbb{I}(X;Y) = -\frac{1}{2}\log(1-\rho^2)$$

As $|\rho|\to 1$ the MI diverges to $+\infty$ (perfect linear dependence); at $\rho=0$ the MI is 0 (independence).

### Why it matters
This closed-form result shows that mutual information strictly generalises Pearson correlation: it captures the full dependence between two jointly Gaussian variables while reducing to a simple function of $\rho$. It motivates MI as a 'generalised correlation coefficient' for non-Gaussian data. The formula also makes explicit why MI can be infinite for perfectly dependent continuous variables, in contrast to discrete MI.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]