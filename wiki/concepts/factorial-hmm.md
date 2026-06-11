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
id: pkis:concept:factorial-hmm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
tags:
- HMM
- distributed-representation
- energy-disaggregation
- approximate-inference
title: Factorial HMM
understanding: 0
---

## Definition
An HMM with a **distributed hidden state** represented as $M$ independent Markov chains $z_{t,1}, \ldots, z_{t,M}$, each with its own transition matrix $A_m$, combined through a shared observation model:

$$p(\mathbf{z}, \mathbf{y}) = \prod_t \left[\prod_m p(z_{tm} \mid z_{t-1,m})\right] p(y_t \mid z_t)$$

A typical observation model is $p(y_t \mid z_t) = \mathcal{N}\!\left(y_t \mid \sum_m W_m \bar{z}_{tm}, \Sigma\right)$ where $\bar{z}_{tm}$ is a 1-of-$K$ encoding. Representing $B$ bits requires $M = B$ binary chains vs $K = 2^B$ states in a standard HMM.

### Why it matters
Factorial HMMs achieve exponential representational efficiency by factoring the latent state. They are used in energy disaggregation (separating total household power into per-device contributions) and in other source-separation problems. The main challenge is that exact inference is intractable due to explaining away among the chains.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]