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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- generative-models
id: pkis:concept:differentiable-generator-network
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- latent-variable
- generator
- reparameterisation
- implicit-density
title: Differentiable Generator Network
understanding: 0
---

## Definition
A neural network $g(\mathbf{z};\boldsymbol{\theta})$ that maps a simple latent distribution $p(\mathbf{z})$ (e.g., $\mathcal{N}(0,I)$) to samples or conditional distributions over observed data $\mathbf{x}$, with the implicit data distribution:
$$p_x(\mathbf{x})=\frac{p_z(g^{-1}(\mathbf{x}))}{\left|\det\left(\frac{\partial g}{\partial\mathbf{z}}\right)\right|}$$
(when $g$ is invertible), or by marginalisation $p(\mathbf{x})=\mathbb{E}_{\mathbf{z}}p(\mathbf{x}|\mathbf{z})$ when $g$ parametrises a conditional. Gradients of a loss on $\mathbf{x}$ flow back through $g$ to $\boldsymbol{\theta}$ via the reparameterisation trick.

### Why it matters
Differentiable generator networks are the unifying component of VAEs, GANs, normalising flows, and generative moment matching networks. They replace explicit density specification with a learned nonlinear change-of-variables, enabling modelling of complex high-dimensional distributions without intractable partition functions or MCMC.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]