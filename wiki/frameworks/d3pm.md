---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- generative-models
- natural-language-processing
id: pkis:framework:d3pm
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- discrete-diffusion
- categorical-distribution
- text-generation
- masked-language-model
title: Discrete Denoising Diffusion Probabilistic Model (D3PM)
understanding: 0
---

## Definition
A discrete-time diffusion framework for categorical data in which the forward process is defined by a **row-stochastic transition matrix** $Q_t$:

$$q(x_t|x_{t-1}) = \text{Cat}(x_t\mid x_{t-1}Q_t), \qquad q(x_t|x_0) = \text{Cat}(x_t\mid x_0\bar Q_t), \quad \bar Q_t=Q_1Q_2\cdots Q_t$$

The posterior $q(x_{t-1}|x_t,x_0)$ is also categorical and computable in closed form. Common choices for $Q_t$ include: **uniform** (adds uniform noise), **absorbing/mask** (transitions to a special MASK token), and **discretised Gaussian** (transitions to nearby ordinal states).

The reverse process $p_\theta(x_{t-1}|x_t)$ is parameterised by predicting the clean token $\tilde p_\theta(\tilde x_0|x_t)$ and marginalising:
$$p_\theta(x_{t-1}|x_t)\propto\sum_{\tilde x_0}q(x_{t-1}|x_t,\tilde x_0)\tilde p_\theta(\tilde x_0|x_t)$$

### Why it matters
D3PM extends diffusion to text, semantic labels, and other discrete modalities. The masking variant subsumes BERT's masked language-model objective as a one-step special case, and the masking diffusion variant subsumes any-order autoregressive models. It also connects to MaskGIT-style parallel iterative decoding, which is far faster than sequential autoregressive generation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]