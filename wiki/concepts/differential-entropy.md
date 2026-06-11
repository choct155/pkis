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
- information-theory
- probability-theory
id: pkis:concept:differential-entropy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch01
- murphy-pml1-intro-ch06
- murphy-pml2-advanced-ch05
tags:
- continuous-entropy
- Gaussian
- maximum-entropy
- information-theory
title: Differential Entropy
understanding: 0
---

## Definition
The differential entropy of a continuous random variable $x$ with density $p(x)$ is
$$H[x] = -\int p(x)\ln p(x)\,dx.$$
It arises as the limit of the discrete entropy after quantising $x$ into bins of width $\Delta$:
$$H_\Delta \approx -\int p(x)\ln p(x)\,dx - \ln\Delta,$$
so $H[x]$ and the discrete entropy differ by the divergent term $-\ln\Delta$.

### Why it matters
Unlike discrete entropy, differential entropy can be negative (e.g., a Gaussian with $\sigma^2<1/(2\pi e)$) and is not invariant under nonlinear reparameterisations. The maximum-entropy distribution under fixed mean $\mu$ and variance $\sigma^2$ is the Gaussian:
$$H_{\max} = \tfrac{1}{2}(1+\ln 2\pi\sigma^2) \text{ nats.}$$
This underpins the Gaussian maximum entropy characterisation and the rationale for Gaussian noise models in regression.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]