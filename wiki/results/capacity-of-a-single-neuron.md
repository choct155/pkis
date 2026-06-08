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
- deep-learning
- statistical-learning
id: pkis:result:capacity-of-a-single-neuron
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch40
tags:
- perceptron
- memory-capacity
- linear-threshold-unit
- phase-transition
- vc-dimension
title: Capacity of a Single Neuron (Two Bits per Weight)
understanding: 0
---

## Definition
A binary linear threshold neuron with $K$ weights (no bias), viewed as a communication channel that stores a labelling of $N$ data points, has **capacity $2K$ bits** — i.e. **two bits per weight**.

The sender adapts weights $\mathbf{w}$ to memorise an arbitrary binary labelling $\{t_n\}_{n=1}^N$ of $N$ points in general position; the receiver reads off $y=f(\mathbf{w}\cdot\mathbf{x})$ at the same $N$ points. The number of distinct dichotomies realisable is $T(N,K)$, and the fraction of all $2^N$ labellings that can be memorised is
$$\frac{T(N,K)}{2^N}=2^{-N}\,2\sum_{k=0}^{K-1}\binom{N-1}{k}.$$
Using the Gaussian approximation to the partial binomial sum, this fraction stays essentially $1$ up to $N=2K$ and then drops catastrophically to $0$ — a sharp **phase transition** at $N=2K$.

### The two regimes
For $N\le K$ every labelling is realisable ($T=2^N$), so $K$ is the **VC dimension**. Between $N=K$ and $N=2K$ almost all labellings remain realisable; beyond $N=2K$ almost none are.

### Why it matters
It quantifies how much a perceptron can *memorise*, not generalise, and recasts learning as channel coding: weights are the message. A bias adds one effective weight ($K\to K+1$). Extrapolated naively, a brain of $10^{11}$ neurons × $10^3$ synapses × 2 bits gives $\sim 2\times10^{14}$ bits.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]