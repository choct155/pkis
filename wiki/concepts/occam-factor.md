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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:occam-factor
instantiates:
- occams-razor
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-model-comparison
related_concepts: []
sources:
- mackay-itila-ch28
tags:
- marginal-likelihood
- model-evidence
- laplace-approximation
- model-comparison
- complexity-penalty
title: The Occam Factor
understanding: 0
---

## Definition
The **Occam factor** is the automatic complexity penalty that arises when the model evidence (marginal likelihood) is approximated by Laplace's method. Around a sharply-peaked posterior at $\mathbf{w}_{MP}$, the evidence factorizes as
$$P(D\mid H_i) \simeq \underbrace{P(D\mid \mathbf{w}_{MP}, H_i)}_{\text{best-fit likelihood}} \times \underbrace{P(\mathbf{w}_{MP}\mid H_i)\,\sigma_{w\mid D}}_{\text{Occam factor}}.$$
The first term rewards fit; the Occam factor (magnitude $<1$) penalizes the model for using its parameters.

### Ratio-of-volumes interpretation
For a prior that is uniform over a range $\sigma_w$, so $P(w_{MP}\mid H_i)=1/\sigma_w$, the penalty becomes
$$\text{Occam factor} = \frac{\sigma_{w\mid D}}{\sigma_w},$$
the ratio of the posterior accessible volume of parameter space to the prior accessible volume — the factor by which the hypothesis space *collapses* when the data arrive. Equivalently, a model with prior range $\sigma_w$ is a bundle of $\sigma_w/\sigma_{w\mid D}$ exclusive submodels, of which one survives; the Occam factor is the inverse of that count. Its logarithm is the information gained about the parameters.

### Several parameters
With a Gaussian posterior of Hessian $A=-\nabla\nabla\ln P(\mathbf{w}\mid D,H_i)$,
$$\text{Occam factor} = P(\mathbf{w}_{MP}\mid H_i)\,\det{}^{-1/2}(A/2\pi).$$
It depends only on the error bars already computed when fitting the model — so model comparison costs no more than parameter estimation plus its curvature.

### Why it matters
The Occam factor turns Occam's razor from a slogan into a computable number. It penalizes models both for having many free parameters and for needing fine tuning (small $\sigma_{w\mid D}$). The chosen model trades off this complexity measure against data misfit, automatically resolving the over-fitting that defeats maximum-likelihood model selection.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-model-comparison]] — prerequisite-of: Understanding the Occam factor explains why evidence-based comparison favours simpler models.
- [[occams-razor]] — instantiates: The Occam factor is the quantitative, computable realization of the qualitative Occam's-razor principle.
[To be populated during integration]