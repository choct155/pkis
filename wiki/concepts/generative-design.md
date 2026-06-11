---
aliases: []
also_type: []
applies:
- deep-generative-model-taxonomy
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
- machine-learning
- generative-models
- applications
id: pkis:concept:generative-design
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- drug-discovery
- molecular-generation
- Bayesian-optimization
- VAE
- design
title: Generative Design
understanding: 0
uses:
- variational-autoencoder
- bayesian-optimization
- latent-space-interpolation
---

## Definition
**Generative design** uses a (deep) generative model to propose candidate objects — molecules, protein sequences, circuit layouts, materials — that satisfy desired property constraints. A common workflow:

1. Train a VAE (or similar model) on a library of unlabeled examples to learn a smooth latent space.
2. Use a property predictor or black-box oracle to score objects.
3. Perform **Bayesian optimization** in the latent space to find $z^* = \arg\max_{z} \text{score}(d(z))$.
4. Decode $z^*$ to obtain a novel candidate.

The generative model acts as a differentiable, continuous surrogate for a discrete combinatorial search space.

### Why it matters
Generative design is a major driver of generative model adoption in drug discovery (molecular generation), materials science, and protein engineering. The combination of VAE + Bayesian optimization is the canonical baseline for data-efficient search in structured, high-dimensional design spaces.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[deep-generative-model-taxonomy]] — applies
- [[latent-space-interpolation]] — uses
- [[bayesian-optimization]] — uses
- [[variational-autoencoder]] — uses
[To be populated during integration]