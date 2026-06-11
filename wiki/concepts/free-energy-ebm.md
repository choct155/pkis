---
aliases: []
also_type: []
analogous-to:
- variational-free-energy
- elbo
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
- probabilistic-graphical-models
- deep-learning
- statistical-physics
id: pkis:concept:free-energy-ebm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch16
tags:
- energy-based-model
- latent-variables
- RBM
- variational-inference
- partition-function
title: Free Energy (Latent Variable EBMs)
understanding: 0
uses:
- energy-based-model
- partition-function
---

## Definition
$$\mathcal{F}(x) = -\log \sum_{h} \exp(-E(x,h))$$

The **free energy** of an energy-based model with latent variables $h$ is the negative log of the marginal unnormalized probability $\tilde{p}(x)$ obtained by summing out $h$. It relates to the true log-probability via $\log p(x) = -\mathcal{F}(x) - \log Z$.

### Why it matters
The free energy provides a tractable surrogate objective: if the sum over $h$ can be computed (as in the RBM, where the conditional is factorial), then $\mathcal{F}(x)$ and its gradient are available without computing $Z$. This makes contrastive divergence and related training algorithms practical. The term is borrowed from thermodynamics, where free energy quantifies the usable work in a system; the analogy is that $\mathcal{F}$ measures how well the model explains $x$ after *integrating out* the internal degrees of freedom.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partition-function]] — uses
- [[elbo]] — analogous-to
- [[variational-free-energy]] — analogous-to
- [[energy-based-model]] — uses
[To be populated during integration]