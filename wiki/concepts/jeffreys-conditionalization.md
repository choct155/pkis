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
- statistics
- probability-theory
- epistemology
generalizes:
- bayesian-inference
id: pkis:concept:jeffreys-conditionalization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
tags:
- bayesian-inference
- conditionalization
- soft-evidence
- kl-divergence
- belief-updating
title: Jeffrey's Conditionalization Rule
understanding: 0
uses:
- kl-divergence
- kl-divergence-uniqueness
---

## Definition
**Jeffrey's conditionalization** generalizes Bayesian updating to cases where new evidence does not pin down the data exactly, but rather updates the marginal distribution over observations to some specified $p(D)$.

Given prior $q(\theta)$ and likelihood $q(D|\theta)$, after updating to a new marginal $p(D)$, the updated belief over parameters is:

$$p(\theta) = \int dD\, p(D)\, q(\theta|D)$$

This arises from minimizing $D_{\mathrm{KL}}(p(\theta,D) \| q(\theta,D))$ subject to the marginal constraint $p(D)$. When $p(D) = \delta(D - D_0)$, this reduces to standard Bayesian conditioning. The conditional $p(\theta|D) = q(\theta|D)$ is unchanged; only the marginal $p(\theta)$ changes.

### Why it matters
Jeffrey's conditionalization handles soft evidence (uncertain observations) within a principled KL-minimization framework. It shows that Bayesian inference is not merely a chain-rule identity but a constrained KL minimization, naturally extending to noisy or uncertain measurements.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kl-divergence-uniqueness]] — uses
- [[kl-divergence]] — uses
- [[bayesian-inference]] — generalizes
[To be populated during integration]