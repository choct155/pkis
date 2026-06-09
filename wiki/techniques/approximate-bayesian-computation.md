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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:technique:approximate-bayesian-computation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch13
tags:
- likelihood-free
- simulation-based-inference
- rejection-sampling
- posterior-approximation
- summary-statistics
title: Approximate Bayesian Computation (ABC)
understanding: 0
---

## Definition
Approximate Bayesian computation (ABC) is a class of likelihood-free posterior inference procedures that require only the ability to simulate data from the model, not to evaluate the likelihood. The basic rejection form: draw omega from the prior p(omega), simulate replicated data y_rep from the data model p(y_rep|omega), compute a discrepancy d(y_rep, y) (zero when identical, larger when more different), and accept omega if d(y_rep, y) < epsilon. Accepted draws approximate the posterior because parameters are retained in proportion to the probability that they generate data close to the observed data, which approximates the likelihood.

ABC faces three coupled challenges: (1) choosing a discrepancy d that captures the parameter-relevant aspects of the data (ideally the sufficient statistics) without demanding agreement on irrelevant noise; (2) setting the tolerance epsilon small enough to be informative but large enough to avoid rejecting nearly all simulations; (3) controlling an unacceptably high rejection rate when the prior is broad. These are mitigated by hybrids: drawing proposals from a non-prior distribution and correcting with importance sampling, or moving through parameter space with MCMC steps. A related idea is the substitution likelihood, which replaces the full likelihood with a rank- or quantile-based 'almost-likelihood' (e.g. enabling a copula joint model where the marginals would not fit), broadening the class of applicable models. ABC is the natural tool when the generative model is easy to simulate but the likelihood is intractable or unavailable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]