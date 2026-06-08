---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:principle:occams-razor
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch28
tags:
- model-comparison
- model-selection
- simplicity
- bayesian-inference
- philosophy-of-science
title: Occam's Razor
understanding: 0
---

## Definition
**Occam's razor** is the principle of preferring the simplest hypothesis that adequately accounts for the data: *'accept the simplest explanation that fits the data.'* When several models are compatible with a set of observations, one should not multiply entities beyond necessity.

The principle is often defended on aesthetic grounds (simple theories are 'more beautiful') or on the empirical track record of simplicity. MacKay's central claim is sharper: coherent Bayesian inference embodies Occam's razor *automatically and quantitatively*, with no need for any subjective bias against complex models.

### Why it matters
Naive model selection by best fit is self-defeating: a more complex model can always fit the data at least as well, so maximizing the likelihood drives one inexorably toward over-parameterized models that generalize poorly. Some complexity penalty is therefore not optional but structurally required. Occam's razor names the qualitative principle that supplies it.

### The Bayesian justification
Consider the posterior odds between two models $H_1$ (simple) and $H_2$ (complex):
$$\frac{P(H_1\mid D)}{P(H_2\mid D)} = \frac{P(H_1)}{P(H_2)}\,\frac{P(D\mid H_1)}{P(D\mid H_2)}.$$
Even with equal priors $P(H_1)=P(H_2)$, the data-dependent evidence ratio favours the simpler model. A complex model can predict a greater *variety* of data sets, so it must spread its predictive probability $P(D\mid H_2)$ more thinly over data space. When the data are compatible with both, the simpler model concentrated more probability on them and wins. MacKay's sequence example ($-1,3,7,11$: 'add 4' versus a fitted cubic) yields odds of roughly forty million to one for the arithmetic rule.

### Coincidences and complexity
The everyday intuition that *coincidences are suspicious* is the same effect: a complex model that must invoke a finely-tuned coincidence (two boxes of identical height and colour behind a tree) pays a large penalty for the prior probability it wasted on all the alternatives that did not occur.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]