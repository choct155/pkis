---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:hypothesis-testing
instantiates:
- sampling-theory
knowledge_type: technique
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[maximum-likelihood-estimation]]'
- '[[information-criteria]]'
- '[[cross-validation]]'
sources:
- '[[kroese-statistical-modeling]]'
- kroese-statistical-modeling-ch05
tags:
- frequentist
- p-value
- null-hypothesis
- power
- type-1-error
- likelihood-ratio-test
title: Hypothesis Testing
understanding: 0
---

Hypothesis testing is a frequentist procedure for deciding between a null hypothesis H₀ and an alternative H₁ by computing a test statistic T(Y) from data and comparing it to a reference distribution under H₀, rejecting H₀ when T falls in the rejection region at significance level α.

## Connections
- [[sampling-theory]] — instantiates: Significance testing is the central inferential procedure of the sampling-theory framework.
- [[maximum-likelihood-estimation]] — uses: likelihood ratio tests compare the MLE under H₀ vs. H₁ using the Wilks asymptotic chi-squared distribution
- [[information-criteria]] — contrasts-with: AIC/BIC are asymptotically related to likelihood ratio tests but optimized for prediction rather than hypothesis control
- [[cross-validation]] — contrasts-with: CV estimates generalization error directly; hypothesis testing controls Type I error rate

## Reading Path
- [[kroese-statistical-modeling-ch05]] (unread) — primary treatment: null/alternative hypotheses, p-values, power, ANOVA for normal linear models
- [[kroese-statistical-modeling-ch06]] (unread) — likelihood ratio tests and score tests as special hypothesis testing procedures

## What a p-value does not mean
A persistent error, flagged by MacKay (Ch. 37) and conceded by sampling theorists themselves, is interpreting a $p$-value as a posterior probability of the null. A report '$p=0.07$' means: *if the experiment were repeated many times and $H_0$ were true, 7% of the time the statistic would be as extreme as observed.* It does **not** mean there is a 93% chance the treatments differ, nor that $P(H_0\mid D)=0.07$. The test also reports only *statistical* significance, never the effect size or practical magnitude.

MacKay's vaccination example sharpens the critique: comparing treatment $A$ (1/30 infected) with control $B$ (3/10), the $\chi^2$ test gives $p\approx0.07$ (and flips to 'accept $H_0$' under Yates's correction), whereas a Bayesian computation of $P(p_{A+}<p_{B+}\mid D)\approx0.99$ gives a direct, decision-relevant answer. Sampling theory can be 'trigger-happy' (rejecting $H_0$ on data that actually favour it) or, conversely, miss evidence intuition deems strong — and its verdict can swing with the choice of statistic, continuity correction, or stopping rule.