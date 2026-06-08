---
aliases: []
also_type: []
analogous-to:
- sum-product-algorithm
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
- bayesian-stats
- information-theory
id: pkis:technique:max-product-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch26
specializes:
- min-sum-algorithm
tags:
- message-passing
- map-inference
- factor-graph
- viterbi
- semiring
title: Max-Product Algorithm
understanding: 0
uses:
- factor-graph
---

## Definition
The max-product algorithm finds the global mode of a factored function,
$$\mathbf{x}^* = \arg\max_{\mathbf{x}} P^*(\mathbf{x}) = \arg\max_{\mathbf{x}} \prod_{m=1}^{M} f_m(\mathbf{x}_m),$$
rather than its marginals. It is obtained from the sum-product algorithm by the *semiring substitution* of $(\max, \times)$ for $(\sum, \times)$ everywhere the message rules appear, exploiting that maximization distributes over multiplication. The factor-to-variable message becomes
$$r_{m\to n}(x_n) = \max_{\mathbf{x}_{m\setminus n}}\Big( f_m(\mathbf{x}_m)\!\!\prod_{n'\in N(m)\setminus n}\!\! q_{n'\to m}(x_{n'})\Big),$$
and the quantity formerly equal to the normalizer $Z$ becomes $\max_{\mathbf{x}} P^*(\mathbf{x})$. Each node's 'marginal' $Z_n(x_n)$ now reports the best attainable value of $P^*$ consistent with that setting of $x_n$, and a traceback recovers the maximizing configuration.

### Min-sum / Viterbi form
In practice the recursion is run in the negative-log-likelihood domain, where $(\max,\times)$ becomes $(\min,+)$. This **min-sum** form is exactly the Viterbi algorithm, avoiding underflow and replacing multiplications with additions.

### Why it matters
Max-product is the MAP/codeword-decoding counterpart of sum-product's bitwise marginalization. The single distributive-law swap shows that marginalization and maximization are the *same* dynamic program over different semirings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[min-sum-algorithm]] — specializes: In the negative-log domain max-product becomes the min-sum / Viterbi algorithm.
- [[factor-graph]] — uses: Max-product passes the same two message types over a factor graph.
- [[sum-product-algorithm]] — analogous-to: Same message recursion with the (max, times) semiring substituted for (sum, times); marginalization vs maximization.
[To be populated during integration]