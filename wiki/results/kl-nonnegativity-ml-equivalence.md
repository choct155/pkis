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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- information-theory
- statistics
- machine-learning
id: pkis:result:kl-nonnegativity-ml-equivalence
instantiates:
- kl-divergence
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- elbo
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- KL-divergence
- Jensen-inequality
- maximum-likelihood
- mutual-information
- convexity
title: KL Divergence Non-negativity and Equivalence to Maximum Likelihood
understanding: 0
uses:
- jensens-inequality
- maximum-likelihood-estimation
- mutual-information
- likelihood-function
---

## Definition
The Kullback–Leibler divergence between distributions $p$ and $q$ satisfies
$$\mathrm{KL}(p\|q) = -\int p(x)\ln\frac{q(x)}{p(x)}\,dx \geq 0,$$
with equality iff $p=q$ almost everywhere. The proof uses Jensen's inequality applied to the strictly convex function $-\ln x$:
$$\mathrm{KL}(p\|q)\geq -\ln\int q(x)\,dx = 0.$$

Minimising $\mathrm{KL}(p\|q(\cdot|\theta))$ over $\theta$ is equivalent to maximising the log-likelihood $\sum_n \ln q(x_n|\theta)$ over the empirical distribution, because $\int p(x)\ln p(x)\,dx$ does not depend on $\theta$.

### Why it matters
Links information-theoretic model fitting with maximum likelihood estimation, mutual information, variational inference (ELBO), and compression. Mutual information $I[x,y]=\mathrm{KL}(p(x,y)\|p(x)p(y))\geq 0$ follows immediately.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[elbo]] — prerequisite-of
- [[likelihood-function]] — uses
- [[mutual-information]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[jensens-inequality]] — uses
- [[kl-divergence]] — instantiates
[To be populated during integration]