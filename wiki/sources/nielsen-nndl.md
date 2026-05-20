---
title: "Neural Networks and Deep Learning"
authors: "Michael A. Nielsen"
year: 2015
type: book
domain: [deep-learning, optimization]
tags: [neural-networks, gradient-descent, backpropagation, convolutional-networks, regularization]
source_url: "http://neuralnetworksanddeeplearning.com"
drive_id: "1OvaRAM8W_QPmYOVaeZDMVbNTBBI-7txZ"
drive_path: "PKIS/sources/books/Neural Networks and Deep Learning"
isbn: ""
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts:
  - "[[neural-networks]]"
  - "[[backpropagation]]"
  - "[[gradient-descent]]"
  - "[[convolutional-neural-networks]]"
  - "[[dropout]]"
  - "[[cross-entropy-loss]]"
  - "[[activation-functions]]"
  - "[[universal-approximation-theorem]]"
  - "[[vanishing-gradient-problem]]"
  - "[[weight-initialization]]"
  - "[[regularization]]"
  - "[[automatic-differentiation]]"
---

## Summary

*Neural Networks and Deep Learning* is a free online book by Michael Nielsen that provides a rigorous yet accessible introduction to the core concepts and techniques of neural networks and deep learning. The book takes a hands-on, principle-oriented approach: rather than surveying a broad landscape of tools, it develops a small set of foundational ideas deeply, using Python code and the MNIST handwritten-digit recognition problem as a running example throughout.

The book opens with the basics of perceptrons and sigmoid neurons, then builds up to gradient-descent training and a working MNIST classifier. Chapter 2 derives backpropagation from first principles, establishing four fundamental equations that give insight into how gradients flow through a layered network. Chapter 3 is the technical core of modern training practice, covering the cross-entropy cost function (solving the learning-slowdown problem of quadratic cost), L1/L2 regularization, dropout, improved weight initialization, and SGD variants including momentum and adaptive learning rates.

Chapter 4 presents a visual, constructive proof of the universal approximation theorem: a single hidden layer of sigmoid neurons can approximate any continuous function to arbitrary accuracy. Chapter 5 diagnoses why deep networks are hard to train by analyzing the vanishing (and exploding) gradient problem — gradients in early layers are systematically smaller than in later layers due to the product of bounded sigmoid derivatives. Chapter 6 introduces convolutional neural networks (local receptive fields, shared weights, pooling) and achieves near-human performance on MNIST, then surveys recurrent networks, LSTMs, and deep belief networks. An appendix reflects on whether a simple universal learning algorithm is theoretically achievable.

The book's strength is conceptual depth over breadth: every technique is motivated, derived, and implemented. There is no ISBN as this is a freely distributed online book first published in 2015.

## Key Knowledge Objects

- [[neural-networks]] (technique, high) — feedforward layered function approximators trained by backpropagation; receives extended treatment throughout the book
- [[backpropagation]] (technique, high) — reverse-mode chain rule for gradient computation; derived from four fundamental equations in Ch. 2
- [[gradient-descent]] (technique, high) — iterative optimization by steepest descent; SGD and momentum variants covered in Ch. 1 and 3
- [[cross-entropy-loss]] (concept, high) — loss function that avoids learning slowdown from saturated output neurons; derived in Ch. 3
- [[activation-functions]] (concept, high) — sigmoid, tanh, and ReLU neurons; comparison and trade-offs covered in Ch. 3 and 6
- [[dropout]] (technique, high) — regularization by randomly zeroing hidden neurons during training; covered in Ch. 3
- [[universal-approximation-theorem]] (result, high) — a single hidden layer can approximate any continuous function; constructive visual proof in Ch. 4
- [[vanishing-gradient-problem]] (problem, high) — gradients in early layers systematically shrink during backpropagation in deep networks; diagnosed in Ch. 5
- [[convolutional-neural-networks]] (technique, high) — local receptive fields, shared weights, and pooling for spatial data; introduced in Ch. 6
- [[weight-initialization]] (technique, moderate — could be principle) — improved initialization scales weights by 1/sqrt(n_in) to avoid saturated neurons; covered in Ch. 3
- [[regularization]] (concept, high) — L1 and L2 penalties, dropout, and data augmentation as overfitting controls; covered in Ch. 3

