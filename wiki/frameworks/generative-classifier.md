---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
generalizes:
- naive-bayes-model
- gaussian-discriminant-analysis
id: pkis:framework:generative-classifier
instantiates:
- generative-vs-discriminative-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- classification
- generative-model
- bayes-rule
- class-conditional-density
title: Generative Classifier
understanding: 0
---

## Definition
$$p(y = c \mid x, \theta) = \frac{p(x \mid y=c,\theta)\, p(y=c\mid\theta)}{\sum_{c'} p(x \mid y=c',\theta)\, p(y=c'\mid\theta)}$$

A generative classifier models the full joint distribution $p(x, y) = p(y)\,p(x\mid y)$ by specifying a **class-conditional density** $p(x\mid y=c,\theta)$ and a class prior $p(y=c\mid\theta)$; the posterior is obtained via Bayes' rule.

### Why it matters
Because the joint is modelled explicitly, generative classifiers naturally handle missing inputs (by marginalisation), support semi-supervised learning with unlabelled data, allow new classes to be added without retraining the whole model, and may better capture the causal data-generating process — making them more robust to distribution shift. The tradeoff is that modelling the (often irrelevant) input density can reduce predictive accuracy versus a discriminative approach when the assumed density is mis-specified.

### Key instantiations
Gaussian Discriminant Analysis (GDA/LDA/QDA) and Naive Bayes are the canonical parametric generative classifiers covered in this chapter.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-vs-discriminative-models]] — instantiates: This node is the specific concept distinguishing joint vs conditional modelling in classification
- [[gaussian-discriminant-analysis]] — generalizes
- [[naive-bayes-model]] — generalizes
[To be populated during integration]