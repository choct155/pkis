---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
- machine-learning
id: pkis:technique:max-sum-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
tags:
- MAP-inference
- Viterbi
- dynamic-programming
- back-tracking
- tree
- factor-graph
title: Max-Sum Algorithm
understanding: 0
---

## Definition
The **max-sum algorithm** finds the MAP configuration $\mathbf{x}^{\max} = \arg\max_{\mathbf{x}} p(\mathbf{x})$ on a tree-structured factor graph by replacing summation with maximisation and products with sums of log-factors:

$$\mu_{f \to x}(x) = \max_{x_1,\ldots,x_M}\left[\ln f(x,x_1,\ldots,x_M) + \sum_{m \in \text{ne}(f)\setminus x} \mu_{x_m \to f}(x_m)\right]$$
$$\mu_{x \to f}(x) = \sum_{l \in \text{ne}(x)\setminus f} \mu_{f_l \to x}(x)$$

The maximum log-probability is $\max_x \sum_{s \in \text{ne}(x)} \mu_{f_s \to x}(x)$ at the root. The maximising configuration is recovered via **back-tracking**: store $\phi(x_n) = \arg\max_{x_{n-1}}[\cdot]$ during the forward pass, then trace back from the root.

The log transformation prevents underflow and converts products to sums; the distributive law $\max(a+b, a+c) = a + \max(b,c)$ enables the same factored computation as sum-product.

### Why it matters
Max-sum is the generalisation of the **Viterbi algorithm** to arbitrary tree factor graphs. It yields the globally joint-maximising assignment, unlike greedily maximising individual marginals (which can fail). Back-tracking is essential when multiple configurations tie for the maximum.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]