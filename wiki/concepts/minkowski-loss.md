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
- statistics
- machine-learning
- decision-theory
generalizes:
- optimal-regression-conditional-mean
id: pkis:concept:minkowski-loss
instantiates:
- expected-loss
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- loss-function
- regression
- median
- mode
- robust-regression
title: Minkowski Loss for Regression
understanding: 0
uses:
- decision-theory-foundations
---

## Definition
$$\mathbb{E}[L_q] = \int\int |y(\mathbf{x})-t|^q\,p(\mathbf{x},t)\,d\mathbf{x}\,dt, \quad q>0.$$

The optimal predictor $y^*(\mathbf{x})$ minimising $\mathbb{E}[L_q]$ is:
- $q=2$: conditional **mean** $\mathbb{E}[t|\mathbf{x}]$
- $q=1$: conditional **median**
- $q\to 0$: conditional **mode**

### Why it matters
Generalises squared loss to a family parameterised by $q$, making explicit the median and mode as optimal predictors under alternative robustness criteria. The mode optimum under $q\to 0$ is directly relevant to MAP estimation and multimodal conditional distributions, while $q=1$ (absolute loss) is central to robust regression.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[decision-theory-foundations]] — uses
- [[expected-loss]] — instantiates
- [[optimal-regression-conditional-mean]] — generalizes
[To be populated during integration]