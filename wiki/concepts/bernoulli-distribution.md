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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability
- statistics
- machine-learning
generalizes:
- binomial-distribution
id: pkis:concept:bernoulli-distribution
instantiates:
- exponential-family-distribution
- exponential-family
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
- murphy-pml1-intro-ch02
specializes:
- binomial-distribution
tags:
- discrete-distribution
- binary-variable
- exponential-family
- conjugate-prior
title: Bernoulli Distribution
understanding: 0
uses:
- beta-distribution
- probability-mass-function
---

## Definition
$$\text{Bern}(x|\mu) = \mu^x(1-\mu)^{1-x}, \quad x \in \{0,1\}, \quad 0 \le \mu \le 1$$

The simplest discrete probability distribution, assigning probability $\mu$ to the outcome $x=1$ and $1-\mu$ to $x=0$. It has mean $\mathbb{E}[x]=\mu$ and variance $\text{var}[x]=\mu(1-\mu)$.

### Why it matters
The Bernoulli distribution is the fundamental building block for binary classification likelihoods, the binomial and multinomial families, and logistic regression. Its exponential-family form reveals the logistic sigmoid as the canonical link function. Maximum likelihood estimation yields the sample proportion, illustrating how MLE can overfit on small samples (e.g., 3/3 heads → $\hat{\mu}=1$), motivating Bayesian treatment with a Beta conjugate prior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exponential-family]] — instantiates
- [[binomial-distribution]] — specializes
- [[probability-mass-function]] — uses
- [[exponential-family-distribution]] — instantiates: Natural parameter eta=logit(mu), sufficient statistic u(x)=x
- [[beta-distribution]] — uses: Beta is conjugate prior for Bernoulli/Binomial parameter mu
- [[binomial-distribution]] — generalizes: Binomial is sum of N i.i.d. Bernoullis
[To be populated during integration]