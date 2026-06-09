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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:noninformative-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch02
- gelman-bda3-ch14
tags:
- prior
- objective-bayes
- reference-prior
title: Noninformative Prior
understanding: 0
---

## Definition
A **noninformative** (or *reference*, *vague*, *flat*, *diffuse*) prior is one chosen to play a minimal role in the posterior, so that inferences are dominated by the data — the intent being "to let the data speak for themselves."

The canonical examples are improper limits of conjugate priors. For a normal mean with known variance, taking the prior precision to zero gives the flat density

$$p(\theta) \propto \text{constant}, \qquad \theta \in (-\infty,\infty),$$

whose integral is infinite (it is *improper*), yet which yields the proper posterior $p(\theta\mid y)\approx N(\bar y,\,\sigma^2/n)$ given at least one data point. For a normal variance (known mean), the analogous limit is the improper $p(\sigma^2)\propto 1/\sigma^2$.

## Intuition
Think of a noninformative prior as the limit of a conjugate prior with *zero pseudo-observations*: it adds no information of its own, so the posterior is determined entirely by the likelihood. The price is that such a density often fails to integrate to one (it is improper) and so is not a genuine probability distribution. Improper priors are admissible only as a computational device — one must always *check that the resulting posterior is proper* (has a finite integral). The Beta$(0,0)$ prior for a binomial parameter is the cautionary case: it gives an improper posterior whenever $y=0$ or $y=n$.

A further conceptual trap is *non-invariance*: a density that is flat in one parameterization is not flat in another (uniform on $\sigma^2$ is not uniform on $\log\sigma^2$), so "complete ignorance" has no parameterization-free meaning. This is the essential weakness of Laplace's principle of insufficient reason and the motivation for invariance-based rules such as Jeffreys' prior.

### Why it matters
Noninformative priors are the workhorse when one is unwilling to quantify real prior knowledge but still wants a Bayesian posterior. They make Bayesian estimates coincide closely with classical (likelihood-dominated) answers in data-rich problems, which both reassures practitioners and clarifies the relationship between the two paradigms. Their failure modes — impropriety, parameterization-dependence, and breakdown in hierarchical variance parameters — are precisely what motivate the modern preference for *weakly informative* priors and hierarchical modeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]