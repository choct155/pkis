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
- statistics
- information-theory
- information-geometry
extends:
- score-function
id: pkis:result:fim-exponential-family
instantiates:
- fisher-information
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
tags:
- Fisher-information
- exponential-family
- sufficient-statistics
- natural-parameters
- information-geometry
title: 'FIM for Exponential Family: FIM equals Covariance of Sufficient Statistics'
understanding: 0
uses:
- exponential-family
- sufficient-statistics
- jeffreys-prior
- natural-gradient
---

## Definition
For an exponential family distribution with natural parameters $\eta$ and sufficient statistics $T(x)$:
$$\log p(x|\eta)=\eta^\top T(x)-A(\eta)+h(x)$$
the Fisher information matrix with respect to $\eta$ equals the covariance of the sufficient statistics:
$$F_\eta = \operatorname{Cov}_{p(x|\eta)}[T(x)]$$
With respect to the moment parameters $m=\mathbb{E}[T(x)]=\nabla A(\eta)$:
$$F_m = F_\eta^{-1} = \operatorname{Cov}[T(x)]^{-1}$$
and $\partial\eta/\partial m = F_\eta^{-1}$, so the two FIMs are matrix inverses of each other.

### Why it matters
This result unifies the FIM across all exponential family models (Gaussian, Bernoulli, Poisson, etc.) and connects information geometry (dual coordinate systems $\eta$ and $m$) to the covariance structure of sufficient statistics. It simplifies derivation of Jeffreys priors and natural gradient updates for exponential family models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[natural-gradient]] — uses
- [[jeffreys-prior]] — uses
- [[fisher-information]] — instantiates
- [[sufficient-statistics]] — uses
- [[exponential-family]] — uses
- [[score-function]] — extends
[To be populated during integration]