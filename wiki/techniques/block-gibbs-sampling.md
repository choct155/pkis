---
aliases: []
also_type: []
applies:
- restricted-boltzmann-machine
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
- statistics
- probabilistic-inference
id: pkis:technique:block-gibbs-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
specializes:
- gibbs-sampler
tags:
- gibbs-sampling
- block-update
- rbm
- conditional-independence
- mcmc
title: Block Gibbs Sampling
understanding: 0
uses:
- conditional-independence
- contrastive-divergence
---

## Definition
A variant of Gibbs sampling in which a **block** of variables that are conditionally independent given their Markov blanket is sampled jointly in a single step, rather than updating one variable at a time:
$$\mathbf{x}_{\mathcal{B}} \sim p(\mathbf{x}_{\mathcal{B}} \mid \mathbf{x}_{-\mathcal{B}})$$
where $\mathcal{B}$ indexes conditionally independent variables.

In a Restricted Boltzmann Machine (RBM), all hidden units are conditionally independent given the visibles and vice versa, so both the full hidden layer $\mathbf{h}$ and the full visible layer $\mathbf{v}$ constitute valid blocks.

### Why it matters
Block updates reduce autocorrelation between successive samples and can dramatically improve mixing when the block structure matches the model's independence structure. This is the basis of the efficient Gibbs samplers used in RBM training (contrastive divergence) and in exact inference for models with conjugate blocks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[contrastive-divergence]] — uses: CD in RBMs performs one or k steps of block Gibbs sampling
- [[restricted-boltzmann-machine]] — applies: RBM bipartite structure enables exact block updates of all hidden or all visible units
- [[conditional-independence]] — uses: requires the block to be conditionally independent given the rest
- [[gibbs-sampler]] — specializes: updates a conditionally independent block in one step
[To be populated during integration]