---
aliases: []
also_type: []
component_scores:
  alternatives: 4
  conditions: 4
  diagnostics: 4
  failure_modes: 4
  implementation: 3
  operational_mechanism: 5
  principled_mechanism: 4
contrasts-with:
- transformer-attention-mechanisms
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-07'
domain:
- bayesian-stats
- deep-learning
- statistical-learning
- optimization
extends:
- weight-initialization
- gaussian-process-regression
- belief-propagation
id: pkis:technique:mean-field-approximation
knowledge_type: technique
maturity: settled
related_concepts:
- '[[variational-inference]]'
- '[[elbo]]'
- '[[coordinate-ascent-vi]]'
score_date: '2026-06-07'
sources:
- '[[blei-vi-review]]'
- '[[ganguly-intro-vi]]'
- '[[sjolund-parametric-vi]]'
tags:
- variational-methods
- approximate-inference
- probability-theory
- statistical-physics
- independence-assumption
- tractability
title: Mean-Field Variational Approximation
understanding: 3
---

A variational inference approach that assumes the variational posterior fully factorizes over the latent variables: q(z) = ∏_j q_j(z_j), with each factor governed independently; this independence assumption makes ELBO optimization tractable via coordinate ascent but can systematically underestimate posterior variance.

## Connections
- [[transformer-attention-mechanisms]] — contrasts-with: Attention is architecturally designed to recover inter-token correlations that mean field discards; see bridge note
- [[belief-propagation]] — extends: Loopy belief propagation makes an implicit mean field approximation when applied to graphs with cycles
- [[gaussian-process-regression]] — extends: Infinite-width networks converge to GPs under the mean field argument that layer outputs are approximately independent Gaussians
- [[weight-initialization]] — extends: Mean field independence assumption at initialization is the theoretical basis for variance propagation analysis underlying Xavier and He initialization schemes

- [[variational-inference]] — specializes: mean-field is the classical and most studied sub-family of VI
- [[elbo]] — uses: mean-field CAVI iteratively maximizes the ELBO by optimizing each factor q_j in closed form
- [[coordinate-ascent-vi]] — uses: mean-field factorization enables coordinate ascent because each factor's optimal form is the unnormalized geometric mean of the complete conditional
- [[em-algorithm]] — commonly-confused-with: EM's E-step and mean-field CAVI have similar iterative structure, but EM uses exact conditional expectations while mean-field uses approximate factorized ones

## Reading Path

- [[blei-vi-review]] (unread) — authoritative treatment; Section 2.3–2.4; CAVI derivation for general exponential families; known limitation of variance underestimation
- [[ganguly-intro-vi]] (unread) — Section 4; introduces mean-field family; Section 5 works through CAVI on Gaussian mixture toy problem
- [[sjolund-parametric-vi]] (unread) — Section on modeling; contrasts mean-field (historical) with parametric/neural-network approach (modern); highlights mean-field's limited applicability

## Cross-Domain Principle
Mean field approximation is broader than variational inference — it is a general principle originating in statistical physics: replace each component's interaction with all others by its interaction with the *average field* produced by all others. This decouples components, converting an intractable joint problem into independent single-component problems.

**Statistical physics (origin):** In the Ising model, computing the partition function over all spin configurations is exponential. Mean field replaces each spin's interaction with its neighbors with its interaction with the average magnetization. Each spin is then determined by a single scalar rather than the full neighbor configuration.

**Variational inference:** The mean-field variational family assumes q(z) = ∏_j q_j(z_j). Each latent variable's distribution is optimized against the mean behavior of the others via the CAVI update — not against their full joint. This is the direct statistical analog of the physics assumption.

**Neural network initialization theory:** Each neuron's pre-activation is a sum of many weighted inputs. Under random initialization, CLT ensures this is approximately Gaussian. Across neurons, outputs are approximately independent because each is dominated by its own large sum — each neuron responds to the average statistical field of the inputs, not to specific cross-neuron correlations. This justifies: (a) the neural network–Gaussian process correspondence in the infinite-width limit, and (b) principled weight initialization schemes (Xavier, He) that control variance propagation through depth.

**Loopy belief propagation:** When [[belief-propagation]] runs on graphs with cycles, each node treats incoming messages as independent — ignoring correlations that cycles introduce. Mean field in structure if not in name.

**The trade in every instantiation:**
- *Gain:* Tractability — joint problem over interacting components becomes independent single-component problems, often solvable in closed form or by iteration.
- *Cost:* Correlation blindness — dependencies between components are discarded; variance is systematically underestimated. Critically, the independence assumption restricts the *search space*, not the search path — you are confined to a submanifold of factorized distributions before optimization begins.

## Open Questions
- At what width does the mean field approximation of neural network layers become practically accurate, and how does this interact with depth?
- Is there a unified formal account spanning statistical physics, VI, and neural network theory, or are these analogies rather than instances of a common mathematical structure? This question is substantively unresolved in the literature, not merely pedagogical.