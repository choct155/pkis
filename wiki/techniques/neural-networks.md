---
aliases: []
also_type:
- framework
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- deep-learning
- statistical-learning
id: pkis:technique:neural-networks
knowledge_type: technique
maturity: settled
related_concepts:
- '[[bias-variance-tradeoff]]'
- '[[regularization]]'
sources:
- '[[hastie-esl]]'
- '[[nielsen-nndl]]'
- '[[marcus-dl-critical-appraisal-2018]]'
tags:
- optimization
- linear-algebra
title: Neural Networks (Feedforward)
understanding: 0
---

Layered function approximators that compose affine transformations with nonlinear activation functions, trained by gradient-based optimization (backpropagation). Classification note: assigned as technique but also functions as a framework — neural networks encompass an architecture space, training methodology, regularization strategies (weight decay, early stopping, dropout), and Bayesian extensions.

## Reading Path
- [[nielsen-nndl-ch01]] (unread) — builds a working feedforward MNIST classifier from perceptrons and sigmoid neurons; the primary principle-oriented treatment
- [[nielsen-nndl-ch03]] (unread) — covers practical improvements: cross-entropy loss, regularization, dropout, weight initialization
- [[hastie-esl-ch11]] (unread) — statistical learning perspective on neural networks
- [[marcus-dl-critical-appraisal-2018]] (unread) — critical appraisal of the deep learning paradigm as a whole; identifies 10 structural limitations including poor generalization outside training distribution, need for large datasets, opacity, and lack of compositionality; motivates hybrid neural-symbolic architectures

## Specifying a Neural Network: Architecture, Activity Rule, Learning Rule
MacKay (ITILA Ch. 38) gives a clean three-part specification that defines any neural network model:

- **Architecture** — what variables exist and their topological relationships. Typically the *weights* of connections between neurons and the *activities* of the neurons.
- **Activity rule** — the short-time-scale dynamics: local rules saying how neuron *activities* change in response to one another, usually as a function of the (fixed) weights.
- **Learning rule** — the long-time-scale dynamics: how the *weights* change over time. The learning rule generally depends on the neuron activities, and may also depend on *target* values supplied by a teacher.

The key separation is the **two time scales**: activities settle quickly under fixed weights (the activity rule), while weights adapt slowly (the learning rule). MacKay notes these rules may be *invented* by researchers or, more principledly, *derived* from a chosen objective function — the latter being the route that connects neural networks to probabilistic modelling and gradient-based optimization.

## Learning Paradigms: Supervised vs Unsupervised
MacKay divides neural network algorithms into two broad classes by the form of the data they consume:

- **Supervised networks** receive *inputs paired with targets*, where the target is a teacher's specification of the desired response. Learning shapes the weights so the network's output matches the target.
- **Unsupervised networks** receive data in undivided form, simply a set of examples $\{\mathbf{x}\}$. Some unsupervised algorithms merely *memorize* the examples for later recall (associative memories); others aim to *generalize* — to discover patterns, extract underlying features, or model the data distribution.

The boundary is porous: an unsupervised model that can *fill in missing variables* of an example $\mathbf{x}$ (predicting one part of the data from another) thereby also acts as a supervised network. This blurring foreshadows the modern view of self-supervised learning, where supervision targets are manufactured from the structure of the unlabelled data itself.

## Memory Capacity of a Single Neuron
Viewed as a communication channel, a binary linear threshold neuron with $K$ weights can store about $2K$ bits — **two bits per weight**. It can almost certainly memorise any random binary labelling of up to $N=2K$ points (in general position) and almost certainly fails beyond that, a sharp phase transition. The number of realisable dichotomies is Cover's $T(N,K)=2\sum_{k=0}^{K-1}\binom{N-1}{k}$, equal to $2^N$ for $N\le K$; hence the VC dimension of a $K$-input threshold unit is $K$. See [[capacity-of-a-single-neuron]] and [[cover-function-counting-theorem]].