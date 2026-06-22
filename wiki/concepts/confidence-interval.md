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
date_updated: '2026-06-22'
domain:
- bayesian-stats
id: pkis:concept:confidence-interval
instantiates:
- sampling-theory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch37
- cassandras-des-intro-ch10
- kroese-statistical-modeling-ch05
- angelopoulos-prediction-powered-inference-2023
tags:
- frequentist
- coverage
- confidence-level
- interval-estimation
- sampling-theory
title: Confidence Interval
understanding: 0
---

## Definition
A **confidence interval** is a data-dependent interval $(\theta_\min(D), \theta_\max(D))$ for an unknown parameter $\theta$, equipped with a **confidence level** $f$ (e.g. 95%). The confidence level is a *pre-data, frequentist* property: imagining many data sets generated from a fixed true $\theta$, the random interval covers the true value a fraction $f$ of the time, and this coverage holds for every value of $\theta$:
$$P\big(\theta \in (\theta_\min(D), \theta_\max(D)) \mid \theta\big) = f \quad \forall\,\theta.$$

The confidence level is *not* the probability that $\theta$ lies in the particular realized interval.

### Why it matters
Confidence intervals are the standard frequentist summary of estimation uncertainty, yet they are almost universally misread as posterior credible statements ('there is a 95% chance $\theta$ is in here'). MacKay uses them to expose the gap between what sampling theory delivers and what investigators actually want.

### MacKay's coverage paradox
Let $\theta$ be an integer and $x_1,x_2$ each equal $\theta$ or $\theta+1$ with probability $1/2$. The interval $[\min(x_1,x_2),\min(x_1,x_2)]$ has confidence level 75%. But on data $(29,29)$ the posterior is split 50/50 between $\theta=28$ and $29$; on data $(29,30)$ we are 100% certain $\theta=29$. In neither case is the post-data probability equal to the advertised 75%. The lesson: the 'confidence' is a property of the *procedure across repetitions*, not of the conclusion drawn from the data in hand.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sampling-theory]] — instantiates: Confidence intervals are the sampling-theory device for interval estimation, with frequency-coverage semantics.
[To be populated during integration]