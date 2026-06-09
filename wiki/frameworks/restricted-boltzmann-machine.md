---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- multilayer-perceptron
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
- statistical-learning
id: pkis:framework:restricted-boltzmann-machine
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch17
specializes:
- boltzmann-machine
- undirected-graphical-models
tags:
- boltzmann-machine
- hidden-units
- bipartite-graph
- feature-learning
- generative-model
- gibbs-sampling
title: Restricted Boltzmann Machine
understanding: 0
uses:
- gibbs-sampler
---

## Definition
A restricted Boltzmann machine (RBM) is a Boltzmann machine whose graph is bipartite: one layer of visible units and one layer of hidden units, with NO connections within a layer (only visible-hidden edges). This restriction -- written schematically V1 <-> H <-> V2 when the visible layer is split into inputs V1 and outputs V2 -- is what makes the model practical: conditional on the units in the other layer, the units within a layer are mutually independent, so an entire layer can be Gibbs-sampled in one block via the logistic conditionals Pr(X_j=1 | rest). This collapses the expensive expectation computations that hamper a general (fully connected) Boltzmann machine.

Like any Boltzmann machine, an RBM is an undirected, energy-based generative model trained to maximize the log-likelihood of the joint distribution over all visible units (features AND targets), in contrast to a single-hidden-layer neural network, which has directed edges, real-valued hidden units, and minimizes a conditional cross-entropy of targets given inputs. Because it models the joint distribution, an RBM can extract structure in the feature vector that supervised training would ignore, and these unsupervised features often prove useful downstream. Classification is done by clamping V1 and either sampling the label distribution or comparing the unnormalized joint densities across label categories (the partition function cancels).

Exact maximum-likelihood learning requires the gradient term E_Theta(X_j X_k), estimated by Gibbs sampling to stationarity -- but mixing is slow, especially as weights grow. The practical fix is contrastive divergence (Hinton, 2002), which starts the chain at the data and runs only a few steps. RBMs trained this way and stacked greedily layer-by-layer (Hinton et al., 2006) learn powerful feature hierarchies: on MNIST a single RBM reaches a 1.9% test error, reduced to 1.25% by first learning 500 unsupervised features through a stack of RBMs -- competitive with SVMs and backprop-trained neural networks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[multilayer-perceptron]] — contrasts-with: Same single-hidden-layer shape but undirected/generative joint-likelihood vs directed/discriminative conditional cross-entropy.
- [[gibbs-sampler]] — uses: Block Gibbs sampling of whole layers exploits within-layer conditional independence.
- [[undirected-graphical-models]] — specializes: An RBM is an undirected, energy-based graphical model over binary units.
- [[boltzmann-machine]] — specializes: An RBM is a Boltzmann machine with a bipartite (no intra-layer) connection structure.
[To be populated during integration]