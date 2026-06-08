---
aliases: []
also_type: []
applies:
- hypothesis-testing
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
contrasts-with:
- likelihood-principle
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:problem:stopping-rule-problem
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch37
tags:
- stopping-rule
- p-value
- experimental-design
- likelihood-principle
- sampling-theory
title: Stopping-Rule Problem
understanding: 0
---

## Definition
The **stopping-rule problem** is the observation that frequentist significance assessments can change with the experimenter's *intention about when to stop collecting data*, even when the observed data are identical. Because a $p$-value integrates over the sample space of outcomes that could have occurred, the relevant sample space — and hence the $p$-value — depends on the stopping rule.

### MacKay's coin example
Dr. Bloggs tosses a coin and records `aaabaaaabaab`: 3 $b$s in 12 tosses. If $n=12$ was fixed and $r$ is random, the sampling theorist computes
$$P(r \le 3 \mid n=12, H_0) = \sum_{r=0}^{3}\binom{12}{r}2^{-12} \approx 0.07,$$
'not significant'. But if Bloggs instead decided to toss *until the third $b$ appeared* (so $r=3$ is fixed and $n$ is random), the relevant distribution is
$$P(n \mid H_0, r) = \binom{n-1}{r-1}2^{-n}, \qquad P(n \ge 12 \mid r=3, H_0) \approx 0.03,$$
'significant after all'. Same data, opposite verdict.

### Why it matters
MacKay's spy/janitor thought experiments — onlookers updating beliefs as tosses arrive, a coin destroyed after the experiment — show the absurdity: what we learn about the bias $p_a$ cannot depend on Bloggs's private intentions or on post-hoc constraints. This is the cleanest argument for the **likelihood principle**: inference should depend only on $P(D\mid H)$ at the observed data. The Bayesian inference about $p_a$ is identical under either stopping rule; the frequentist $p$-value is not.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hypothesis-testing]] — applies: The problem arises within significance testing: the relevant sampling distribution, and hence the p-value, depends on the experimenter's stopping rule.
- [[likelihood-principle]] — contrasts-with: The stopping-rule dependence of p-values is precisely the violation that the likelihood principle forbids; Bayesian inference is invariant to the stopping rule.
[To be populated during integration]