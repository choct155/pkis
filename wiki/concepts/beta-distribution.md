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
- statistical-learning
id: pkis:concept:beta-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch23
tags:
- probability-distribution
- conjugate-prior
- binomial
- prior-over-probability
title: Beta Distribution
understanding: 0
---

## Definition
The **beta distribution** is a density over a variable $p$ that is itself a probability, $p \in (0,1)$. With shape parameters $u_1, u_2 > 0$,

$$P(p \mid u_1, u_2) = \frac{1}{Z(u_1,u_2)}\, p^{u_1-1}(1-p)^{u_2-1}, \qquad Z(u_1,u_2) = \frac{\Gamma(u_1)\Gamma(u_2)}{\Gamma(u_1+u_2)}.$$

The normalizer is the **beta function**. Intuitively the exponents act like pseudo-counts: $u_1-1$ prior successes and $u_2-1$ prior failures, so the density concentrates near $p = u_1/(u_1+u_2)$ as the counts grow.

### Special cases
Familiar priors are corners of the beta family: $u_1=u_2=1$ gives the uniform distribution; $u_1=u_2=0.5$ gives the Jeffreys prior; and $u_1=u_2=0$ gives the improper Laplace prior. In the **logit basis** $l \equiv \ln\frac{p}{1-p}$ the beta is always a smooth bell-shaped density, even when $P(p)$ has integrable singularities at $p=0$ or $p=1$ — another instance of a singularity being a basis artefact.

### Why it matters
The beta is the conjugate prior for the binomial bias: observing $r$ successes in $N$ trials updates $\mathrm{Beta}(u_1,u_2) \to \mathrm{Beta}(u_1+r,\ u_2+N-r)$, keeping inference in closed form. This conjugacy underlies Laplace's rule of succession and makes the beta the default model for any single unknown probability.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]