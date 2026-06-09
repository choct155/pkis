---
aliases: []
also_type:
- framework
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-09'
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

## Foundations: probability as a measure of uncertainty
BDA3 Ch. 1 reviews *why* probability is a reasonable yardstick for uncertainty, distinguishing the mathematical axioms (nonnegativity, additivity over mutually exclusive outcomes, summing to 1) from their justification. Two classical accounts of a numerical probability are the symmetry/exchangeability argument (probability = favorable cases / possibilities, assuming equally likely outcomes) and the frequency argument (probability = long-run relative frequency in identical independent trials). Both are in a sense subjective, requiring judgments about physical setup and the meaning of 'equally likely' and 'identical'. The frequency view has the special difficulty that it cannot assign a probability to a genuinely single event except by embedding it conceptually in a hypothetical long sequence. Three further rationales are offered for using probability as the measure of uncertainty: analogy with physical randomness; an axiomatic/normative decision-theoretic argument (reasonable ordering and transitivity axioms force probabilities); and coherence of bets — defining $p$ as the price at which you would bet \$p$ to win \$1 if event $E$ occurs, the requirement that no opponent can guarantee a gain (a Dutch book) provably forces your assessments to obey the probability axioms. The betting rationale is limited by the need for exact two-way odds on all events and by asymmetric information.