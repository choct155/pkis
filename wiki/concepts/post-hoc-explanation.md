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
generalizes:
- lime-local-surrogate
- saliency-map
- shapley-feature-importance
- counterfactual-explanation
id: pkis:concept:post-hoc-explanation
instantiates:
- interpretable-ml-ecosystem
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
tags:
- interpretability
- saliency
- LIME
- SHAP
- attribution
- feature-importance
title: Post-Hoc Explanation
understanding: 0
uses:
- distribution-shift
---

## Definition
A **post-hoc explanation** is an artifact $E = g(f, x, \mathcal{D})$ produced after a model $f$ has been trained, where $g$ extracts a (necessarily partial) view of $f$'s behavior without modifying $f$ itself.

Because $E$ is an approximation, there is always a **fidelity gap**: $E$ may be faithful only locally, only for certain inputs, or only with respect to certain aspects of the model (e.g., first-order sensitivity but not interactions).

### Why it matters
Post-hoc methods are the primary interpretability tool when (a) the deployed model is a black box (e.g., a large neural network), (b) the model cannot be retrained, or (c) one needs to explain a system of interconnected models. Families include: saliency/attribution maps (gradient-based, perturbation-based), local surrogate models (LIME), global mimic/distillation models, example-based methods (influential training points, counterfactuals), and Shapley/Banzhaf feature-importance scores.

### Key limitation
Post-hoc explanations can be adversarially manipulated: two perceptually indistinguishable inputs with the same predicted label can receive very different explanations, and joint training can produce models whose explanations pass partial-view tests while the underlying model violates the intended constraint.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[distribution-shift]] — uses: Post-hoc explanations must account for whether explanation neighborhoods remain in-distribution.
- [[counterfactual-explanation]] — generalizes
- [[shapley-feature-importance]] — generalizes
- [[saliency-map]] — generalizes
- [[lime-local-surrogate]] — generalizes
- [[interpretable-ml-ecosystem]] — instantiates
[To be populated during integration]