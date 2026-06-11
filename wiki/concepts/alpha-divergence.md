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
- information-theory
- approximate-inference
id: pkis:concept:alpha-divergence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch10
tags:
- alpha-divergence
- Renyi
- Hellinger
- KL-divergence
- message-passing
title: Alpha-Divergence Family
understanding: 0
---

## Definition
$$D_\alpha(p\|q) = \frac{4}{1-\alpha^2}\left(1 - \int p(x)^{\frac{1+\alpha}{2}}q(x)^{\frac{1-\alpha}{2}}\,dx\right), \quad -\infty < \alpha < \infty$$

A one-parameter family of divergences interpolating between $\text{KL}(p\|q)$ (at $\alpha\to 1$), $\text{KL}(q\|p)$ (at $\alpha\to -1$), and the Hellinger distance (at $\alpha=0$); all members satisfy $D_\alpha\geq 0$ with equality iff $p=q$.

### Why it matters
Unifies a broad spectrum of message-passing and variational algorithms: variational Bayes, expectation propagation, loopy belief propagation, tree-reweighted BP, power EP, and fractional BP all arise as special or limiting cases by choosing different values of $\alpha$. Understanding the continuum clarifies the mode-seeking / mass-covering trade-off.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]