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
- information-theory
id: pkis:concept:minimal-sufficient-statistic
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
specializes:
- sufficient-statistics
tags:
- sufficient-statistic
- data-compression
- exponential-family
- information-theory
- minimal
title: Minimal Sufficient Statistic
understanding: 0
uses:
- pitman-koopman-darmois-theorem
- exponential-family
- data-processing-inequality
- mutual-information
---

## Definition
A **sufficient statistic** $s(X)$ for parameter $\theta$ satisfies $\mathbb{I}(\theta; s(X)) = \mathbb{I}(\theta; X)$, meaning the data processing inequality holds with equality in the chain $\theta \to X \to s(X)$.

A **minimal sufficient statistic** is a sufficient statistic that is a function of every other sufficient statistic $s'(X)$:
$$s(X) = f(s'(X)) \quad \text{for some function } f \text{ and all sufficient } s'$$

The information-theoretic ordering is:
$$\theta \to s(X) \to s'(X) \to X$$

where $s'$ augments $s$ with redundant information. For $N$ Bernoulli trials, the minimal sufficient statistic is $(N, N_1)$ — total trials and successes — discarding the ordering of outcomes.

### Why it matters
Minimal sufficient statistics identify the irreducible information content of data for parameter estimation. The Pitman-Koopman-Darmois theorem shows exponential families are the only fixed-support families admitting bounded-dimensional sufficient statistics, making this concept central to the theory of optimal data compression for inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mutual-information]] — uses: Sufficiency defined via I(θ;s(X)) = I(θ;X)
- [[data-processing-inequality]] — uses
- [[exponential-family]] — uses
- [[pitman-koopman-darmois-theorem]] — uses
- [[sufficient-statistics]] — specializes
[To be populated during integration]