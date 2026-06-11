---
aliases: []
also_type: []
analogous-to:
- variational-free-energy
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
- variational-autoencoder
- normalizing-flows
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- probabilistic-modeling
- statistical-physics
generalizes:
- boltzmann-machine
- undirected-graphical-models
- ising-model
id: pkis:concept:energy-based-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch16
- murphy-pml2-advanced-ch24
specializes:
- undirected-graphical-models
tags:
- graphical-models
- undirected-models
- deep-learning
- boltzmann-machine
- partition-function
title: Energy-Based Model (EBM)
understanding: 0
uses:
- partition-function
- clique-potential
- gibbs-inequality
---

## Definition
$$\tilde{p}(\mathbf{x}) = \exp(-E(\mathbf{x})), \quad p(\mathbf{x}) = \frac{\exp(-E(\mathbf{x}))}{Z}$$

An undirected probabilistic model in which the unnormalized probability of every configuration is guaranteed positive by defining it as the exponential of a negative scalar *energy function* $E(\mathbf{x})$; lower energy means higher probability.

### Why it matters
The exponential form removes the non-negativity constraint on learning, allowing unconstrained optimization of $E$. It unifies a large family of models (Boltzmann machines, Ising models, restricted Boltzmann machines) under one framework and connects statistical mechanics terminology (energy, partition function, free energy) to probabilistic modeling. The free energy for models with latent variables $h$ is $\mathcal{F}(x) = -\log \sum_h \exp(-E(x,h))$, which collapses the latent variables into an effective energy over visible variables.

### Connections
- [[normalizing-flows]] — contrasts-with: Normalizing flows maintain tractable likelihoods via invertible maps; EBMs trade this for unconstrained architectures
- [[variational-autoencoder]] — contrasts-with: VAEs use directed latent-variable models with tractable ELBO; EBMs use undirected energy functions with intractable Z
- [[ising-model]] — generalizes: Ising model is an EBM with pairwise binary interactions
- [[gibbs-inequality]] — uses: Gibbs distribution is the form of EBM; Gibbs inequality underpins MLE equivalence to KL minimization
- [[undirected-graphical-models]] — generalizes: EBMs are a flexible superset of undirected graphical models (Markov random fields); UGMs impose additional Markov structure on the energy
- [[variational-free-energy]] — analogous-to
- [[clique-potential]] — uses
- [[boltzmann-machine]] — generalizes
- [[partition-function]] — uses
- [[undirected-graphical-models]] — specializes
The product-of-experts interpretation: each additive term in $E(\mathbf{x})$ corresponds to a separate factor (expert) in $\tilde{p}$, so the joint model enforces multiple soft constraints simultaneously via multiplication of probabilities.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]