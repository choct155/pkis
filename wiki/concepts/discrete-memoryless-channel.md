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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:discrete-memoryless-channel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- channel-capacity
- noisy-channel-coding-theorem
related_concepts: []
sources:
- mackay-itila-ch09
tags:
- channel
- transition-matrix
- noise
- memoryless
- mackay
title: Discrete Memoryless Channel
understanding: 0
---

## Definition
A discrete memoryless channel (DMC) $Q$ is the basic model of noisy transmission: it is specified by an input alphabet $\mathcal{A}_X$, an output alphabet $\mathcal{A}_Y$, and a set of transition probabilities $P(y\mid x)$, one distribution over outputs for each input. 'Memoryless' means each use is independent: the output at one time depends only on that time's input.

### Transition matrix
The transitions form a matrix
$$Q_{j\mid i} = P(y=b_j \mid x=a_i),$$
with outputs indexing rows and inputs indexing columns, so each column is a probability vector. The output distribution follows from the input distribution by matrix multiplication:
$$\mathbf{p}_Y = Q\,\mathbf{p}_X.$$

### Inference over a channel
Given a received $y$, the input is recovered probabilistically via Bayes' theorem,
$$P(x\mid y) = \frac{P(y\mid x)P(x)}{\sum_{x'} P(y\mid x')P(x')}.$$
Decoding is then a posterior-inference problem, and pattern recognition (handwritten digits, speech) can be framed as decoding a DMC whose output is the observed signal.

### Why it matters
The DMC is the object the noisy-channel coding theorem is stated about. Its capacity $C=\max_{P_X} I(X;Y)$ and the typical-set counting argument over the extended channel $Q^N$ both rest on this clean transition-matrix abstraction, which separates the fixed physics of the noise from the engineer's free choice of input distribution and code.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[noisy-channel-coding-theorem]] — prerequisite-of: The coding theorem is stated about a discrete memoryless channel.
- [[channel-capacity]] — prerequisite-of: Capacity is a property defined for a given DMC Q.
[To be populated during integration]