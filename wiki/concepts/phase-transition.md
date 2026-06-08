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
- statistical-learning
- information-theory
id: pkis:concept:phase-transition
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch31
tags:
- phase-transition
- critical-phenomena
- universality
- collective-behavior
- order-parameter
- ising-model
title: Phase Transition
understanding: 0
uses:
- partition-function
---

## Definition
A **phase transition** is a qualitative change in the macroscopic state of a system as a control parameter (e.g. temperature) crosses a critical value, arising from collective behaviour among many interacting components. In the Ising ferromagnet, below a critical temperature the spins align into long-range order (non-zero magnetization $m = \tfrac1N\sum_n x_n$); above it they are effectively independent and $m \to 0$.

### Signature: a peak in fluctuations, not heat capacity
A peak in the heat capacity alone is *not* evidence of a phase transition — any finite-level system shows a Schottky anomaly (a heat-capacity blip with no peak in the energy variance). The true signature is a peak in the energy *fluctuations* $\operatorname{var}(E)$, equivalently in $\langle m^2 \rangle$, growing as the system approaches criticality. The 2D rectangular ferromagnet shows such a peak; the triangular antiferromagnet, being frustrated, shows none and has no transition to long-range order.

### Why it matters
Strictly, true phase transitions occur only in the infinite-$N$ limit, but finite simulations ($N\!\approx\!100$) already reveal critical fluctuations. The principle of *universality* means all systems sharing dimension and symmetry exhibit identical critical scaling laws, so studying the Ising model characterizes phase transitions across magnetism, fluids, and beyond. The transition temperature can be estimated from where the high- and low-temperature free-energy branches intersect.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partition-function]] — uses: Critical signatures (energy variance, free-energy branch crossing, transition temperature) are derived from Z and its derivatives.
[To be populated during integration]