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
- bayesian-inference
id: pkis:technique:cavi
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
tags:
- CAVI
- coordinate-ascent
- mean-field
- variational-inference
- free-form-VI
title: Coordinate Ascent Variational Inference (CAVI)
understanding: 0
---

## Definition
$$q_j^*(z_j) \propto \exp\!\Bigl(\mathbb{E}_{z_{\mathrm{mb}_j}}[\log \tilde{p}(z_j, z_{\mathrm{mb}_j})]\Bigr)$$

CAVI iteratively updates each variational factor $q_j$ in turn while holding the others fixed. At each step, the update is obtained in closed form as the exponential of the expected log joint w.r.t. the Markov blanket of $z_j$. Convergence to a local optimum of the ELBO is guaranteed because the bound is concave in each factor separately.

### Why it matters
CAVI is the workhorse of **free-form VI**: no distributional family need be chosen by hand — the functional form of each $q_j$ falls out automatically from the conjugate structure of the model. It enables efficient inference in Bayesian mixture models, LDA, and other hierarchical models with conjugate priors.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]