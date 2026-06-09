---
aliases: []
also_type: []
analogous-to:
- min-sum-algorithm
- belief-propagation
- kalman-filter
applies:
- convolutional-code
- hidden-markov-model
- filtering-prediction-smoothing
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
- statistical-learning
id: pkis:technique:forward-backward-algorithm
instantiates:
- sum-product-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch25
tags:
- forward-backward
- bcjr
- sum-product
- trellis
- bitwise-decoding
- marginalization
- message-passing
title: Forward-Backward (BCJR) Algorithm
understanding: 0
uses:
- trellis
---

## Definition
The **forward-backward algorithm** (also the **BCJR algorithm**) is the sum-product algorithm specialized to a trellis. It solves the *bitwise decoding problem*: computing the posterior marginal $P(t_n=t\mid\mathbf{y})$ for each transmitted bit, in time proportional to the number of trellis edges rather than $O(2^{K})$.

Let $w_{ij}=P(y_n\mid t_n)$ be the likelihood on the edge from node $j$ to node $i$, and $\mathcal{P}(i)$ the parents of $i$. The **forward pass** computes
$$\alpha_0 = 1,\qquad \alpha_i = \sum_{j\in\mathcal{P}(i)} w_{ij}\,\alpha_j,$$
where $\alpha_i$ is proportional to the joint probability that the path passes through node $i$ and the first $n$ symbols were observed. The **backward pass** computes
$$\beta_I = 1,\qquad \beta_j = \sum_{i:\,j\in\mathcal{P}(i)} w_{ij}\,\beta_i.$$

### Combining the messages
For each bit value $t\in\{0,1\}$, summing over edges at time $n$ carrying that value,
$$r_n^{(t)} = \!\!\sum_{i,j:\,j\in\mathcal{P}(i),\,t_{ij}=t}\!\! \alpha_j\,w_{ij}\,\beta_i,\qquad P(t_n=t\mid\mathbf{y}) = \frac{r_n^{(t)}}{Z},$$
with $Z=r_n^{(0)}+r_n^{(1)}=\alpha_I$, the final forward message and the marginal probability of the data.

### Why it matters
This is the exact, efficient route to per-bit soft outputs that drive iterative decoders (e.g. turbo codes) and is mathematically identical to the forward-backward inference used in hidden Markov models and Kalman smoothing, making it a canonical instance of exact marginalization on a chain.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[filtering-prediction-smoothing]] — applies: Forward-backward realizes the filtering and smoothing inference tasks via forward and backward messages.
- [[hidden-markov-model]] — applies: Forward-backward performs filtering and smoothing inference in HMMs via T/O matrix recursions.
- [[convolutional-code]] — applies: The forward-backward (BCJR) algorithm computes per-bit posteriors on the convolutional trellis.
- [[kalman-filter]] — analogous-to: Both are exact forward-backward inference on a chain; Kalman is the linear-Gaussian continuous-state case.
- [[belief-propagation]] — analogous-to: Forward-backward / BCJR is belief propagation specialized to a chain, and is exact there.
- [[min-sum-algorithm]] — analogous-to: Same trellis message passing; sum/product for marginals vs min/sum for the best path.
- [[trellis]] — uses: The alpha/beta recursions are defined over the nodes and edges of the code trellis.
- [[sum-product-algorithm]] — instantiates: Forward-backward is the sum-product algorithm specialized to a trellis (chain) graph.
[To be populated during integration]