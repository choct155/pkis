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
contrasts-with:
- conjugate-prior
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:hyperprior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- hierarchical-bayesian-models
related_concepts: []
sources:
- gelman-bda3-ch05
tags:
- hierarchical-models
- prior-construction
- variance-components
- weakly-informative-priors
title: Hyperprior Distribution
understanding: 0
---

## Definition
The prior distribution p(φ) assigned to the hyperparameters φ of a hierarchical model — the parameters that govern the population distribution from which group-level parameters are drawn. Making φ itself uncertain (rather than fixing it at a point estimate) is precisely what distinguishes a full hierarchical Bayesian analysis from empirical-Bayes-style plug-in approximations, and the choice of hyperprior, especially for variance components, can materially change inferences.

## Role in the Hierarchy
In a hierarchical model the joint prior factors as p(φ,ω) = p(φ)·p(ω|φ), and the data depend on φ only through ω, so
$$p(\phi,\omega\mid y) \propto p(\phi)\, p(\omega\mid\phi)\, p(y\mid\omega).$$
The hyperprior p(φ) is what makes φ a genuine random quantity, propagating hyperparameter uncertainty into the posterior for the ω_j's — the key flaw of plug-in estimates is that they ignore this uncertainty.

## Priors for Variance Components (the hard case)
For a group-level scale parameter τ, the choice of 'noninformative' hyperprior is delicate, especially when the number of groups J is small:
- **Uniform on τ** yields a proper posterior for J ≥ 3 and behaves well in the 8-schools example; it has a mild upward miscalibration but lets the data dominate. The recommended default for noninformative work.
- **Uniform on log τ** (∝ τ⁻¹) gives an *improper* posterior: the marginal likelihood stays finite as τ→0, so infinite mass piles up at logτ→−∞. The data can never rule out τ = 0.
- **Inverse-gamma(ε,ε) on τ²**, conditionally conjugate, is *not* noninformative: it improperly limits as ε→0 and exerts a strong pull toward zero, with inferences highly sensitive to ε.
- **Half-Cauchy(0, A)** is a convenient weakly informative family with a broad peak at zero and a gentle tail; it tames the unrealistic upper tail when J is very small (the 3-schools example) while still letting the data speak.

## Guidance
Any noninformative or weakly informative hyperprior is provisional: fit the model, inspect the posterior, and revise the hyperprior if it implies conclusions that contradict substantive knowledge. With improper hyperpriors, always verify the resulting posterior is proper.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conjugate-prior]] — contrasts-with: Conditionally conjugate inverse-gamma hyperpriors are convenient but, unlike a genuine conjugate prior at the data level, are not noninformative for variance components.
- [[hierarchical-bayesian-models]] — prerequisite-of: Specifying a hyperprior on the hyperparameters is required to complete a hierarchical Bayesian model.
[To be populated during integration]