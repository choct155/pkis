---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:result:optimal-symbol-codelengths
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch05
tags:
- source-coding
- shannon-information-content
- gibbs-inequality
- relative-entropy
- symbol-codes
title: Optimal Symbol Codelengths and the Cost of Wrong Lengths
understanding: 0
---

## Definition
For a uniquely decodable code the expected length is bounded below by the entropy, $L(C,X)\ge H(X)$, with equality iff the code is complete and the codelengths equal the Shannon information contents:
$$l_i = \log_2 \frac{1}{p_i}.$$

### Proof sketch
Define implicit probabilities $q_i\equiv 2^{-l_i}/z$, so $l_i=\log\tfrac1{q_i}-\log z$. Then
$$L(C,X)=\sum_i p_i l_i \ge \sum_i p_i\log\tfrac1{p_i}-\log z \ge H(X),$$
using Gibbs' inequality (equality iff $q_i=p_i$) and Kraft $z\le 1$.

### The cost of the wrong code
If the true distribution is $\{p_i\}$ but a complete code with implicit probabilities $q_i$ is used, the average length exceeds the entropy by exactly the relative entropy:
$$L(C,X) = H(X) + D_{KL}(\mathbf{p}\,\|\,\mathbf{q}).$$

### Why it matters
This gives the operational meaning of two central quantities: the Shannon information content is the ideal codelength, and KL divergence is the literal number of bits per symbol wasted by encoding with a mismatched model. Because ideal lengths are generally non-integer, exact equality is unattainable in a symbol code — motivating arithmetic coding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]