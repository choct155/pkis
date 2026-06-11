---
aliases: []
also_type: []
applies:
- energy-based-model
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
- fisher-information
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- information-theory
id: pkis:concept:stein-score-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch24
tags:
- score-function
- EBM
- Langevin-dynamics
- diffusion-models
title: Stein Score Function
understanding: 0
---

## Definition
$$s_\theta(x) \triangleq \nabla_x \log p_\theta(x) = -\nabla_x E_\theta(x)$$

The Stein score (also called Hyvärinen score) is the gradient of a log-density with respect to its input $x$, as opposed to the Fisher score $\nabla_\theta \log p_\theta(x)$ which differentiates with respect to parameters. For an EBM, the score equals the negative gradient of the energy and is independent of the intractable partition function.

### Why it matters
The Stein score is the central object in score matching, Langevin MCMC, kernelized Stein discrepancy, and diffusion-based generative models. Because it eliminates $Z_\theta$, it enables tractable gradient-based training and sampling for models whose likelihoods cannot be evaluated. The Stein score also defines the target of denoising autoencoders and connects EBMs to optimal denoising via Tweedie's formula.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[fisher-information]] — contrasts-with: Stein/Hyvärinen score differentiates log-density w.r.t. x; Fisher score differentiates w.r.t. θ
- [[energy-based-model]] — applies
[To be populated during integration]