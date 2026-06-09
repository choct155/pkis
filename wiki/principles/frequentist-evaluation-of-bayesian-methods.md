---
aliases: []
also_type: []
applies:
- confidence-interval
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
contrasts-with:
- hypothesis-testing
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:principle:frequentist-evaluation-of-bayesian-methods
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch04
tags:
- operating-characteristics
- coverage
- consistency
- efficiency
- calibration
- repeated-sampling
title: Frequentist Evaluation of Bayesian Methods
understanding: 0
uses:
- bernstein-von-mises-theorem
- sampling-theory
---

## Definition
The practice of judging a Bayesian procedure by its operating characteristics under repeated sampling, treating the inference as one element of a sequence of hypothetical replications with the parameter held fixed. The relevant frequentist criteria are: consistency (the point estimate's sampling distribution contracts to omega_0 as n grows), asymptotic unbiasedness ((E(omega-hat|omega_0) - omega_0)/sd(omega-hat|omega_0) -> 0), efficiency (mean squared error attains its lowest achievable value, with asymptotic efficiency = 1 in the limit), and confidence coverage (a region C(y) contains omega_0 at least 100(1-alpha)% of the time). Under mild regularity the posterior mean, median, and mode are consistent, asymptotically unbiased, and asymptotically efficient, and Bayesian (1-alpha) posterior intervals have approximately (1-alpha) frequentist coverage even in fairly small samples. Gelman's stance is that frequentist evaluation is a useful external check on a Bayesian procedure but coverage alone is not a sufficient basis for inference (one can construct intervals that are empty 5% of the time and the whole real line 95% of the time, attaining exact coverage while being useless). The principle motivates simulation-based calibration: drawing omega from the prior, y from the model, and verifying that the 50% interval contains the truth 50% of the time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hypothesis-testing]] — contrasts-with: Frequentist evaluation is endorsed for coverage/consistency but Gelman rejects point-null hypothesis testing as a comparison criterion.
- [[sampling-theory]] — uses: Operating characteristics (consistency, efficiency, coverage) are sampling-theory constructs applied to Bayesian estimators.
- [[bernstein-von-mises-theorem]] — uses: Large-sample correspondence (posterior intervals attaining nominal frequentist coverage) follows from posterior asymptotic normality.
- [[confidence-interval]] — applies: Coverage of Bayesian posterior intervals is assessed against the frequentist confidence-interval criterion under repeated sampling.
[To be populated during integration]