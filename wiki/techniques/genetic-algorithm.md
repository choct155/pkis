---
aliases: []
also_type: []
analogous-to:
- simulated-annealing
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- search-and-planning
extends:
- local-beam-search
id: pkis:technique:genetic-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch04
tags:
- genetic-algorithm
- evolutionary-computation
- crossover
- mutation
- selection
- schema-theorem
- genetic-programming
title: Genetic Algorithm
understanding: 0
---

## Definition
An evolutionary algorithm that can be viewed as a variant of stochastic beam search explicitly motivated by natural selection: a population of individuals (states) evolves so that the fittest produce offspring (successor states) that populate the next generation. In genetic algorithms each individual is a string over a finite alphabet (often Boolean), analogous to DNA over ACGT; in evolution strategies an individual is a sequence of real numbers, and in genetic programming an individual is a computer program represented as a syntax tree. The algorithm is parameterized by population size, individual representation, mixing number ρ (number of parents per offspring; ρ=2 is most common, ρ=1 reduces to asexual stochastic beam search), a selection process (e.g. probability proportional to fitness, or tournament selection of the ρ fittest of n random individuals), a recombination/crossover procedure (split parent strings at a crossover point and recombine), a mutation rate (each component flipped with that probability), and the makeup of the next generation (possibly with elitism, retaining top parents so fitness never decreases, or culling below a threshold). For 8-queens, individuals are 8-digit strings (row per column) scored by the number of nonattacking pairs (28 for a solution). Crossover is advantageous only when meaningful contiguous blocks (useful sub-solutions) exist: schema theory shows that a schema—a partially specified substring—whose instances have above-average fitness grows in frequency over generations, but if positions are randomly permuted, crossover conveys no advantage. Thus successful use requires careful representation engineering so that schemas correspond to meaningful solution components. GAs are typically slower to converge than stochastic hill climbing, but have found practical use in circuit/antenna design, job-shop scheduling, and neural-architecture search; the Baldwin effect (lifetime learning relaxing the fitness landscape) shows learning can accelerate evolution even without Lamarckian inheritance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[simulated-annealing]] — analogous-to: Both take large stochastic steps early and smaller steps as the search 'cools'/population converges.
- [[local-beam-search]] — extends: GAs are stochastic beam search plus recombination/crossover of multiple parents.
[To be populated during integration]