---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- bayesian-inference
- probabilistic-graphical-models
id: pkis:framework:bayesian-inference-patterns
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
specializes:
- bayesian-inference
tags:
- latent-variables
- global-latents
- local-latents
- bayesian-computation
- inference
title: Bayesian Inference Patterns (Global / Local / Mixed Latents)
understanding: 0
uses:
- latent-variable-models
- em-algorithm
- variational-inference
- amortized-inference
- probabilistic-graphical-models
- stochastic-vi
---

## Definition
$$p(x_{1:N}, z_{1:N}, \theta) = p(\theta_x)p(\theta_z)\prod_{n=1}^{N} p(x_n|z_n,\theta_x)p(z_n|\theta_z)$$

Three canonical structural patterns classify how latent variables appear in a probabilistic model: (1) **global latents** — parameters θ shared across all N observations; (2) **local latents** — per-datapoint hidden states $z_n$ with known θ; (3) **global and local latents** — fully Bayesian treatment of both θ and $z_{1:N}$. Each pattern motivates a distinct family of inference algorithms.

### Why it matters
Recognising which pattern a model belongs to determines the most efficient inference strategy: conjugate/exact updates for globals, EM or parallel VI for locals, and stochastic/amortised VI or full MCMC for the mixed case. The taxonomy also explains *why* uncertainty in global parameters is often negligible (θ is informed by all N points) while local uncertainty is high (each $z_n$ sees only one datapoint).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stochastic-vi]] — uses
- [[probabilistic-graphical-models]] — uses
- [[amortized-inference]] — uses
- [[variational-inference]] — uses
- [[em-algorithm]] — uses: EM exploits the local-latents pattern
- [[latent-variable-models]] — uses
- [[bayesian-inference]] — specializes
[To be populated during integration]