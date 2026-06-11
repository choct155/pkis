---
aliases: []
also_type: []
analogous-to:
- iteratively-reweighted-least-squares
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
extends:
- gaussian-mixture-models
id: pkis:technique:mixture-linear-regression-em
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch14
specializes:
- mixture-models
tags:
- mixture-model
- regression
- EM
- weighted-least-squares
- latent-variable
title: Mixture of Linear Regression Models (EM)
understanding: 0
uses:
- em-algorithm
- linear-regression
---

## Definition
A mixture of $K$ Gaussian linear regression models with shared precision $\beta$:
$$p(t|\boldsymbol{\phi},\theta) = \sum_{k=1}^{K}\pi_k\,\mathcal{N}(t\mid\mathbf{w}_k^T\boldsymbol{\phi},\,\beta^{-1})$$
fit by EM. The M-step for $\mathbf{w}_k$ solves a *weighted* normal equation:
$$\mathbf{w}_k = (\boldsymbol{\Phi}^T\mathbf{R}_k\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^T\mathbf{R}_k\mathbf{t}, \quad \mathbf{R}_k=\operatorname{diag}(\gamma_{nk})$$
where responsibilities $\gamma_{nk} = p(k|\boldsymbol{\phi}_n,\theta^{\text{old}})$ come from the E-step.

### Why it matters
This model captures multimodal, heteroscedastic regression distributions that a single linear model cannot represent, while remaining analytically tractable in its M-step (weighted least squares with closed form). Setting the mixing coefficients to be input-dependent extends this to a mixture of experts, and the Bayesian extension uses variational inference. The model illustrates the general principle that EM for conditional mixture models reduces each M-step to a separate, responsibility-weighted version of the corresponding single-component problem.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[iteratively-reweighted-least-squares]] — analogous-to
- [[mixture-models]] — specializes
- [[linear-regression]] — uses
- [[gaussian-mixture-models]] — extends
- [[em-algorithm]] — uses
[To be populated during integration]