---
aliases: []
also_type: []
applies:
- amortized-vi
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
- machine-learning
- bayesian-inference
id: pkis:concept:amortization-gap
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
tags:
- amortization-gap
- VAE
- inference-network
- semi-amortized-VI
title: Amortization Gap
understanding: 0
uses:
- elbo
---

## Definition
The **amortization gap** is the difference between the ELBO achieved by per-example optimal variational parameters $\psi_n^*$ and the ELBO achieved by an inference network $f^{\mathrm{inf}}_\phi$:
$$\Delta_n = \mathcal{L}(\theta,\psi_n^*|x_n) - \mathcal{L}(\theta,f^{\mathrm{inf}}_\phi(x_n)|x_n) \geq 0$$

It quantifies the suboptimality introduced when a single shared network must serve as a universal approximator of the per-instance posterior map.

### Why it matters
The amortization gap motivates **semi-amortized VI** (Kim et al., 2018): use the inference network to warm-start a local optimizer for $\psi_n$, combining the global efficiency of amortization with per-example accuracy. It is distinct from the approximation gap (error due to restricted variational family) and the inference gap (their sum).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[elbo]] — uses: The gap is measured in ELBO units: difference between per-example optimal ELBO and amortized ELBO.
- [[amortized-vi]] — applies
[To be populated during integration]