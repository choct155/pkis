---
aliases: []
also_type: []
applies:
- polynomial-curve-fitting
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
- statistics
- machine-learning
- decision-theory
generalizes:
- minkowski-loss
id: pkis:result:optimal-regression-conditional-mean
instantiates:
- decision-theory-foundations
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- squared-loss
- conditional-mean
- regression
- bias-variance
- decision-theory
title: Optimal Regression Function is the Conditional Mean
understanding: 0
uses:
- bias-variance-tradeoff
- expectation-and-variance
---

## Definition
Under squared loss $L(t,y(\mathbf{x}))=\{y(\mathbf{x})-t\}^2$, the function $y^*(\mathbf{x})$ minimising expected loss satisfies
$$y^*(\mathbf{x}) = \mathbb{E}_t[t|\mathbf{x}] = \int t\,p(t|\mathbf{x})\,dt.$$
This follows from calculus of variations applied to $\mathbb{E}[L]=\iint\{y(\mathbf{x})-t\}^2 p(\mathbf{x},t)\,d\mathbf{x}\,dt$.

Decomposing the loss:
$$\mathbb{E}[L] = \int\{y(\mathbf{x})-\mathbb{E}[t|\mathbf{x}]\}^2 p(\mathbf{x})\,d\mathbf{x} + \underbrace{\int\mathrm{var}[t|\mathbf{x}]\,p(\mathbf{x})\,d\mathbf{x}}_{\text{irreducible noise}}.$$

### Why it matters
Establishes the probabilistic target for regression: any estimator's MSE can be decomposed into reducible bias and irreducible noise. Generalises directly to vector targets and underpins the bias-variance tradeoff. For the Minkowski loss $|y-t|^q$: $q=2$ gives the mean, $q=1$ the median, $q\to 0$ the mode.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[polynomial-curve-fitting]] — applies
- [[expectation-and-variance]] — uses
- [[minkowski-loss]] — generalizes
- [[bias-variance-tradeoff]] — uses
- [[decision-theory-foundations]] — instantiates
[To be populated during integration]