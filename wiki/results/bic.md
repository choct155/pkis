---
aliases: []
also_type: []
applies:
- bayesian-model-comparison
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- Bayesian-inference
- model-selection
id: pkis:result:bic
instantiates:
- information-criteria
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
tags:
- model-comparison
- penalised-likelihood
- Schwarz-criterion
- Occam-factor
- marginal-likelihood
title: BIC (Bayesian Information Criterion)
understanding: 0
uses:
- laplace-approximation
- marginal-likelihood
- occam-factor
---

## Definition
$$\ln p(\mathcal{D}) \approx \ln p(\mathcal{D}|\boldsymbol{\theta}_{\text{MAP}}) - \frac{M}{2}\ln N$$

where $M$ is the number of model parameters and $N$ is the number of data points. BIC is derived from the Laplace approximation to the log model evidence by assuming a broad Gaussian prior and that the Hessian of the log-likelihood scales as $N$. Compared with AIC ($-M$), BIC imposes a stronger $\frac{M}{2}\ln N$ penalty for model complexity.

### Why it matters
BIC is a practical Bayesian model-selection score that does not require specifying a prior. It asymptotically approximates the log marginal likelihood, embodies an automatic Occam's razor, and is consistent (selects the true model as $N\to\infty$ among a fixed set). Its derivation from the Laplace approximation reveals the conditions under which it may be misleading (low $N$, rank-deficient Hessian, multimodal posteriors).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-model-comparison]] — applies
- [[occam-factor]] — uses
- [[marginal-likelihood]] — uses
- [[laplace-approximation]] — uses
- [[information-criteria]] — instantiates
[To be populated during integration]