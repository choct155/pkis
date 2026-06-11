---
aliases: []
also_type: []
applies:
- density-estimation
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- inverse-autoregressive-flow
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- generative-models
id: pkis:concept:masked-autoregressive-flow
instantiates:
- autoregressive-flow
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- normalizing-flow
- autoregressive
- masked-network
- density-estimation
title: Masked Autoregressive Flow (MAF)
understanding: 0
---

## Definition
MAF is an affine autoregressive flow in which the combined conditioner $\Theta(x) = (\theta_1, \ldots, \theta_D)$ is implemented as a single masked MLP (MADE). Binary masks zero out connections so that $\theta_i$ receives no information from $x_{j}$ for $j \geq i$, preserving autoregressivity while sharing parameters across all conditioners.

$$x_i = u_i \exp(\alpha_i(x_{1:i-1})) + \mu_i(x_{1:i-1}), \quad \log|\det J(f)| = \sum_{i=1}^D \alpha_i(x_{1:i-1}).$$

A single forward pass of the masked network evaluates all $\theta_i$ simultaneously, making density evaluation $O(1)$ network calls; sampling requires $D$ sequential network calls.

### Why it matters
MAF achieves state-of-the-art density estimation while being parameter-efficient. It is the inverse of IAF: the computational asymmetry (fast density, slow sampling) makes MAF suited for MLE training but less so for variational inference sampling tasks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inverse-autoregressive-flow]] — contrasts-with
- [[density-estimation]] — applies
- [[autoregressive-flow]] — instantiates
[To be populated during integration]