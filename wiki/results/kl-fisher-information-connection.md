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
- optimization
id: pkis:result:kl-fisher-information-connection
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- natural-gradient
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
tags:
- kl-divergence
- fisher-information
- natural-gradient
- mahalanobis
- information-geometry
title: KL Divergence–Fisher Information Connection
understanding: 0
uses:
- kl-divergence
- fisher-information
- cramer-rao-bound
---

## Definition
For a parametric family $p_\theta(x)$ and a nearby distribution $p_{\theta+\delta}(x)$, a second-order Taylor expansion yields:

$$D_{\mathrm{KL}}(p_\theta \| p_{\theta+\delta}) \approx \frac{1}{2}\,\delta^T \mathbf{F}(\theta)\,\delta$$

where $\mathbf{F}(\theta) = -\mathbb{E}[\nabla^2 \log p_\theta(x)] = \mathbb{E}[(\nabla \log p_\theta)(\nabla \log p_\theta)^T]$ is the **Fisher Information Matrix** (FIM). The first-order term vanishes because the expected score is zero.

Thus, locally, KL divergence is a squared Mahalanobis distance in the metric induced by the FIM.

### Why it matters
This connection motivates the **natural gradient** method, which preconditions gradient descent by the inverse FIM to obtain updates that are invariant to reparameterization of the parameter space. It also underlies the geometric view of statistical manifolds (information geometry) and justifies using KL as a proximity measure in trust-region optimization methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cramer-rao-bound]] — uses
- [[natural-gradient]] — prerequisite-of
- [[fisher-information]] — uses
- [[kl-divergence]] — uses
[To be populated during integration]