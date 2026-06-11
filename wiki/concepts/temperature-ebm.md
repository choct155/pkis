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
- statistical-physics
- probabilistic-inference
id: pkis:concept:temperature-ebm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
tags:
- energy-based-models
- temperature
- boltzmann
- tempering
- statistical-physics
title: Temperature in Energy-Based Models
understanding: 0
uses:
- boltzmann-machine
- partition-function
---

## Definition
The **temperature** $T = 1/\beta$ of an energy-based model parametrises the sharpness of its probability distribution:
$$p_\beta(\mathbf{x}) \propto \exp\!\left(-\beta E(\mathbf{x})\right)$$

- $\beta \to \infty$ ($T \to 0$): distribution concentrates deterministically on the lowest-energy state.
- $\beta = 1$ ($T = 1$): the model's trained distribution.
- $\beta \to 0$ ($T \to \infty$): distribution becomes uniform over states.

### Why it matters
Temperature is the key control parameter for tempering-based MCMC techniques. Raising the temperature flattens the landscape, enabling the chain to traverse energy barriers; lowering it sharpens the distribution for sampling. The concept connects deep learning to statistical physics (Boltzmann distribution) and underpins simulated annealing, parallel tempering, and diffusion-based generative models.

### Critical temperatures
Phase-transition-like behaviour can occur at critical temperatures where the tempering schedule must be slowed, limiting the practical effectiveness of tempering algorithms.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partition-function]] — uses: normalisation constant Z(beta) depends on temperature
- [[boltzmann-machine]] — uses: beta parameter originates from Boltzmann distribution in statistical physics
[To be populated during integration]