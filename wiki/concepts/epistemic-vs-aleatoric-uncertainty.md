---
aliases: []
also_type: []
analogous-to:
- bias-variance-tradeoff
- law-of-total-variance
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
- statistics
- decision-theory
id: pkis:concept:epistemic-vs-aleatoric-uncertainty
instantiates:
- probabilistic-ml-framework
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch01
- murphy-pml1-intro-ch02
specializes:
- uncertainty-quantification
tags:
- uncertainty-quantification
- bayesian
- reliability
title: Epistemic vs Aleatoric Uncertainty
understanding: 0
uses:
- bayesian-inference
- entropy
- information-theory
---

## Definition
Two orthogonal sources of uncertainty in predictive models:
- **Epistemic uncertainty** (model/knowledge uncertainty): reducible uncertainty arising from limited data or limited model expressiveness; formally, variance in $p(\theta|\mathcal{D})$.
- **Aleatoric uncertainty** (data/irreducible uncertainty): intrinsic stochasticity in the data-generating process $p(y|x,\theta^*)$ that cannot be eliminated by collecting more data.

$$\text{Var}[y|x] = \underbrace{\mathbb{E}_\theta[\text{Var}[y|x,\theta]]}_{{\text{aleatoric}}} + \underbrace{\text{Var}_\theta[\mathbb{E}[y|x,\theta]]}_{{\text{epistemic}}}$$

### Why it matters
Distinguishing the two types guides where to invest: more data reduces epistemic uncertainty; better models can capture aleatoric structure. In safety-critical applications (medical diagnosis, autonomous driving), quantifying both types is essential for reliable decision-making.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[information-theory]] — uses
- [[law-of-total-variance]] — analogous-to
- [[entropy]] — uses
- [[bias-variance-tradeoff]] — analogous-to
- [[probabilistic-ml-framework]] — instantiates
- [[bayesian-inference]] — uses
- [[uncertainty-quantification]] — specializes
[To be populated during integration]