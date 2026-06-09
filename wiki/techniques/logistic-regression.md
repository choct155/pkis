---
aliases: []
also_type: []
contrasts-with:
- linear-discriminant-analysis
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- statistical-learning
id: pkis:technique:logistic-regression
instantiates:
- generative-vs-discriminative-models
knowledge_type: technique
maturity: settled
related_concepts:
- '[[regularization]]'
sources:
- '[[hastie-esl]]'
- '[[kroese-statistical-modeling]]'
specializes:
- generalized-linear-models
tags:
- probability-theory
- optimization
title: Logistic Regression
understanding: 0
uses:
- weight-decay-as-prior
- iteratively-reweighted-least-squares
---

Linear classification model that estimates class posterior probabilities via a logistic (sigmoid) link function, fitted by maximum likelihood through iteratively reweighted least squares.

## Reading Path
- [[hastie-esl]] (unread) — primary treatment in linear classification methods
- [[kroese-statistical-modeling-ch10]] (unread) — logistic regression as the logit GLM; contrasted with probit model and Poisson regression within unified GLM framework

## Equivalence to the Logistic Single Neuron
MacKay (ITILA Ch. 39) derives logistic regression from the bottom up as a **single logistic neuron**: the model $y(\mathbf{x};\mathbf{w})=1/(1+e^{-\mathbf{w}\cdot\mathbf{x}})$ is literally a feedforward unit computing activation $a=\mathbf{w}\cdot\mathbf{x}$ followed by a sigmoid, and the trained output is read as $P(\text{class }1\mid\mathbf{x})$. The standard logistic-regression objective is exactly the neuron's cross-entropy error
$$G(\mathbf{w}) = -\sum_n\big[t^{(n)}\ln y^{(n)}+(1-t^{(n)})\ln(1-y^{(n)})\big],$$
whose per-example term is the *information content* of the outcome — equivalently the relative entropy between the empirical label distribution $(t,1-t)$ and the model's $(y,1-y)$, bounded below by zero and attained iff $y^{(n)}=t^{(n)}$ for all $n$. Maximizing the Bernoulli likelihood and minimizing this cross-entropy coincide. The gradient $\partial G/\partial w_j=-\sum_n(t^{(n)}-y^{(n)})x_j^{(n)}$ yields the delta update $\Delta w_i=\eta(t-y)x_i$. The same logistic posterior arises canonically from two Gaussian class-conditionals with shared covariance (MacKay §11.2), explaining *why* this functional form is the natural classifier.

## Connections
- [[iteratively-reweighted-least-squares]] — uses: fit by maximum likelihood through IRLS
- [[linear-discriminant-analysis]] — contrasts-with: same logit-linear form but discriminative (conditional likelihood, arbitrary Pr(X)) vs generative (full joint with Gaussian densities); robustness vs efficiency tradeoff
- [[generative-vs-discriminative-models]] — instantiates
- [[weight-decay-as-prior]] — uses
- [[generalized-linear-models]] — specializes