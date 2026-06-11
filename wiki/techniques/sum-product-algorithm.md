---
aliases: []
also_type: []
analogous-to:
- variable-elimination
applies:
- trellis
- dag-factorization
- markov-random-field
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
generalizes:
- belief-propagation
- forward-backward-algorithm
id: pkis:technique:sum-product-algorithm
instantiates:
- message-passing
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
- conditional-independence
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
- [[markov-random-field]] — applies
- [[dag-factorization]] — applies
- [[conditional-independence]] — uses
- [[variable-elimination]] — analogous-to
- [[forward-backward-algorithm]] — generalizes
- [[message-passing]] — instantiates
- [[belief-propagation]] — generalizes
- [[factor-graph]] — uses: Sum-product message rules are defined over the variable/factor nodes of a factor graph.
- [[trellis]] — applies: Sum-product runs on the trellis to solve bitwise (marginal) decoding.
- [[generating-functions]] — uses: Counting paths via weighted sums connects to generating-function bookkeeping of combinatorial counts.
- [[message-passing]] — specializes: Sum-product is the marginalizing instance of the general message-passing paradigm.
[To be populated during integration]

## Bitwise Decoding on a Trellis (Forward-Backward)
Replacing the min and sum of the Viterbi algorithm by sum and product, and the edge costs by the likelihoods $P(y_n\mid t_n)$ themselves, turns trellis message passing into the **sum-product algorithm** for *bitwise* decoding. The forward messages $\alpha_i=\sum_{j\in\mathcal{P}(i)} w_{ij}\alpha_j$ and backward messages $\beta_j=\sum_{i:\,j\in\mathcal{P}(i)} w_{ij}\beta_i$ combine to give each bit's posterior marginal $P(t_n=t\mid\mathbf{y})\propto\sum \alpha_j w_{ij}\beta_i$ over edges carrying value $t$. This trellis instance is exactly the **forward-backward / BCJR** algorithm, demonstrating that sum-product on a chain marginalizes in time linear in the number of edges.

## Factor-graph formulation: the two message rules
On a factor graph, the algorithm passes messages of two types along each edge, both functions of the adjacent variable $x_n$: variable-to-factor messages $q_{n\to m}$ and factor-to-variable messages $r_{m\to n}$.

**Variable to factor** (multiply incoming factor messages, excluding the recipient):
$$q_{n\to m}(x_n) = \!\!\prod_{m'\in M(n)\setminus m}\!\! r_{m'\to n}(x_n).$$

**Factor to variable** (sum the factor times incoming variable messages over all of $\mathbf{x}_m$ except $x_n$):
$$r_{m\to n}(x_n) = \sum_{\mathbf{x}_{m\setminus n}}\Big( f_m(\mathbf{x}_m)\!\!\prod_{n'\in N(m)\setminus n}\!\! q_{n'\to m}(x_{n'})\Big).$$

Leaf nodes seed the recursion: a leaf variable broadcasts $q_{n\to m}(x_n)=1$; a leaf factor broadcasts $r_{m\to n}(x_n)=f_m(x_n)$. A message is emitted once all messages it depends on have arrived, so after a number of steps equal to the graph diameter every edge carries a message in each direction. The marginal is then the product of all incoming factor messages at a variable,
$$Z_n(x_n) = \!\prod_{m\in M(n)}\! r_{m\to n}(x_n),$$
with $Z = \sum_{x_n} Z_n(x_n)$ and $P_n(x_n) = Z_n(x_n)/Z$. On-the-fly normalization of the $q$ messages keeps values from over/under-flowing, and passing log-messages turns the products into sums (at the cost of softmax combinations $\ln\sum_i e^{l_i}$).

## Application: Decoding LDPC Codes
The sum-product algorithm's most celebrated application is the decoding of low-density parity-check codes (MacKay ITILA Ch. 47). The code's parity-check matrix $\mathbf{H}$ defines a bipartite Tanner graph of *bit* and *check* nodes, and the algorithm propagates probability ratios along its edges to approximate the bitwise posteriors $P(x_n=1\mid\mathbf{z},\mathbf{H})$. Two refinements are characteristic of this setting: (1) the check ('horizontal') update reduces to a product of message differences, $\delta r_{mn} = (-1)^{z_m}\prod_{n'\in N(m)\setminus n}\delta q_{mn'}$, viewable as a Fourier transform and its inverse; and (2) decoding can **stop-when-it's-done** — halt the moment a tentative $\hat{\mathbf{x}}$ satisfies $\mathbf{H}\hat{\mathbf{x}}=\mathbf{z}$. Although the Tanner graph contains cycles (so sum-product is only approximate), for a good code at an achievable rate the posterior concentrates on one codeword, and loopy belief propagation finds it reliably. This is precisely what allows LDPC codes to approach the Shannon limit in practice.

## Application: decoding repeat-accumulate codes
Decoding **repeat-accumulate codes** is a representative two-phase use of the sum-product algorithm on a factor graph mixing a trellis with local constraint nodes. In the first half of each iteration, the accumulator trellis receives transition likelihoods (including channel evidence) and runs the **forward-backward algorithm** to emit a likelihood for each variable node. In the second half, the equality (repetition) nodes multiply their incoming messages and send fresh likelihood messages back into the trellis. Iterating exchanges soft information between the convolutional (accumulator) and repetition parts of the graph. A *stop-when-it's-done* criterion checks whether the current hard decisions satisfy all parity constraints, separating detected decoding failures from rare undetected errors due to low-weight codewords. Empirically the iteration count $\tau$ to convergence follows a heavy-tailed power law $P(\tau)\propto\tau^{-p}$.

## Erasure-Channel Specialization: the Peeling Decoder
On an **erasure channel** the sum–product algorithm collapses into an especially simple form: every message is either *completely certain* (a variable's value is known with probability one) or *completely uncertain* (uniform over all values), with no intermediate soft beliefs. The algorithm then reduces to the **[[peeling-decoder]]** — repeatedly find a check connected to a single unknown source packet, fix that packet, XOR it into its other checks, and remove its edges. This is the decoder used by [[lt-codes]] and other sparse-graph erasure codes, running in near-linear time.