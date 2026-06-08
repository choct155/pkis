---
aliases: []
also_type: []
applies:
- sum-product-decoding-ldpc
- low-density-parity-check-code
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:technique:density-evolution
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch47
tags:
- error-correction
- ldpc
- iterative-decoding
- phase-transition
- asymptotic-analysis
title: Density Evolution and the Decoding Threshold
understanding: 0
---

## Definition
**Density evolution** analyzes the asymptotic behaviour of iterative LDPC decoding by tracking the probability distributions of the messages passed in the algorithm as the iteration count grows, on an idealized infinite, loop-free, tree-like graph with the same local degrees $(j,k)$ as the code. The key object is the average entropy (or error probability) of a single bit after $i$ iterations — equivalently the conditional entropy of a central bit given all checks out to radius $i$.

### The threshold
Successful decoding requires that this average bit entropy **collapse to zero** as iterations increase. Below a critical channel noise level it does; above it the entropy converges to a nonzero floor (decoding failure). The boundary noise level is the **decoding threshold** of the code family — a sharp phase transition. Gallager originally estimated it by Monte Carlo: each iteration maintains a representative sample of $\{r,x\}$ pairs, assembling tree fragments by drawing $(j-1)(k-1)$ children from the previous iteration's list and running sum-product top-to-bottom. Richardson and Urbanke (2001) later derived thresholds analytically; e.g. regular $(4,8)$ codes have threshold $f\approx 0.075$ on the BSC.

### Approximate density evolution
The full distributional update is costly, so practitioners make Gaussian approximations to the message distributions and track only their parameters. The resulting visual diagnostics are **EXIT charts** (ten Brink 1999; Chung et al. 2001), which guide the design of capacity-approaching irregular codes.

### Why it matters
Density evolution turns the empirical question 'how noisy a channel can this code tolerate?' into a computable threshold, and it is the principal design tool for optimizing degree distributions of irregular LDPC codes to squeeze within a fraction of a decibel of the Shannon limit.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[low-density-parity-check-code]] — applies: Density evolution computes the noise threshold and guides degree-distribution design of LDPC codes.
- [[sum-product-decoding-ldpc]] — applies: Density evolution tracks the asymptotic message distributions of sum-product decoding to find its threshold.
[To be populated during integration]