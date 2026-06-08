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
- bayesian-stats
id: pkis:concept:likelihood-equivalence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch35
tags:
- likelihood-equivalence
- causal-direction
- graphical-models
- markov-equivalence
- causal-discovery
- prior-design
title: Likelihood Equivalence
understanding: 0
---

## Definition
Two directed graphical models are **likelihood-equivalent** if, for any setting of the parameters of one, there exists a setting of the parameters of the other that makes the joint distribution over all observables identical. The minimal example is the pair $A \to B$ and $B \to A$: a joint $P(a,b)$ can always be factored either as $P(a)P(b\mid a)$ or $P(b)P(a\mid b)$, so observational data alone cannot distinguish them via the likelihood.

### Bayes can still break the tie
Likelihood equivalence stops *sampling-theory* methods (which use only the likelihood) from inferring arrow direction. It does **not** bind a Bayesian: the two models live over different parameter spaces, and there is no requirement that the priors assign matching densities. With honestly chosen priors the marginal likelihoods $P(\text{Data}\mid H_{A\to B})$ and $P(\text{Data}\mid H_{B\to A})$ differ, yielding a non-trivial posterior over direction. MacKay's binary toy example, with Beta$(1,1)$ priors on each (conditional) probability, gives a posterior odds of roughly $3.8{:}1$ in favour of $A\to B$ — because the probabilities inferred under that direction sit more typically within the prior.

### Why it matters
A widespread orthodoxy deliberately restricts priors to those for which *prior equivalence* also holds (specially-constructed Dirichlet priors), discarding the Bayesian ability to read causal direction from observational data. MacKay argues this is a philosophical error: priors should encode genuine assumptions, not be rigged to enforce indistinguishability. The concept frames the limits of causal discovery — it is the parametric cousin of Markov-equivalence classes of DAGs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]