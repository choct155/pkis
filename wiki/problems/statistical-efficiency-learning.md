---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
contrasts-with:
- data-hunger
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-22'
domain:
- machine-learning
- statistics
- sample-complexity
id: pkis:problem:statistical-efficiency-learning
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch01
- angelopoulos-ppi-plus-2023
tags:
- sample-complexity
- few-shot
- inductive-bias
- meta-learning
- data-scarce
title: Statistical Efficiency / Data Efficiency
understanding: 0
uses:
- vc-dimension
- bias-variance-tradeoff
- pac-learning
- inductive-bias
- cramer-rao-bound
---

## Definition
A learning algorithm $\mathcal{A}$ is *statistically efficient* if it achieves a given generalisation error $\epsilon$ using a sample size $n$ that is small relative to the hypothesis-class complexity, ideally matching the Cramér–Rao bound or information-theoretic minimax rate:
$$n^* = \mathcal{O}\!\left(\frac{d}{\epsilon^2}\right) \text{ or better,}$$
where $d$ is an effective dimensionality (e.g., VC dimension, effective number of parameters).

Data-efficient methods learn quickly from few examples by exploiting strong inductive biases — structural priors, compositionality, causal knowledge — rather than brute-force data scale.

### Why it matters
In data-scarce domains (medicine, robotics, rare events) large-scale scraping is infeasible. Data efficiency therefore separates model-based / Bayesian / causal approaches from pure deep learning in practical, safety-critical settings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cramer-rao-bound]] — uses
- [[data-hunger]] — contrasts-with
- [[inductive-bias]] — uses
- [[pac-learning]] — uses
- [[bias-variance-tradeoff]] — uses
- [[vc-dimension]] — uses
[To be populated during integration]