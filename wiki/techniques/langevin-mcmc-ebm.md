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
- machine-learning
- statistics
- probabilistic-modeling
id: pkis:technique:langevin-mcmc-ebm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch24
tags:
- MCMC
- EBM-sampling
- Langevin-dynamics
- stochastic-gradient
title: Langevin MCMC for EBMs
understanding: 0
---

## Definition
$$x^{k+1} \leftarrow x^k - \frac{\epsilon^2}{2}\nabla_x E_\theta(x^k) + \epsilon\, z^k, \quad z^k \sim \mathcal{N}(0,I)$$

Langevin MCMC simulates a discretized overdamped Langevin diffusion to draw samples from $p_\theta(x) \propto e^{-E_\theta(x)}$. Initialising from a simple prior and iterating drives $x^k$ toward high-probability (low-energy) regions while injecting Gaussian noise for exploration. In the limit $\epsilon\to 0$, $K\to\infty$ the chain converges to $p_\theta$ under regularity conditions.

### Why it matters
Langevin MCMC exploits the Stein score $-\nabla_x E_\theta$, which is tractable for EBMs, to draw approximate samples without knowing $Z_\theta$. It underpins MCMC-based MLE training of EBMs and is the sampler of choice for contrastive divergence with gradient-based dynamics. A Metropolis–Hastings correction yields the Metropolis-adjusted Langevin algorithm (MALA), removing discretisation bias.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]