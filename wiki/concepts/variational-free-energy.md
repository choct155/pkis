---
aliases: []
also_type: []
analogous-to:
- elbo
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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
generalizes:
- mean-field-approximation
id: pkis:concept:variational-free-energy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- variational-inference
related_concepts: []
sources:
- mackay-itila-ch33
tags:
- variational-methods
- statistical-physics
- free-energy
- mean-field
- bound
- feynman-bogoliubov
title: Variational Free Energy
understanding: 0
uses:
- kl-divergence
---

## Definition
The **variational free energy** is the objective minimized when a tractable distribution $Q(x;\theta)$ is fitted to an intractable Gibbs distribution $P(x\mid\beta,\mathbf{J}) = \tfrac{1}{Z}\exp[-\beta E(x;\mathbf{J})]$:

$$\beta\tilde{F}(\theta) = \sum_x Q(x;\theta)\,\ln\frac{Q(x;\theta)}{\exp[-\beta E(x;\mathbf{J})]}.$$

It admits two illuminating rewritings. As a thermodynamic decomposition,

$$\beta\tilde{F}(\theta) = \beta\langle E\rangle_Q - S_Q,$$

the mean energy under $Q$ minus the entropy of $Q$ (energy traded against disorder). As a divergence,

$$\beta\tilde{F}(\theta) = D_{KL}(Q\,\|\,P) + \beta F,\qquad \beta F \equiv -\ln Z.$$

### Why it matters
Because $D_{KL}(Q\|P)\ge 0$ (Gibbs' inequality), $\tilde{F}(\theta)\ge F$ for **every** $Q$, with equality iff $Q=P$. Minimizing $\tilde{F}$ therefore (i) drives $Q$ toward $P$ and (ii) yields a rigorous bound $\tilde{Z}\equiv e^{-\beta\tilde{F}}\le Z$ — a tractable lower bound on the otherwise-intractable partition function. This is the Feynman--Bogoliubov bound and the physics-language ancestor of the ELBO.

### Tractability
Though $\tilde{F}$ is itself a sum over all $x$, it becomes computable when $Q$ is simple. For a separable $Q(x;\mathbf{a})\propto\exp(\sum_n a_n x_n)$, both $S_Q=\sum_n H_2^{(e)}(q_n)$ and $\langle E\rangle_Q$ factorize into per-spin terms, making minimization cheap.

### Generalization
Richer families $Q$ (capturing correlations) tighten the bound but cost more to evaluate — a direct expression of the expressiveness--tractability tradeoff. The framework subsumes mean-field theory, ensemble learning for posteriors, and (via Bethe/Kikuchi free energies) loopy belief propagation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variational-inference]] — prerequisite-of: Casting inference as minimizing a free-energy bound is the foundation of variational inference.
- [[elbo]] — analogous-to: The negative variational free energy is the physics-language form of the ELBO; both lower-bound the (log-)evidence/partition function.
- [[kl-divergence]] — uses: betaF-tilde = D_KL(Q||P) + betaF; the bound follows from Gibbs' inequality on the KL term.
- [[mean-field-approximation]] — generalizes: Mean-field theory is variational free-energy minimization with a separable trial distribution.
[To be populated during integration]