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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
id: pkis:technique:abduction-action-prediction
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch07
tags:
- counterfactuals
- structural-causal-models
- do-operator
- bayesian-networks
- causality
title: Abduction–Action–Prediction
understanding: 0
---

## Definition
The three-step procedure (Pearl, Theorem 7.1.7) for evaluating the probability of a counterfactual "had $A$ been the case, then $B$" given evidence $e$, in a probabilistic causal model $\langle M, P(u)\rangle$:

$$P(B_A \mid e) = \sum_u P(B_A(u)) \, P(u \mid e).$$

*Intuition:* route the evidence through the invariant background variables $U$, surgically rewrite history under the antecedent, then predict forward.

### The three steps
1. **Abduction** — update the prior over background variables: $P(u) \to P(u \mid e)$. The evidence $e$ is absorbed into beliefs about the unobserved context $U$, which carries all information from the actual world.
2. **Action** — form the submodel $M_A$ by the intervention $do(A)$, replacing the equations for the antecedent variables with the forced values (severing their incoming arrows).
3. **Prediction** — compute $P(B)$ in the modified model $M_A$ under the updated distribution $P(u \mid e)$.

### Why it matters
The procedure operationalizes Level-3 (counterfactual) queries on the Ladder of Causation. It explains why counterfactuals demand more than the do-operator alone: the abduction step conditions on evidence that is itself affected by the antecedent, distinguishing genuine counterfactuals from plain interventions. The same three steps work deterministically (where abduction pins down $U$), in linear-Gaussian models, and in causal Bayesian networks with intrinsic nondeterminism—where action becomes arrow-deletion plus instantiation.

### Worked deterministic instance
In the firing-squad example, evaluating "the prisoner would be dead even had rifleman A not shot" given the prisoner is dead: abduction infers the court ordered the execution ($U$); action sets $\neg A$; prediction shows B still shoots, so $D$ holds.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]