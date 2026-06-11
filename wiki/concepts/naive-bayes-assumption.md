---
aliases: []
also_type: []
analogous-to:
- lda-logistic-regression-equivalence
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
id: pkis:concept:naive-bayes-assumption
instantiates:
- naive-bayes-model
- generative-classifier
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- conditional-independence
- generative-classifier
- naive-bayes
- classification
title: Naive Bayes Assumption
understanding: 0
uses:
- conditional-independence
---

## Definition
$$p(x \mid y=c,\theta) = \prod_{d=1}^D p(x_d \mid y=c, \theta_{dc})$$

The naive Bayes assumption posits that the $D$ features $x_1,\ldots,x_D$ are **conditionally independent** given the class label $y=c$. Combined with a class prior $\pi_c$, this defines the naive Bayes classifier (NBC) with $O(CD)$ parameters.

### Why it matters
Although the independence assumption is almost always violated in practice, the NBC is surprisingly competitive because (i) low parameter count reduces overfitting, and (ii) even if individual probability estimates are poor, the rank-ordering of posteriors (needed for classification) may still be correct. The assumption also leads to a closed-form factorised posterior that is trivially updated when new classes or features are added.

### Connection to logistic regression
When features are in the exponential family, the NBC posterior takes the softmax form of multinomial logistic regression; the difference is that NBC maximises the joint likelihood while logistic regression maximises the conditional likelihood.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[lda-logistic-regression-equivalence]] — analogous-to: NBC also reduces to logistic regression form for exponential family features
- [[generative-classifier]] — instantiates
- [[conditional-independence]] — uses
- [[naive-bayes-model]] — instantiates
[To be populated during integration]