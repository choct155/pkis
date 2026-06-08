---
aliases: []
also_type: []
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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
extends:
- coupling-from-the-past
id: pkis:concept:monotone-coupling
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- exact-sampling
related_concepts: []
sources:
- mackay-itila-ch32
tags:
- monotonicity
- partial-order
- coalescence
- ising-model
- sandwiching
- bounding-chains
title: Monotone Coupling for Exact Sampling
understanding: 0
uses:
- gibbs-sampler
---

## Definition
**Monotone coupling** is the structural property that makes coupling from the past practical on enormous state spaces. The states are equipped with a (partial) order, and the coupled update rule is *monotone*: it preserves that order, so two trajectories never cross. Then coalescence of *all* trajectories can be certified by tracking only the chains started in the **maximal** and **minimal** states; when these upper and lower bounds meet, every intermediate trajectory is sandwiched between them and must also have coalesced.

$$x \succeq y \;\Rightarrow\; \Phi_u(x) \succeq \Phi_u(y) \quad \text{(monotone update under shared randomness } u\text{)}.$$

### Example: the Ising model
For a ferromagnet, define $x \succeq y$ iff $x_i \ge y_i$ for every spin $i$; the maximal and minimal states are all-up and all-down. Coupled Gibbs sampling (all chains update the same spin with a shared $u$) is monotone, so simulating just these two extreme histories suffices to obtain an exact sample.

### Why it matters
It reduces an intractable simulation over $2^N$ states to just two bounding trajectories, turning CFTP from a theoretical curiosity into a usable algorithm.

### Beyond attractive systems
Monotone coupling needs an 'attractive' (e.g. positive-coupling) system. For general spin systems with negative couplings, the *summary-state* / *sandwiching* / *bounding-chain* generalization tracks an envelope of states in the augmented space $\{-1,+1,?\}^N$ instead of two true trajectories.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exact-sampling]] — prerequisite-of: Monotone coupling is what makes exact sampling practical for large attractive spin systems.
- [[gibbs-sampler]] — uses: Coupled monotone Gibbs sampling on the ferromagnetic Ising model is the canonical example.
- [[coupling-from-the-past]] — extends: Monotonicity lets CFTP track only extreme states, making it tractable on huge state spaces.
[To be populated during integration]