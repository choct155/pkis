---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:maximum-likelihood-estimation
knowledge_type: technique
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[em-algorithm]]'
- '[[hypothesis-testing]]'
- '[[logistic-regression]]'
sources:
- '[[kroese-statistical-modeling]]'
tags:
- likelihood
- estimation
- fisher-information
- cramer-rao
- mle
- asymptotic-theory
title: Maximum Likelihood Estimation
understanding: 0
---

Maximum Likelihood Estimation (MLE) finds the parameter value θ̂ that maximizes the likelihood function L(θ; Y) = p(Y|θ) — i.e., the parameter under which the observed data were most probable.

## Reading Path
- [[kroese-statistical-modeling-ch06]] (unread) — primary treatment: score functions, Fisher information, Cramér-Rao bound, asymptotic normality of MLE, likelihood ratio tests, and Newton-Raphson

## Bayesian critique (MacKay)
MacKay (ITILA Ch. 3) frames the Bayesian critique of point estimation: the full posterior $P(\theta\mid D)\propto P(D\mid\theta)P(\theta)$ is 'the unique and complete solution', so 'there is no need to invent estimators, nor criteria for comparing alternative estimators.' MLE corresponds to the mode of the posterior under a flat prior, but it discards the spread the posterior encodes. For prediction, the MLE plug-in differs from the posterior-predictive average (Laplace's rule, $\frac{F_a+1}{F_a+F_b+2}$ vs. $F_a/F$).