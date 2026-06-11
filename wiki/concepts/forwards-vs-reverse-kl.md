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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- information-theory
id: pkis:concept:forwards-vs-reverse-kl
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
tags:
- kl-divergence
- variational-inference
- mode-seeking
- mode-covering
- moment-matching
- approximate-inference
title: Forwards vs Reverse KL (M-projection vs I-projection)
understanding: 0
---

## Definition
Given a target distribution $p$ and an approximating family $q$, two distinct optimization problems arise:

$$\text{M-projection (forwards KL): } q^* = \arg\min_q D_{\mathrm{KL}}(p \| q)$$
$$\text{I-projection (reverse KL): } q^* = \arg\min_q D_{\mathrm{KL}}(q \| p)$$

**Forwards KL** (moment projection) forces $q > 0$ wherever $p > 0$, producing **mode-covering** (zero-avoiding) behavior — $q$ spreads mass to cover all modes of $p$, often resulting in over-dispersed approximations. When $q$ is an exponential family, the optimal $q$ matches the sufficient-statistic moments of $p$ (moment matching).

**Reverse KL** (information projection) forces $q = 0$ wherever $p = 0$, producing **mode-seeking** (zero-forcing) behavior — $q$ collapses onto one mode of $p$, often resulting in over-confident approximations.

### Why it matters
The choice between forwards and reverse KL fundamentally shapes the behavior of approximate inference algorithms: variational inference typically minimizes reverse KL, while MLE minimizes forwards KL to the empirical distribution. Understanding this asymmetry is essential for diagnosing under- vs over-confidence in learned models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]