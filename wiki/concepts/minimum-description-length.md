---
aliases: []
also_type: []
analogous-to:
- bayesian-information-criterion
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
- information-theory
- statistics
- machine-learning
id: pkis:concept:minimum-description-length
instantiates:
- information-criteria
- bayesian-occams-razor
- compression-as-probabilistic-modelling
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- model-selection
- compression
- Occam-razor
- two-part-code
- MDL
- information-theory
title: Minimum Description Length (MDL) Principle
understanding: 0
uses:
- source-coding-theorem
- essential-bit-content
---

## Definition
$$L_{\text{MDL}}(m) = -\log p(D|\hat{\theta},m) + \frac{D_m}{2}\log N$$

A model is preferred if it minimises the total description length of the data: the **two-part code** consists of (1) the cost of communicating the parameters ($\frac{D_m}{2}\log N$ bits, since each of the $D_m$ parameters can be estimated to precision $O(1/\sqrt{N})$) plus (2) the cost of encoding the data given the model ($-\log p(D|\hat{\theta},m)$ bits via the Shannon–Fano code).

### Why it matters
MDL provides an information-theoretic foundation for model selection that is independent of priors. It formalises Occam's razor: the best model is the one that compresses the data most. MDL is formally equivalent to BIC up to a factor of 2, revealing a deep connection between Bayesian model comparison and lossless data compression. The closely related **minimum message length (MML)** criterion handles the prior encoding cost more carefully.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[compression-as-probabilistic-modelling]] — instantiates
- [[essential-bit-content]] — uses
- [[bayesian-occams-razor]] — instantiates
- [[source-coding-theorem]] — uses
- [[bayesian-information-criterion]] — analogous-to
- [[information-criteria]] — instantiates
[To be populated during integration]