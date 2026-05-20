---
title: "Hypothesis Testing"
knowledge_type: technique
also_type: []
domain: [statistical-learning, bayesian-stats]
tags: [frequentist, p-value, null-hypothesis, power, type-1-error, likelihood-ratio-test]
related_concepts: ["[[probability-theory]]", "[[maximum-likelihood-estimation]]", "[[information-criteria]]", "[[cross-validation]]"]
sources: ["[[kroese-statistical-modeling]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Hypothesis testing is a frequentist procedure for deciding between a null hypothesis H₀ and an alternative H₁ by computing a test statistic T(Y) from data and comparing it to a reference distribution under H₀, rejecting H₀ when T falls in the rejection region at significance level α.

## Connections
- [[maximum-likelihood-estimation]] — uses: likelihood ratio tests compare the MLE under H₀ vs. H₁ using the Wilks asymptotic chi-squared distribution
- [[information-criteria]] — contrasts-with: AIC/BIC are asymptotically related to likelihood ratio tests but optimized for prediction rather than hypothesis control
- [[cross-validation]] — contrasts-with: CV estimates generalization error directly; hypothesis testing controls Type I error rate

## Reading Path
- [[kroese-statistical-modeling-ch05]] (unread) — primary treatment: null/alternative hypotheses, p-values, power, ANOVA for normal linear models
- [[kroese-statistical-modeling-ch06]] (unread) — likelihood ratio tests and score tests as special hypothesis testing procedures
