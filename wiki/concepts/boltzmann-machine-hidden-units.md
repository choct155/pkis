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
- deep-learning
- statistical-learning
id: pkis:concept:boltzmann-machine-hidden-units
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch43
tags:
- boltzmann-machine
- hidden-units
- latent-variables
- higher-order-correlations
- feature-detectors
- restricted-boltzmann-machine
title: Hidden Units in Boltzmann Machines
understanding: 0
---

## Definition
A Boltzmann machine whose units are *all visible* can only capture the **second-order statistics** $\langle x_i x_j\rangle$ of an environment. Many real ensembles (e.g. the 'shifter' ensemble, or images of chairs) carry essential structure only in *higher-order* correlations; their second-order statistics are uninformative. One could add explicit higher-order terms ($v_{ijk}x_i x_j x_k+\cdots$), but the number of parameters explodes (fourth-order statistics of a $128\times128$ image need $>10^7$ terms).

**Hidden units** are Hinton and Sejnowski's (1986) solution: extra latent neurons $h$ that are not clamped to data. The model keeps only pairwise interactions over the joint state $y=(x,h)$, yet *marginalizing out* the hidden units induces arbitrary higher-order correlations among the visible variables. Hidden units often become interpretable **feature detectors**.

### Learning with hidden units
With $P(x^{(n)}\mid W)=\sum_h P(x^{(n)},h\mid W)$, the gradient is again a difference of correlations over $y=(x,h)$:
$$\frac{\partial}{\partial w_{ij}}\ln P(\{x^{(n)}\}\mid W) = \sum_n\Big[\langle y_i y_j\rangle_{P(h\mid x^{(n)},W)} - \langle y_i y_j\rangle_{P(x,h\mid W)}\Big].$$
The positive ('clamped') phase fixes the visible units to data and lets the hidden units sample their conditional; the negative ('free') phase samples the whole network. Both require Monte Carlo, so two sampling runs are now needed per gradient step.

### Why it matters
Hidden units are the decisive innovation that lets the labelled shifter ensemble — unlearnable from second-order statistics — be learned. Restricting the architecture so visible and hidden units form a bipartite graph yields the **restricted Boltzmann machine**, the workhorse of deep belief networks. The double-Monte-Carlo cost, however, is why plain Boltzmann machines are rarely used in practice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]