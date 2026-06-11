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
- probability-theory
- measure-theory
id: pkis:concept:probability-space
instantiates:
- probability-theory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- random-variable
- conditional-independence
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- probability
- measure-theory
- sigma-field
- sample-space
- foundations
title: Probability Space
understanding: 0
uses:
- kolmogorov-axioms
---

## Definition
$$( \Omega,\, \mathcal{F},\, \mathbb{P} )$$

A probability space is a triple consisting of: the **sample space** $\Omega$ (the set of all possible outcomes), the **event space** $\mathcal{F}$ (a $\sigma$-field of subsets of $\Omega$), and the **probability measure** $\mathbb{P}: \mathcal{F} \to [0,1]$ satisfying the Kolmogorov axioms (non-negativity, normalization, countable additivity). It is the foundational mathematical object on which all probability theory is built.

### Why it matters
Every probabilistic model—from simple coin flips to complex Bayesian networks—is implicitly defined as a probability space; making this structure explicit exposes what "probability" means and clarifies when operations such as conditioning and marginalization are well-defined.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conditional-independence]] — prerequisite-of
- [[probability-theory]] — instantiates
- [[random-variable]] — prerequisite-of
- [[kolmogorov-axioms]] — uses
[To be populated during integration]