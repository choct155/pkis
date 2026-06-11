---
aliases: []
also_type: []
analogous-to:
- variational-free-energy
applies:
- undirected-graphical-models
- turbo-code
- sum-product-decoding-ldpc
- gaussian-graphical-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- variational-inference
- gibbs-sampler
- mean-field-approximation
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
- information-theory
- machine-learning
extends:
- sum-product-algorithm
- belief-propagation
- sum-product-algorithm-trees
id: pkis:technique:loopy-belief-propagation
instantiates:
- sum-product-decoding-ldpc
- iterative-turbo-decoding
- belief-propagation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
- goodfellow-deeplearning-ch16
- murphy-pml2-advanced-ch09
specializes:
- message-passing
- generalised-belief-propagation
tags:
- approximate-inference
- message-passing
- LDPC
- turbo-codes
- Bethe-approximation
title: Loopy Belief Propagation
understanding: 0
uses:
- sum-product-algorithm
- variational-free-energy
- computation-tree-bp
- residual-belief-propagation
---

## Definition
**Loopy belief propagation (LBP)** applies the sum-product message-passing rules (8.66)–(8.69) to factor graphs that contain **cycles**, using an iterative schedule:
1. Initialise all messages to the unit function (1 for variable→factor, $f(x)$ for factor→variable leaf messages).
2. Repeatedly update messages according to (8.66) and (8.69) until convergence or a fixed number of iterations.
3. Compute approximate marginals as products of incoming messages at each variable node.

LBP is not guaranteed to converge, and even when it does the marginals are generally approximate.

### Why it matters
Despite lacking theoretical guarantees, LBP achieves state-of-the-art performance in many applications. In particular, **turbo decoding** and **sum-product decoding of LDPC codes** are instances of LBP that operate near the Shannon limit. LBP can be analysed via the Bethe free energy approximation (a variational view). Its failure modes include oscillation and overconfident marginals due to 'double counting' of evidence around loops.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-graphical-model]] — applies: GBP on Gaussians gives exact means
- [[generalised-belief-propagation]] — specializes: GBP is a more accurate generalisation
- [[residual-belief-propagation]] — uses
- [[computation-tree-bp]] — uses
- [[sum-product-decoding-ldpc]] — applies
- [[turbo-code]] — applies
- [[mean-field-approximation]] — contrasts-with
- [[variational-free-energy]] — uses: LBP minimises the Bethe free energy
- [[belief-propagation]] — instantiates
- [[sum-product-algorithm-trees]] — extends
- [[message-passing]] — specializes
- [[gibbs-sampler]] — contrasts-with
- [[variational-inference]] — contrasts-with
- [[undirected-graphical-models]] — applies
- [[sum-product-algorithm]] — uses
- [[belief-propagation]] — extends
- [[variational-free-energy]] — analogous-to
- [[iterative-turbo-decoding]] — instantiates
- [[sum-product-decoding-ldpc]] — instantiates
- [[sum-product-algorithm]] — extends
[To be populated during integration]