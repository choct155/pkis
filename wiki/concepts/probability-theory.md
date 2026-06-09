---
aliases: []
also_type:
- framework
coverage: 3
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:probability-theory
knowledge_type: concept
maturity: settled
prerequisite-of:
- gaussian-mixture-models
- bayesian-linear-regression
related_concepts:
- '[[gaussian-distribution]]'
- '[[conjugate-prior]]'
- '[[linear-algebra]]'
sources:
- '[[deisenroth-mml]]'
- '[[kroese-statistical-modeling]]'
- '[[lange-applied-probability]]'
tags:
- mathematical-foundations
- measure-theory
title: Probability Theory
understanding: 0
---

The formal study of uncertainty and random phenomena, built on measure-theoretic foundations (probability spaces, sigma-algebras, measures), providing the language for statistical inference, generative models, and Bayesian reasoning throughout ML.

## Reading Path
- [[deisenroth-mml]] (unread) — mathematical treatment: probability spaces, random variables, Bayesian inference, Gaussian distributions
- [[kroese-statistical-modeling-ch01]] (unread) — accessible build-up from random experiments through conditional probability, Bayes' rule, and independence; most pedagogically complete Part I treatment in the wiki
- [[lange-applied-probability-ch01]] (unread) — axiomatic review with multivariate normal treatment

## Connections
- [[bayesian-linear-regression]] — prerequisite-of: MML Ch.1: the probabilistic view of model choice (Ch.6) is the foundation for the regression pillar's Bayesian treatment (Ch.9), where parameters are integrated out rather than optimized.
- [[gaussian-mixture-models]] — prerequisite-of: MML Ch.1: probability theory (Ch.6) is the language for quantifying noise/uncertainty and underlies the density-estimation pillar realized as GMMs (Ch.11).