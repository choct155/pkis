---
aliases: []
also_type: []
applies:
- hopfield-network
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
id: pkis:result:hopfield-network-capacity
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch42
tags:
- hopfield-network
- memory-capacity
- spin-glass
- phase-transition
- signal-to-noise
- amit-gutfreund-sompolinsky
title: Capacity of the Hopfield Network (0.138N)
understanding: 0
uses:
- ising-model
---

## Definition
The **capacity** of a Hebb-rule Hopfield network is the number of random binary patterns it can store as usable attractors. Setting the network to a desired pattern $\mathbf{x}^{(n)}$, a neuron's activation splits into a **signal** term and a **noise** term:
$$a_i = (I-1)\,x_i^{(n)} + \sum_{j\neq i}\sum_{m\neq n} x_i^{(m)}x_j^{(m)}x_j^{(n)}.$$
The noise is a sum of zero-mean, unit-variance random terms, so $a_i$ is approximately Gaussian with mean $I x_i^{(n)}$ and variance $IN$. The per-bit flip probability is
$$P(i\text{ unstable}) = \Phi\!\left(-\sqrt{I/N}\right),$$
governed entirely by the load $N/I$.

### Two capacity definitions
**Stringent** (no bit may flip at all): $N_{\max} \approx I/(4\ln I + 2\ln(1/\epsilon))$, which grows *slower* than linearly. **Statistical-physics** (small corruption allowed): Amit, Gutfreund & Sompolinsky (1985) found a sharp first-order transition at
$$N_{\mathrm{crit}} = 0.138\,I.$$
Below it, a stable state sits near each memory (about 1.6% of bits flipped); above it, only uncorrelated **spin-glass** states survive. In bits this is $0.122\,I^2 \approx 0.24$ bits per weight.

### Why it matters
The $0.138I$ result quantifies a phase transition between *working memory* and *catastrophic spin-glass failure*, links neural memory to spin-glass physics, and shows the Hebb rule is far from optimal — a learned (perceptron-style) rule can store more.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ising-model]] — uses: The 0.138I transition is located with spin-glass statistical-physics methods; failure states are spin-glass states.
- [[hopfield-network]] — applies: Quantifies how many random patterns a Hebb-rule Hopfield network can store (~0.138 N) before catastrophic failure.
[To be populated during integration]