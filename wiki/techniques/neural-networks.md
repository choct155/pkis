---
aliases: []
also_type:
- framework
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-20'
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
- nielsen-nndl-ch01
- nielsen-nndl-ch03
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

## Feedback Networks and the Hopfield Model
Neural networks split by connectivity into **feedforward** networks (connections form a directed acyclic graph) and **feedback** (recurrent) networks (anything else). The **Hopfield network** is the canonical feedback network: fully connected with *symmetric* weights $w_{ij}=w_{ji}$ and no self-connections, every neuron's output feeding back as input to all others.

This feedback structure is what gives the network its distinctive capability — *attractor dynamics* and content-addressable memory — but it also forces a choice of update order (synchronous vs. asynchronous) absent in feedforward nets, and convergence is only guaranteed under symmetry with asynchronous updates.

A neat unification (MacKay's Exercise 42.10): if a Hopfield network's memories are all stable, then *each neuron* solves a single-neuron binary classification problem on the other neurons' states. So an unsupervised associative memory is, internally, a collection of supervised binary classifiers — and the same cross-entropy objective and gradient algorithm used to train one neuron can train the whole network, outperforming the one-shot Hebb rule.

## Probabilistic Interpretation of Supervised Training (MacKay Ch. 44)
MacKay gives supervised network training a clean probabilistic reading: the error function *is* a negative log likelihood and the regularizer *is* a negative log prior, so minimizing the objective is MAP inference.

- **Likelihood / noise model:** $P(D\mid\mathbf{w},\beta,H) = \frac{1}{Z_D(\beta)}\exp(-\beta E_D)$. Sum-squared error $E_D$ thus assumes Gaussian output noise with variance $\sigma_\nu^2 = 1/\beta$. For classification, $\beta E_D$ is replaced by the cross-entropy $G(\mathbf{w})$ and there is no $\beta$ (no Gaussian noise).
- **Prior:** $P(\mathbf{w}\mid\alpha,H) = \frac{1}{Z_W(\alpha)}\exp(-\alpha E_W)$. Quadratic $E_W$ gives a Gaussian prior with variance $\sigma_W^2 = 1/\alpha$ — weight decay as a prior.
- **Posterior:** $P(\mathbf{w}\mid D,\alpha,\beta,H) = \frac{1}{Z_M}\exp(-M(\mathbf{w}))$, so the minimizer $\mathbf{w}_{\text{MP}}$ is the most probable parameter vector.

**Why this reframing pays off.** From the statistical view a supervised net is just a nonlinear curve-fitter, and the central difficulty is effective complexity: as a control parameter (e.g. weight-decay $\alpha$, hidden-unit count, basis radius) increases model complexity, training error keeps falling but test error first falls then rises — the overfitting U-curve. The Bayesian treatment controls this by maximizing the *evidence* $P(D\mid\text{control parameters})$: over-complex models are automatically penalised (Occam), no validation set is needed (all data fit the model and compare it), hyperparameters can be optimized on-line and by gradient, and the objective is noise-free unlike cross-validation. Marginalizing over $\mathbf{w}$ further yields predictive error bars (figure 44.6). Implementation is via Monte Carlo or Gaussian (Laplace) approximations.