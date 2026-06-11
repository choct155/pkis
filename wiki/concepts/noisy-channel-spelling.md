---
aliases: []
also_type: []
analogous-to:
- binary-symmetric-channel
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
- natural-language-processing
- information-theory
id: pkis:concept:noisy-channel-spelling
instantiates:
- hidden-markov-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
tags:
- spelling-correction
- edit-distance
- noisy-channel
- language-model
title: Noisy Channel Model (Spelling Correction)
understanding: 0
uses:
- n-gram-language-model
- language-model
---

## Definition
A probabilistic model for spelling correction that treats the intended word $z$ as a message corrupted by a noisy channel to produce the observed word $y$. The likelihood is defined via edit distance:

$$p(y \mid z) = \begin{cases} p_1 & y = z \\ p_2 & y \in D(z,1) \\ p_3 & y \in D(z,2) \\ p_4 & \text{otherwise} \end{cases}$$

where $D(z,d)$ is the set of words at edit distance $d$ from $z$ and $p_1 > p_2 > p_3 > p_4$. Combined with a language model prior $p(z_{1:T})$ (unigram or bigram), the MAP estimate $\hat{z} = \arg\max_z p(z)p(y|z)$ gives the most likely correction. Upgrading the prior to a first-order Markov (bigram) model naturally yields an HMM over word sequences.

### Why it matters
The noisy channel framework is a foundational NLP paradigm that cleanly separates the language model (prior) from the error model (likelihood), enabling modular improvement of each component and extension to context-aware correction via HMM inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[binary-symmetric-channel]] — analogous-to
- [[language-model]] — uses
- [[n-gram-language-model]] — uses
- [[hidden-markov-model]] — instantiates
[To be populated during integration]