## Key Extractions

1. **Four fundamental equations of backpropagation** (Ch. 2): BP1 gives the error in the output layer δ^L = ∇_a C ⊙ σ'(z^L); BP2 propagates error backward δ^l = ((w^{l+1})^T δ^{l+1}) ⊙ σ'(z^l); BP3 gives ∂C/∂b^l_j = δ^l_j; BP4 gives ∂C/∂w^l_{jk} = a^{l-1}_k δ^l_j. These four equations together fully characterize how gradients flow through the network.

2. **Learning slowdown with quadratic cost** (Ch. 3): When using MSE loss, a sigmoid output neuron learns slowly when its activation is near 0 or 1 because ∂C/∂w ∝ σ'(z) → 0. Cross-entropy resolves this: ∂C/∂w_j = (a - y) x_j, removing the σ' factor entirely.

3. **Dropout as implicit ensemble** (Ch. 3): Dropout trains an exponential number of thinned networks and at test time approximates their geometric mean by halving the outgoing weights of hidden neurons. This implicit ensembling effect is the primary explanation for its regularization power.

4. **Vanishing gradient diagnosis** (Ch. 5): In a deep network with sigmoid activations, the gradient in an early layer involves a product of terms |w σ'(z)| ≤ |w|/4. If weights are initialized around 1, this product shrinks exponentially with depth, causing early layers to learn exponentially slower than later layers.

5. **Universal approximation** (Ch. 4): Using sigmoid neurons, a two-layer network can approximate any continuous function f: [0,1]^m → R^n to arbitrary precision. The constructive proof works by building step functions from pairs of neurons with large weights, then combining them.

6. **Convolutional key ideas** (Ch. 6): CNNs achieve translation invariance by using shared weights across a spatial feature map (local receptive fields), dramatically reducing parameters. Pooling (max or mean) further compresses spatial dimensions. Nielsen's networks achieve ~99% accuracy on MNIST by combining convolutional layers with fully-connected layers.

7. **Weight initialization** (Ch. 3): Standard initialization (Gaussian with σ=1) saturates many neurons in large networks. Improved initialization uses mean=0, σ=1/√n_in for weights, causing neuron inputs to have variance ≈ 1 regardless of fan-in, avoiding saturation at initialization.

## Connection Candidates

- [[neural-networks]] — uses: this book is the primary treatment of feedforward networks at depth
- [[backpropagation]] — uses: Ch. 2 derives backpropagation from scratch
- [[automatic-differentiation]] — prerequisite-of: backpropagation is a special case of reverse-mode AD; this book approaches it from the NN angle
- [[regularization]] — specializes: dropout and weight decay (L2) are neural-network-specific regularization instances
- [[gradient-descent]] — extends: Ch. 3 covers SGD, momentum, and adaptive-rate variants extending vanilla gradient descent
- [[bias-variance-tradeoff]] — grounds: regularization choices in Ch. 3 are motivated by the bias-variance tradeoff

## Chapters

| Ch | Stub | Title |
|---|---|---|
| 1 | [[nielsen-nndl-ch01]] | Using neural nets to recognize handwritten digits |
| 2 | [[nielsen-nndl-ch02]] | How the backpropagation algorithm works |
| 3 | [[nielsen-nndl-ch03]] | Improving the way neural networks learn |
| 4 | [[nielsen-nndl-ch04]] | A visual proof that neural nets can compute any function |
| 5 | [[nielsen-nndl-ch05]] | Why are deep neural networks hard to train? |
| 6 | [[nielsen-nndl-ch06]] | Deep learning |
| A | [[nielsen-nndl-appA]] | Is there a simple algorithm for intelligence? |
