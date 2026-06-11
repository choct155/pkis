---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- bayes-factor
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:technique:bayesian-t-test
instantiates:
- bayesian-inference
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- hypothesis-testing
- classifier-comparison
- paired-test
- t-distribution
- effect-size
title: Bayesian t-test (Paired Classifier Comparison)
understanding: 0
uses:
- region-of-practical-equivalence
- t-distribution
- noninformative-prior
---

## Definition
Given $N$ paired performance differences $d_i = e_i^1 - e_i^2$ between two classifiers, assume $d_i \sim \mathcal{N}(\Delta, \sigma^2)$. Under a non-informative (Jeffreys) prior on $(\Delta,\sigma)$, the posterior marginal for the mean effect size is a Student-$t$ distribution:

$$p(\Delta|d) = T_{N-1}\!\left(\Delta\,\Big|\,\bar{d},\; s^2/N\right)$$

where $\bar{d}=\frac{1}{N}\sum d_i$ and $s^2=\frac{1}{N-1}\sum(d_i-\bar{d})^2$. Hypothesis probabilities such as $p(|\Delta|>\epsilon|d)$ are then computed directly from this posterior.

### Why it matters
Paired testing removes shared difficulty across examples, substantially increasing statistical power compared to unpaired tests. The Bayesian formulation yields a full posterior over effect size rather than a binary reject/accept decision, naturally integrating with the ROPE framework. It is the standard Bayesian analogue of the frequentist paired $t$-test for classifier evaluation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayes-factor]] — contrasts-with
- [[noninformative-prior]] — uses
- [[bayesian-inference]] — instantiates
- [[t-distribution]] — uses
- [[region-of-practical-equivalence]] — uses
[To be populated during integration]