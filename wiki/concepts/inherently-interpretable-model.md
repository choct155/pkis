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
contrasts-with:
- post-hoc-explanation
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- interpretability
- human-computer-interaction
generalizes:
- decision-trees
- generalized-additive-model
- lasso
id: pkis:concept:inherently-interpretable-model
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
- transparency
- sparse-models
- decision-trees
- rule-sets
title: Inherently Interpretable Model
understanding: 0
uses:
- regularization
---

## Definition
A model $f: \mathcal{X} \to \mathcal{Y}$ is **inherently interpretable** if a domain user can inspect the complete mapping from inputs to outputs—without additional proxies or post-processing—and understand how any input produces its output within the constraints of the task (time, cognition, attention).

Formally, the explanation $E = f$ itself; no surrogate $\hat{f} \approx f$ is required. Canonical examples include sparse linear models, small decision trees, decision lists, rule sets, generalized additive models, and small HMMs.

The key insight is that interpretability is task-relative: a 50-node decision tree may be inherently interpretable for an offline analyst but not for a clinician making a bedside decision in two minutes.

### Why it matters
Inherently interpretable models eliminate the fidelity gap introduced by post-hoc explanations—there is no surrogate to be unfaithful. They have been strongly advocated for high-stakes deployment (credit, medicine, criminal justice) precisely because no approximation stands between the model and the human inspector. With modern optimization (integer programming, distillation-then-discard), they often match black-box accuracy while being verifiable.

### Subtypes
- **Sparse/compact feature-based**: lasso regression, super-sparse linear integer models, generalized additive models.
- **Logic-based**: decision trees, decision lists, decision sets, rule sets, logic programs.
- **Example-based**: $k$-nearest neighbors, prototype/exemplar methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — uses: L1 and other sparsity-inducing regularizers are key to training sparse inherently interpretable models.
- [[interpretable-ml-ecosystem]] — instantiates: When model = explanation, the ecosystem collapses the method/explanation distinction.
- [[lasso]] — generalizes: Sparse linear models (lasso) are a canonical compact inherently interpretable class.
- [[generalized-additive-model]] — generalizes: GAMs with small numbers of smooth component functions are inherently interpretable.
- [[decision-trees]] — generalizes: Decision trees are a canonical example of an inherently interpretable model class.
- [[post-hoc-explanation]] — contrasts-with: Inherently interpretable models need no surrogate; post-hoc methods approximate an already-trained model.
[To be populated during integration]