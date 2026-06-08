---
aliases: []
also_type: []
applies:
- trellis
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
- bayesian-stats
id: pkis:technique:sum-product-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch16
specializes:
- message-passing
tags:
- message-passing
- marginalization
- dynamic-programming
- factor-graph
- forward-backward
title: Sum-Product Algorithm
understanding: 0
uses:
- generating-functions
- factor-graph
---

## Definition
The sum-product algorithm computes marginals of a function that factorizes over a tree by passing messages in which each node **sums** the products of incoming messages along each branch. A node $x$ with upstream neighbours $\{u\}$ sends downstream the message
$$\mu_{x\to d} = \sum \prod_{u} \mu_{u\to x},$$
so that the global marginal at any node is obtained from its incoming messages. MacKay's path-counting example is the special case where every weight equals one: the number of paths from $A$ to a point $P$ equals the sum of the path counts to $P$'s upstream neighbours, and the forward pass yields the total ($5$ paths in the worked grid) without enumeration.

### Forward-backward decomposition
Two passes are run. The **forward** pass propagates messages from the source; a **backward** pass propagates from the sink. Multiplying the forward and backward messages at a node gives the number (or weight) of global configurations passing through it: dividing by the total yields the probability a random path traverses that node, and the backward messages also give the correct biased coin probabilities for drawing a uniform sample (go East with probability $3/5$ vs South $2/5$ in MacKay's grid).

### Why it matters
It is the unifying generalization of the forward-backward algorithm and of belief propagation: marginalization, normalization, and exact sampling on trees all fall out of one message rule. It runs in time linear in the graph, replacing brute-force summation over exponentially many configurations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[factor-graph]] — uses: Sum-product message rules are defined over the variable/factor nodes of a factor graph.
- [[trellis]] — applies: Sum-product runs on the trellis to solve bitwise (marginal) decoding.
- [[generating-functions]] — uses: Counting paths via weighted sums connects to generating-function bookkeeping of combinatorial counts.
- [[message-passing]] — specializes: Sum-product is the marginalizing instance of the general message-passing paradigm.
[To be populated during integration]

## Bitwise Decoding on a Trellis (Forward-Backward)
Replacing the min and sum of the Viterbi algorithm by sum and product, and the edge costs by the likelihoods $P(y_n\mid t_n)$ themselves, turns trellis message passing into the **sum-product algorithm** for *bitwise* decoding. The forward messages $\alpha_i=\sum_{j\in\mathcal{P}(i)} w_{ij}\alpha_j$ and backward messages $\beta_j=\sum_{i:\,j\in\mathcal{P}(i)} w_{ij}\beta_i$ combine to give each bit's posterior marginal $P(t_n=t\mid\mathbf{y})\propto\sum \alpha_j w_{ij}\beta_i$ over edges carrying value $t$. This trellis instance is exactly the **forward-backward / BCJR** algorithm, demonstrating that sum-product on a chain marginalizes in time linear in the number of edges.