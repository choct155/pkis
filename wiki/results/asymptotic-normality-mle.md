---
aliases: []
also_type: []
analogous-to:
- central-limit-theorem
- bernstein-von-mises-theorem
applies:
- maximum-likelihood-estimation
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- statistics
- frequentist-statistics
id: pkis:result:asymptotic-normality-mle
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
- kroese-statistical-modeling-ch06
tags:
- MLE
- asymptotic-theory
- Fisher-information
- sampling-distribution
- central-limit-theorem
title: Asymptotic Normality of the MLE
understanding: 0
uses:
- score-function
- cramer-rao-bound
- sampling-distribution
---

## Definition
**Theorem.** Under suitable regularity conditions, as the sample size $N\to\infty$:
$$\sqrt{N}(\hat{\theta}_{\text{MLE}} - \theta^*) \xrightarrow{d} \mathcal{N}\bigl(0,\, F(\theta^*)^{-1}\bigr)$$
where $\theta^*$ is the true parameter and $F(\theta^*)$ is the Fisher information matrix evaluated at $\theta^*$.

Equivalently, the sampling distribution of the MLE is approximately $\mathcal{N}(\theta^*,\, F(\theta^*)^{-1}/N)$ for large $N$, and the expected Hessian of the NLL over $N$ i.i.d. samples satisfies $\mathbb{E}[H(D)|\theta]=NF(\theta)$.

### Why it matters
This result justifies using the observed Hessian (or its expectation, the FIM) to construct standard errors and confidence intervals for MLE estimates. It also explains why the Bernstein–von Mises theorem yields Gaussian posteriors in large samples: the likelihood dominates the prior and concentrates around the MLE at rate $1/\sqrt{N}$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sampling-distribution]] — uses
- [[cramer-rao-bound]] — uses
- [[bernstein-von-mises-theorem]] — analogous-to
- [[central-limit-theorem]] — analogous-to
- [[maximum-likelihood-estimation]] — applies
- [[score-function]] — uses
[To be populated during integration]