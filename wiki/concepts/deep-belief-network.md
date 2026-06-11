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
- deep-learning
- probabilistic-graphical-models
- generative-models
id: pkis:concept:deep-belief-network
instantiates:
- directed-graphical-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- generative-model
- hybrid-directed-undirected
- layer-wise-pretraining
- historical
title: Deep Belief Network (DBN)
understanding: 0
uses:
- restricted-boltzmann-machine
- undirected-graphical-models
- greedy-layer-wise-pretraining
- elbo
---

## Definition
A deep belief network is a hybrid generative model with $l$ hidden layers defined by the joint distribution:
$$P\!\left(\mathbf{h}^{(l)},\mathbf{h}^{(l-1)}\right)\propto\exp\!\left(\mathbf{b}^{(l)\top}\mathbf{h}^{(l)}+\mathbf{b}^{(l-1)\top}\mathbf{h}^{(l-1)}+\mathbf{h}^{(l-1)\top}\mathbf{W}^{(l)}\mathbf{h}^{(l)}\right),$$
with directed downward connections for all layers below the top two and an undirected (RBM-like) connection between the top two layers. Intuitively, it stacks RBMs so that each layer learns increasingly abstract representations of the data.

### Why it matters
DBNs were among the first deep models to outperform kernel SVMs (on MNIST), igniting the modern deep-learning renaissance; they also showed that greedy layer-wise pre-training could overcome the difficulty of optimising deep architectures. Though largely superseded, they illustrate the tension between directed and undirected components and how approximate inference (explaining-away, intractable partition function) arises in hybrid models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[elbo]] — uses: Each greedy step approximately maximises a variational lower bound on log p(v).
- [[greedy-layer-wise-pretraining]] — uses
- [[undirected-graphical-models]] — uses: The top two layers of a DBN form an undirected (RBM) component.
- [[directed-graphical-models]] — instantiates: DBN uses directed connections between all layer pairs except the top two.
- [[restricted-boltzmann-machine]] — uses: DBN is built by stacking RBMs; parameters are copied directly from constituent RBMs.
[To be populated during integration]