---
aliases: []
also_type: []
analogous-to:
- missing-data-mechanisms
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
- statistics
- machine-learning
- probabilistic-modeling
id: pkis:concept:complete-vs-incomplete-data-em
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- em-algorithm
- complete-vs-incomplete-data-em
related_concepts: []
sources:
- bishop-prml-ch09
tags:
- EM
- latent-variables
- complete-data-likelihood
- mixture-models
title: Complete Data and Incomplete Data in EM
understanding: 0
uses:
- latent-variable-models
---

## Definition
In the EM framework, the **complete data** $\{\mathbf{X}, \mathbf{Z}\}$ is the pair of observed variables $\mathbf{X}$ and latent variables $\mathbf{Z}$; the **incomplete data** is $\mathbf{X}$ alone. The complete-data log likelihood $\ln p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})$ is typically tractable (e.g., the sum and log commute for exponential-family components), whereas the incomplete-data log likelihood
$$\ln p(\mathbf{X}\mid\boldsymbol{\theta}) = \ln\!\sum_{\mathbf{Z}} p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})$$
contains the log of a sum, making direct optimisation difficult.

Intuition: introducing latent variables moves the intractable summation inside a log into a position where it can be handled via an expectation.

### Why it matters
This dichotomy motivates the EM algorithm: because the complete data is unobserved, EM maximises the *expected* complete-data log likelihood $Q(\boldsymbol{\theta},\boldsymbol{\theta}^{\text{old}})=\mathbb{E}_{\mathbf{Z}|\mathbf{X},\boldsymbol{\theta}^{\text{old}}}[\ln p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})]$. For exponential-family components, maximising $Q$ is a standard closed-form problem, while maximising the incomplete-data likelihood directly is not.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[complete-vs-incomplete-data-em]] — prerequisite-of: self-reference removed — linking to em-algorithm instead
- [[missing-data-mechanisms]] — analogous-to
- [[latent-variable-models]] — uses
- [[em-algorithm]] — prerequisite-of
[To be populated during integration]