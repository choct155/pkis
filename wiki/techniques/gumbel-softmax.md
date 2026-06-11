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
- machine-learning
- probabilistic-modeling
id: pkis:technique:gumbel-softmax
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
- murphy-pml2-advanced-ch21
tags:
- discrete-relaxation
- categorical
- reparameterization
- gradient-estimation
- temperature
title: Gumbel-Softmax (Concrete Distribution)
understanding: 0
---

## Definition
The Gumbel-softmax trick provides a continuous, reparameterizable relaxation of a discrete categorical variable. Given unnormalized log-probabilities $\log\alpha_k$ and i.i.d. Gumbel noise $\epsilon_k \sim \text{Gumbel}(0,1)$, define
$$x_k = \frac{\exp\bigl((\log\alpha_k + \epsilon_k)/\tau\bigr)}{\sum_{k'} \exp\bigl((\log\alpha_{k'} + \epsilon_{k'})/\tau\bigr)}$$
where $\tau > 0$ is a **temperature** hyperparameter. As $\tau \to 0$, $\mathbf{x}$ converges to a one-hot sample from $\text{Cat}(\boldsymbol{\alpha})$ (the **Gumbel-max trick**); as $\tau \to \infty$, $\mathbf{x}$ approaches the uniform distribution.

Gumbel noise is sampled as $\epsilon_k = -\log(-\log u_k)$, $u_k \sim \text{Uniform}(0,1)$.

### Why it matters
The Gumbel-softmax enables reparameterized gradients through categorical choices, unlocking end-to-end training of models with discrete latent variables (e.g., discrete VAEs, hard attention). Temperature annealing schedules allow trading off between gradient variance and approximation quality during training.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]