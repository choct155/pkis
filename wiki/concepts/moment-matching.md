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
- statistics
- approximate-inference
- information-theory
id: pkis:concept:moment-matching
instantiates:
- zero-forcing-vs-zero-avoiding-kl
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- expectation-propagation
related_concepts: []
sources:
- bishop-prml-ch10
tags:
- EP
- sufficient-statistics
- exponential-family
- ADF
- KL-minimization
title: Moment Matching Approximation
understanding: 0
uses:
- exponential-family
---

## Definition
When minimizing $\text{KL}(p\|q)$ over a distribution $q$ in the exponential family with natural parameters $\boldsymbol{\eta}$,
$$\mathbb{E}_{q(z)}[\mathbf{u}(z)] = \mathbb{E}_{p(z)}[\mathbf{u}(z)]$$
i.e., the optimal $q$ has **expected sufficient statistics** equal to those of $p$. For a Gaussian $q$ this reduces to matching mean and covariance.

### Why it matters
Provides the tractable computational step inside expectation propagation: instead of globally minimizing a KL divergence over the whole posterior, EP locally moment-matches each cavity-times-factor product to an exponential-family distribution, making the algorithm both principled and efficient. Also the basis of assumed density filtering (ADF).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[zero-forcing-vs-zero-avoiding-kl]] — instantiates
- [[exponential-family]] — uses
- [[expectation-propagation]] — prerequisite-of
[To be populated during integration]