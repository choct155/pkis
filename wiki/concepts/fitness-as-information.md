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
- information-theory
- statistical-learning
id: pkis:concept:fitness-as-information
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch19
tags:
- evolution
- natural-selection
- additive-fitness
- genome
- information-acquisition
title: Fitness as Information Acquired by Natural Selection
understanding: 0
uses:
- shannon-information-content
---

## Definition
MacKay models a haploid genome as a vector $\mathbf{x}$ of $G$ bits, each in a good state ($x_g=1$) or bad state ($x_g=0$), with an **additive fitness function**
$$F(\mathbf{x}) = \sum_{g=1}^{G} x_g, \qquad f(\mathbf{x}) \equiv F(\mathbf{x})/G.$$
Fitness is thus, locally, a roughly linear function of the genome: many small independent changes each nudge fitness slightly, and they combine approximately additively.

The key conceptual move is to read **rising fitness as information being acquired by the species**. If bits are random, $F \approx G/2$; if the population reaches $F=G$, then $G$ bits have been learned — for each locus, selection has discovered which of the two states is better. Defining $\log_2(1/f_g)$ as the information needed to find a good allele present in fraction $f_g$ of the population, the information acquired at intermediate fitness is
$$I = \sum_g \log_2\frac{f_g}{1/2} \approx 2\,(F - G/2)\ \text{bits}.$$
So information is gained at roughly **twice the rate of fitness increase**.

### Why it matters
This reframing turns evolution into a learning/communication problem: natural selection is a noisy teacher transmitting a few bits per individual (who survives), and the genome is the receiver. It makes "how fast can a species learn?" a precise, quantitative question — answered differently for asexual vs sexual reproduction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[shannon-information-content]] — uses: Information acquired per locus is defined as log_2(1/f_g), the Shannon information content of finding a good allele at frequency f_g.
[To be populated during integration]