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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- deep-learning
- statistical-learning
id: pkis:technique:boltzmann-machine-learning-rule
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch43
tags:
- boltzmann-machine
- maximum-likelihood
- data-vs-model-correlations
- wake-sleep
- monte-carlo-gradient
- hebb-rule
title: Boltzmann Machine Learning Rule (Wake-Sleep)
understanding: 0
---

## Definition
The **Boltzmann machine learning rule** fits the weights $W$ of a Boltzmann machine by maximum likelihood on data $\{x^{(n)}\}_1^N$. Differentiating the log likelihood and using $\partial_{w_{ij}}\ln Z(W) = \langle x_i x_j\rangle_{P(x\mid W)}$ gives a gradient that is the **difference of two correlations**:
$$\frac{\partial}{\partial w_{ij}}\ln P(\{x^{(n)}\}\mid W) = N\big[\langle x_i x_j\rangle_{\text{Data}} - \langle x_i x_j\rangle_{P(x\mid W)}\big].$$
The first term is the empirical correlation $\tfrac{1}{N}\sum_n x_i^{(n)} x_j^{(n)}$; the second is the model's own correlation, estimated by **Monte Carlo** sampling from the stochastic activity rule. Gradient ascent raises $w_{ij}$ until model correlations match data correlations.

### Wake and sleep terms
MacKay reads the two terms as 'waking' and 'sleeping' rules. While **awake**, the net measures real-world correlations and *increases* weights in proportion (a Hebbian, positive phase). While **asleep**, it 'dreams' samples from its generative model and *decreases* weights by the dreamed correlations (negative phase). At equilibrium the second-order statistics of the dream world match the real world and the weights stop changing. Starting from $W=0$, where the model correlation is zero by symmetry, one step recovers exactly the **Hebb rule** $w_{ij}=\eta\sum_n x_i^{(n)} x_j^{(n)}$ used to train the Hopfield network.

### Why it matters
This is a clean, biologically suggestive instance of learning-as-inference: contrastive 'data minus model' gradients reappear in contrastive divergence, score matching, and energy-based training. The catch is that the model correlation requires Monte Carlo sampling, making the rule slow and motivating later efficiency innovations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]