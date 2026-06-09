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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:result:cover-hart-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch13
tags:
- nearest-neighbors
- bayes-error
- asymptotics
- classification
title: Cover-Hart Theorem (1-Nearest-Neighbor Error Bound)
understanding: 0
---

## Definition
A classical asymptotic result (Cover & Hart, 1967) stating that the error rate of the 1-nearest-neighbor classifier is never more than twice the Bayes error rate. The intuition (squared-error version): asymptotically, with fixed feature dimension and densely-filling training data, the query point coincides with a training point so the bias is zero; the Bayes rule's error is the variance of a Bernoulli variate (the target at the query), while the 1-NN error is twice that variance — one contribution each from the training and query targets. For misclassification loss, with dominant class k* and true conditional probabilities p_k(x): Bayes error = 1 - p_{k*}(x), and the asymptotic 1-NN error = sum_k p_k(x)(1 - p_k(x)) >= 1 - p_{k*}(x). For K=2 this is 2 p_{k*}(x)(1 - p_{k*}(x)) <= 2(1 - p_{k*}(x)). The general K-class bound is sum_k p_k(x)(1-p_k(x)) <= 2(1-p_{k*}(x)) - (K/(K-1))(1-p_{k*}(x))^2, so the limiting 1-NN error E_1 is bounded above by E*(2 - E* K/(K-1)) where E* is the Bayes error. Practical use: if 1-NN has 10% error, the Bayes rate is asymptotically at least 5%. The crucial caveat is the asymptotic assumption of zero bias; in real (high-dimensional) problems the 1-NN bias can be substantial, which adaptive nearest-neighbor methods aim to alleviate.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]