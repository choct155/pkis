---
aliases: []
also_type: []
applies:
- multi-armed-bandit
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- upper-confidence-bound
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
id: pkis:technique:thompson-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- bayesian
- exploration
- posterior-sampling
- conjugate-prior
title: Thompson Sampling (Posterior Sampling)
understanding: 0
uses:
- conjugate-prior
- bayesian-inference
---

## Definition
$$A_t \sim \Pr\{a \text{ is optimal} \mid \text{data}_{1:t-1}\}$$

A Bayesian exploration method that maintains a posterior distribution over each action's value and selects an action with probability equal to its posterior probability of being the best — typically implemented by sampling one value per action from its posterior and acting greedily on the samples.

### Bayesian setup
The learner assumes a known prior over action values and updates it exactly after each reward (assuming stationarity). With *conjugate priors* the posterior update is closed-form and cheap. Sampling from the posteriors naturally injects more exploration into actions whose values remain uncertain and less into those already pinned down, automatically tapering exploration as evidence accumulates.

### Why it matters
Thompson sampling (a.k.a. posterior sampling) often matches the best distribution-free methods in this chapter while requiring no exploration parameter, and it has strong theoretical guarantees. It is the practical Bayesian counterpart to the optimal-but-intractable information-state / Gittins-index formulation, in which one would plan over the exploding tree of all possible reward sequences. It generalizes the optimism-under-uncertainty idea of UCB into a probability-matching rule that reuses the full machinery of Bayesian inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[upper-confidence-bound]] — contrasts-with: probability-matching Bayesian exploration vs. deterministic optimism bound
- [[bayesian-inference]] — uses: maintains and samples from a posterior over action values
- [[conjugate-prior]] — uses: closed-form posterior updates rely on conjugate priors
- [[multi-armed-bandit]] — applies: Bayesian posterior-sampling exploration for the bandit
[To be populated during integration]