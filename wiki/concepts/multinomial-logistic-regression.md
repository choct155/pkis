---
aliases: []
also_type: []
analogous-to:
- linear-regression
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- multi-label-classification
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- machine-learning
- statistics
generalizes:
- logistic-regression
- binary-logistic-regression
id: pkis:concept:multinomial-logistic-regression
instantiates:
- logistic-regression-nll-convexity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- neural-networks
related_concepts: []
sources:
- murphy-pml1-intro-ch02
- murphy-pml1-intro-ch10
- murphy-pml1-intro
tags:
- classification
- softmax
- logistic-regression
- multiclass
- linear-model
title: Multinomial Logistic Regression (Softmax Regression)
understanding: 0
uses:
- softmax-function
- cross-entropy-loss
- softmax-jacobian
- logit-pre-activation
- maximum-likelihood-estimation
- hierarchical-softmax
- class-imbalance-long-tail
- categorical-distribution
---

## Definition
$$p(y=c|x;\theta) = \frac{\exp(w_c^\top x + b_c)}{\sum_{c'=1}^{C}\exp(w_{c'}^\top x + b_{c'})}, \quad c\in\{1,\ldots,C\}$$

**Multinomial logistic regression** (softmax regression) models the posterior probability of class $c$ using a linear predictor passed through the softmax function: $p(y|x;\theta)=\text{Cat}(y|\text{softmax}(Wx+b))$. The weight matrix $W\in\mathbb{R}^{C\times D}$ and bias $b\in\mathbb{R}^C$ are learned by maximizing the conditional log-likelihood (equivalently minimizing cross-entropy). Decision boundaries between any two classes are linear hyperplanes.

### Why it matters
Multinomial logistic regression is the canonical discriminative baseline for multiclass classification and the output layer of most neural network classifiers. It reduces to binary logistic regression for $C=2$ (up to an identifiable over-parameterization), and provides calibrated probability estimates when trained with cross-entropy loss.

### Connections
- [[categorical-distribution]] — uses
- [[class-imbalance-long-tail]] — uses
- [[hierarchical-softmax]] — uses
- [[multi-label-classification]] — contrasts-with
- [[logistic-regression-nll-convexity]] — instantiates
- [[maximum-likelihood-estimation]] — uses
- [[logit-pre-activation]] — uses
- [[softmax-jacobian]] — uses
- [[binary-logistic-regression]] — generalizes
- [[neural-networks]] — prerequisite-of
- [[linear-regression]] — analogous-to
- [[cross-entropy-loss]] — uses
- [[softmax-function]] — uses
- [[logistic-regression]] — generalizes
The model is over-parameterized for $C>2$ (one weight vector is redundant), motivating parameter tying or regularization. Nonlinear decision boundaries are obtained by feature transformation or by adding hidden layers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]