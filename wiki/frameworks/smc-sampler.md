---
aliases: []
also_type: []
applies:
- marginal-likelihood
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- mcmc
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
generalizes:
- annealed-importance-sampling
id: pkis:framework:smc-sampler
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
specializes:
- sequential-monte-carlo
tags:
- smc
- tempering
- annealing
- bayesian-inference
- normalizing-constant
title: SMC Sampler
understanding: 0
uses:
- likelihood-tempering-smc
- data-tempering-ibis
---

## Definition
An SMC sampler targets a static distribution $\pi(z) = \tilde{\gamma}(z)/Z$ by constructing a sequence of bridging distributions $\{\pi_t(z_t)\}_{t=0}^T$, expanding them to a joint path distribution via backwards kernels:
$$\tilde{\pi}_t(z_{1:t}) = \pi_t(z_t)\prod_{s=1}^{t-1} L_s(z_s|z_{s+1})$$

and then running the generic particle filter (Algorithm 13.3) on this extended space. Key ingredients:
- **Forward kernel** $M_t(z_t|z_{t-1})$: an MCMC kernel leaving $\pi_t$ invariant.
- **Backward kernel** $L_{t-1}(z_{t-1}|z_t)$: time-reversal of $M_t$; when detailed balance holds, the incremental weight simplifies to $\alpha_t = \tilde{\gamma}_t(z_{t-1})/\tilde{\gamma}_{t-1}(z_{t-1})$.

### Why it matters
SMC samplers are a principled alternative to MCMC for multimodal targets: they produce an unbiased estimate of the normalizing constant $Z$, are parallelisable, and support adaptive tuning of kernels. Annealed importance sampling is a special case with no resampling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[marginal-likelihood]] — applies
- [[annealed-importance-sampling]] — generalizes: AIS is SMC sampler without resampling
- [[data-tempering-ibis]] — uses
- [[likelihood-tempering-smc]] — uses
- [[mcmc]] — contrasts-with
- [[sequential-monte-carlo]] — specializes
[To be populated during integration]