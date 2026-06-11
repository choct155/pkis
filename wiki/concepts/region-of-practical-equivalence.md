---
aliases: []
also_type: []
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
- hypothesis-testing
- bayes-factor
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- decision-theory
- machine-learning
id: pkis:concept:region-of-practical-equivalence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-t-test
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- hypothesis-testing
- effect-size
- Bayesian-testing
- model-comparison
- ROPE
title: Region of Practical Equivalence (ROPE)
understanding: 0
---

## Definition
$$R = [-\epsilon, \epsilon]$$

A user-specified interval around zero such that effect sizes $\Delta$ falling inside $R$ are considered **practically equivalent** (negligible) even if statistically distinguishable from zero. In Bayesian significance testing, three mutually exclusive hypotheses are evaluated:
- $H_0: \Delta \in R$ (practically no difference)
- $H_A: \Delta > \epsilon$ (model 1 meaningfully better)
- $H_B: \Delta < -\epsilon$ (model 2 meaningfully better)

by computing $p(H_0|D)$, $p(H_A|D)$, $p(H_B|D)$ from the posterior $p(\Delta|D)$.

### Why it matters
The classical point null $H_0:\Delta=0$ is typically false by construction (any two models differ by *some* amount), making frequentist NHST an uninformative test. The ROPE replaces it with a practically meaningful region. Paired with a Bayesian posterior over effect sizes, it enables questions like "what is the probability that model 1 is better by at least 1%?" — which is what practitioners actually care about.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayes-factor]] — contrasts-with
- [[hypothesis-testing]] — contrasts-with
- [[bayesian-t-test]] — prerequisite-of
[To be populated during integration]