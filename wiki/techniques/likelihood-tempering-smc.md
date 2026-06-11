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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:technique:likelihood-tempering-smc
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- smc-sampler
- annealing
- bayesian-inference
- tempering
- adaptive
title: Likelihood Tempering / Geometric Path SMC
understanding: 0
---

## Definition
$$\tilde{\gamma}_t(z) = \tilde{\gamma}_0(z)^{1-\lambda_t}\,\tilde{\gamma}(z)^{\lambda_t}, \quad 0 = \lambda_0 < \cdots < \lambda_T = 1$$

Likelihood tempering constructs bridging distributions by raising the target to a power $\lambda_t$ ("inverse temperature"), interpolating from an easy-to-sample initial distribution $\pi_0$ to the final target $\pi$. In Bayesian inference $\tilde{\gamma}_t(\theta) = \pi_0(\theta)\,p(D|\theta)^{\lambda_t}$, so the incremental weight is $\alpha_t = \exp[-\delta_t E(\theta)]$ where $E = -\log p(D,\theta)$.

**Adaptive tempering**: set $\lambda_t$ by finding $\delta_t$ such that the ESS of the reweighted particles equals a target $\mathrm{ESS}_{\min}$ (e.g., $0.5N$).

### Why it matters
Likelihood tempering is the workhorse schedule for SMC samplers in Bayesian statistics. It enables sampling from multimodal posteriors where MCMC chains mix poorly, and is the foundation of the connection between SMC samplers and annealed importance sampling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]