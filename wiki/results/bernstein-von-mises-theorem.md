---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:result:bernstein-von-mises-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch04
tags:
- asymptotics
- consistency
- fisher-information
- frequentist-bayesian-correspondence
title: Bernstein-von Mises Theorem (Posterior Asymptotic Normality)
understanding: 0
---

## Definition
Under regularity conditions (the likelihood is continuous in omega and omega_0 lies in the interior, not on the boundary, of the parameter space), as n -> infinity the posterior distribution of the parameter vector omega approaches a multivariate normal centered at omega_0 with covariance (n*J(omega_0))^{-1}, where J is the Fisher information. If the true data-generating distribution lies in the parametric family, f(y) = p(y|omega_0), then consistency also holds: the posterior contracts to a point mass at omega_0. When the truth is outside the family, omega_0 is replaced by the pseudo-true value minimizing the Kullback-Leibler divergence from f to the model. The mechanism is transparent from the Taylor expansion of the log-posterior: the quadratic coefficient is one prior term plus a sum of n likelihood terms, each with expectation approximately -J(omega_0) under the true sampling distribution, so for large n the curvature is well approximated by n*J(omega-hat) or n*J(omega_0) and the prior contribution becomes negligible. A key corollary is the large-sample correspondence between Bayesian and frequentist inference: the posterior law of [I(omega-hat)]^{1/2}(omega - omega-hat) and the repeated-sampling law of the same quantity both converge to N(0, I), so a 95% central posterior interval covers the true value 95% of the time under repeated sampling. The theorem is the formal basis for the normal approximation and for treating frequentist point-estimate-plus-standard-error summaries as approximate Bayesian inferences. Detailed statements and proofs are given in Appendix B of BDA3.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]