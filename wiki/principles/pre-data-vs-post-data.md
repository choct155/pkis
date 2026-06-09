---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:principle:pre-data-vs-post-data
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch16
tags:
- jaynes
- sampling-distribution
- posterior
- inference-philosophy
- estimator
title: Pre-Data vs Post-Data Questions
understanding: 0
---

## Definition
Jaynes's framing of the basic pragmatic difference between orthodox and Bayesian inference: orthodox practice answers only pre-data questions, whereas real scientific inference asks post-data questions. Pre-data questions concern the distribution of as-yet-unseen data and the long-run behavior of an algorithm: e.g. (A) what data do you expect to get? (B) how accurate do you expect estimates from a given algorithm to be, over the class of data sets you might get? (C) if the hypothesis is true, what is the probability of getting data indicating it is true? Post-data questions condition on the one data set actually obtained: (A') given the data, are we surprised? (B') what estimates and what accuracy are we now entitled to claim? (C') what is the probability, conditional on the data, that the hypothesis is true?

The sharpest instance contrasts (Q1) 'how much would the estimate of a parameter alpha vary over all data sets we might conceivably get?' — the width of the sampling distribution of an estimator — with (Q2) 'how accurately is alpha determined by the one data set we actually have?' — the width of the posterior pdf. Orthodoxy is barred from post-data questions because it admits no posterior distribution for a fixed parameter; it answers a pre-data question and passes the result off as if it answered the post-data one. This succeeds only by 'mathematical accidents,' chiefly symmetry between parameter and estimator. For Gaussian sampling with a sufficient statistic and no nuisance parameters and an uninformative prior, the symmetry is exact, so the (mean ± sigma/sqrt(n)) estimate of mu and the sampling estimate coincide numerically though they mean different things; for a Cauchy sampling distribution the symmetry fails (the sample mean's sampling distribution equals that of a single observation), the two questions give wildly different answers, and orthodoxy has never found a satisfactory estimator at all.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]