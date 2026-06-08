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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- information-theory
id: pkis:concept:partition-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch31
tags:
- partition-function
- boltzmann-distribution
- statistical-physics
- free-energy
- normalizing-constant
- fluctuation-dissipation
title: Partition Function
understanding: 0
---

## Definition
The **partition function** is the normalizing constant of a Boltzmann distribution over states $x$ with energy $E(x)$ at inverse temperature $\beta = 1/k_B T$:

$$Z(\beta) = \sum_x \exp[-\beta E(x)], \qquad P(x \mid \beta) = \frac{1}{Z(\beta)} e^{-\beta E(x)}.$$

Far from a mere normalizer, $Z$ is a generating function: every thermodynamic quantity follows from its derivatives.

### Generating function for energy moments
Differentiating $\ln Z$ with respect to $\beta$ recovers the mean and variance of the energy:

$$\frac{\partial \ln Z}{\partial \beta} = -\bar{E}, \qquad \frac{\partial^2 \ln Z}{\partial \beta^2} = \langle E^2 \rangle - \bar{E}^2 = \operatorname{var}(E).$$

The free energy is $F = -k_B T \ln Z$, and the entropy is $S = \ln Z + \beta \bar{E} = -\partial F / \partial T$.

### Why it matters
Because $Z$ encodes the full distribution, observables that would seem to require separate experiments are linked through it. The heat capacity, for example, equals an energy fluctuation: $C = \operatorname{var}(E)/k_B T^2 = k_B \beta^2 \operatorname{var}(E)$ — a fluctuation–dissipation relation that lets Monte Carlo estimates of $\operatorname{var}(E)$ stand in for direct heating experiments. Computing $Z$ exactly is generally intractable (the sum has $2^N$ terms), which motivates both sampling methods and exact tricks like the transfer matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]