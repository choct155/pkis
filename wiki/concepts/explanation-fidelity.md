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
- interpretability
id: pkis:concept:explanation-fidelity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
tags:
- interpretability
- faithfulness
- fidelity
- sanity-check
- surrogate
title: Explanation Fidelity (Faithfulness)
understanding: 0
---

## Definition
**Explanation fidelity** (also called *faithfulness*) measures how accurately an explanation $E$ reflects the behavior of the model $f$ it purports to explain.

Formally, for a local explanation at input $x_0$, one common operationalization is:
$$\text{Fidelity} = \mathbb{E}_{x \sim \mathcal{N}(x_0)}\bigl[\mathbf{1}[\text{sign}(f(x)-f(x_0)) = \text{sign}(E(x)-E(x_0))]\bigr]$$
or more generally any divergence $d(f, E)$ restricted to a neighborhood of $x_0$.

For a global mimic model, fidelity is typically measured as the agreement rate: $\Pr_{x \sim p_\text{data}}[f(x) = E(x)]$.

### Why it matters
A low-fidelity explanation can mislead users into trusting a model that behaves differently than the explanation suggests, or distrust a model that actually behaves well. Fidelity is a prerequisite for actionability and recourse: if flipping an apparently important feature does not actually change the prediction, the recourse advice is useless. Sanity-check protocols (e.g., comparing explanations of trained vs. randomly-initialized models) are standard empirical tests for fidelity failures.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]