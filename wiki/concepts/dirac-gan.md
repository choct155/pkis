---
aliases: []
also_type: []
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
- optimization
- game-theory
id: pkis:concept:dirac-gan
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- GAN
- convergence
- gradient-descent
- stability-analysis
- Nash-equilibrium
title: DiracGAN
understanding: 0
---

## Definition
DiracGAN is a minimal GAN example used to study convergence failure. The data distribution is a Dirac delta at zero; the generator is $G_\theta(z)=\theta$ (a Dirac at $\theta$); the discriminator is $D_\phi(x)=\phi x$ (linear). The Jacobian of the game at the equilibrium $\theta=\phi=0$ is:
$$J=\begin{pmatrix}0 & l'(0)\\-l'(0) & 0\end{pmatrix}$$
with purely imaginary eigenvalues $\pm i l'(0)$. The conserved quantity $\theta^2+\phi^2$ shows that alternating gradient descent orbits the equilibrium indefinitely rather than converging.

### Why it matters
DiracGAN provides the simplest analytic proof that gradient descent does not converge in GANs, motivating regularisation, higher-order optimisers (e.g., RungeKutta4), and consensus-based methods that modify the game dynamics to ensure local convergence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]