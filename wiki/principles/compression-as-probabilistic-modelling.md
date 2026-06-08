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
- information-theory
id: pkis:principle:compression-as-probabilistic-modelling
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch06
tags:
- data-compression
- prediction
- adaptive-models
- bayesian
- universality
title: Compression as Probabilistic Modelling
understanding: 0
---

## Definition
The principle that good data compression is equivalent to good probabilistic modelling (prediction) of the source: if a model supplies a predictive distribution $P(x_n = a_i \mid x_1,\ldots,x_{n-1})$ for each next symbol, a near-optimal coder (e.g. arithmetic coding) turns it into a code whose length per symbol approaches $\log_2 1/P$, the entropy under that model. Better prediction $\Rightarrow$ shorter codes.

### The guessing-game intuition
MacKay illustrates this with a human repeatedly guessing the next letter of English text; the number of guesses per letter is a redundancy-revealing re-encoding. A model that predicts well yields a highly skewed, easily compressed symbol stream.

### Static vs adaptive models
The model may be **static** (fixed i.i.d. distribution) or **adaptive** (context-dependent, e.g. Laplace's rule $P_L(a)=\frac{F_a+1}{\sum_{a'}(F_{a'}+1)}$). Arithmetic coding handles either because model and coder are cleanly separated.

### Why it matters
It frames compression, prediction, and learning as one problem. Taken to its limit, a truly universal compressor that could discover any source's distribution would be a general-purpose artificial intelligence — which is why universal coding is fundamentally hard.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]