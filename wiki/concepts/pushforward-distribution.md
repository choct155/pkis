---
aliases: []
also_type: []
analogous-to:
- reparameterization-trick
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
- probability-theory
- measure-theory
id: pkis:concept:pushforward-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- change-of-variables
- normalizing-flow
- reparameterization
title: Pushforward Distribution
understanding: 0
uses:
- change-of-variables-for-densities
---

## Definition
Given a measurable function $f : \mathcal{X} \to \mathcal{Y}$ and a distribution $p$ on $\mathcal{X}$, the **pushforward** $f_* p$ is the distribution on $\mathcal{Y}$ defined by $(f_* p)(B) = p(f^{-1}(B))$ for measurable $B \subseteq \mathcal{Y}$. When $f$ is a diffeomorphism and $p$ has density $p_u$, the pushforward density is
$$p_x(x) = p_u(f^{-1}(x))\,|\det J(f^{-1})(x)|.$$
Informally: probability mass is 'pushed' through $f$; the Jacobian corrects for local volume changes.

### Why it matters
The pushforward is the foundational concept underlying normalizing flows, importance sampling, and the reparameterization trick. It gives precise meaning to 'transforming a distribution'.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reparameterization-trick]] — analogous-to
- [[change-of-variables-for-densities]] — uses
[To be populated during integration]