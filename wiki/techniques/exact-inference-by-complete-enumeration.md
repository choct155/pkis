---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:technique:exact-inference-by-complete-enumeration
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch21
tags:
- bayesian-inference
- exact-inference
- brute-force
- posterior
title: Exact Inference by Complete Enumeration
understanding: 0
---

## Definition
Complete enumeration is the most direct exact-inference method: list every hypothesis $h$ in the hypothesis space, evaluate the unnormalized posterior $P(h)\,P(\mathcal{D}\mid h)$ for each, and normalize by their sum,

$$P(h\mid\mathcal{D}) = \frac{P(h)\,P(\mathcal{D}\mid h)}{\sum_{h'} P(h')\,P(\mathcal{D}\mid h')}.$$

Any downstream query (a marginal, a MAP estimate, the evidence) is then read off by summing the appropriate entries. For continuous parameters $\theta$ the space is discretized onto a grid, and integrals such as the marginal likelihood become finite sums, $P(\mathcal{D}\mid\mathcal{H}) = \sum_{\theta} P(\theta)\,P(\mathcal{D}\mid\theta,\mathcal{H})$.

### How it works
MacKay's burglar-alarm example enumerates the four joint hypotheses over $(b,e)$, computes each numerator term, normalizes by their sum $P(a{=}1)$, and marginalizes over the earthquake to answer 'was there a burglar?'. The Gaussian-fitting example places a $10\times10$ grid over $(\mu,\sigma)$ and scores each cell's likelihood.

### Why it matters
Enumeration is the conceptual baseline against which all approximate inference (MCMC, variational methods) is measured: it returns the exact posterior with no sampling error or family-mismatch bias. It clarifies what those approximations are approximating. Its fatal limitation is cost — a grid resolving $K$ parameters needs $\gtrsim 10^K$ points — so it is feasible only for small discrete spaces or one- to two-dimensional grids, which is precisely the gap that motivates the rest of Bayesian computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]