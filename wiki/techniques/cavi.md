---
aliases: []
also_type: []
analogous-to:
- gibbs-sampler
applies:
- ising-model
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
- bayesian-inference
id: pkis:technique:cavi
instantiates:
- mean-field-approximation-vi
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
specializes:
- coordinate-ascent-vi
tags:
- CAVI
- coordinate-ascent
- mean-field
- variational-inference
- free-form-VI
title: Coordinate Ascent Variational Inference (CAVI)
understanding: 0
uses:
- markov-blanket
---

## Definition
$$q_j^*(z_j) \propto \exp\!\Bigl(\mathbb{E}_{z_{\mathrm{mb}_j}}[\log \tilde{p}(z_j, z_{\mathrm{mb}_j})]\Bigr)$$

CAVI iteratively updates each variational factor $q_j$ in turn while holding the others fixed. At each step, the update is obtained in closed form as the exponential of the expected log joint w.r.t. the Markov blanket of $z_j$. Convergence to a local optimum of the ELBO is guaranteed because the bound is concave in each factor separately.

### Why it matters
CAVI is the workhorse of **free-form VI**: no distributional family need be chosen by hand — the functional form of each $q_j$ falls out automatically from the conjugate structure of the model. It enables efficient inference in Bayesian mixture models, LDA, and other hierarchical models with conjugate priors.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ising-model]] — applies: Section 10.3.2 applies CAVI to mean field inference in the Ising model for image denoising.
- [[gibbs-sampler]] — analogous-to: CAVI update equations are structurally parallel to Gibbs sampling conditionals (Algorithm 10.4 note).
- [[markov-blanket]] — uses: Each CAVI update averages over the Markov blanket of the updated variable.
- [[coordinate-ascent-vi]] — specializes: CAVI is the canonical free-form implementation of coordinate ascent for VI.
- [[mean-field-approximation-vi]] — instantiates: CAVI is the coordinate ascent algorithm that optimizes the mean field variational objective.
[To be populated during integration]