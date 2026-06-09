---
aliases: []
also_type: []
analogous-to:
- min-sum-algorithm
applies:
- hidden-markov-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- state-space-models
- information-theory
id: pkis:technique:viterbi-for-hmm
instantiates:
- max-product-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch14
specializes:
- filtering-prediction-smoothing
tags:
- viterbi
- most-likely-explanation
- max-product
- dynamic-programming
- trellis
- decoding
- speech-recognition
- backpointers
title: Viterbi Algorithm for HMMs (Most Likely Sequence)
understanding: 0
---

## Definition
A linear-time dynamic-programming algorithm for the most-likely-explanation task in a temporal model: finding the single state sequence argmax over x_{1:t} of P(x_{1:t} | e_{1:t}) that best explains an observation sequence. It views each candidate sequence as a path through a graph (trellis) whose nodes are the possible states at each time step, and exploits the Markov property: the most likely path to a state x_{t+1} extends the most likely path to some state x_t by a single transition.

## Recursion
It propagates a message m_{1:t} = max over x_{1:t-1} of P(x_{1:t-1}, X_t, e_{1:t}), updated by
m_{1:t+1} = P(e_{t+1} | X_{t+1}) max over x_t of [ P(X_{t+1} | x_t) m_{1:t}(x_t) ].
This is *identical to the filtering recursion* except that the summation over x_t is replaced by a maximization and there is no normalizing constant. To recover the actual sequence (not just its probability), the algorithm stores back-pointers recording, for each state, the best predecessor; the optimal path is read off by following back-pointers from the best final state.

## Complexity and numerics
Time is linear in the sequence length t (like filtering), but unlike constant-space filtering, space is also linear in t because the back-pointers must be retained. Probabilities shrink toward underflow over long sequences (DNA, message decoding can run for millions of steps); fixes are to normalize m at each step (valid since max(cx,cy)=c max(x,y)) or to work in log space and replace multiplication by addition (valid since log is monotonic). The Viterbi algorithm first appeared in Viterbi (1967).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[filtering-prediction-smoothing]] — specializes: Viterbi solves the most-likely-explanation task, one of the four canonical temporal inference tasks.
- [[max-product-algorithm]] — instantiates: Viterbi is the max-product (max/sum) semiring version of the forward filtering recursion.
- [[min-sum-algorithm]] — analogous-to: Same trellis dynamic program; the AIMA HMM most-likely-explanation framing is the probabilistic-temporal counterpart of the min-sum/Viterbi decoder.
- [[hidden-markov-model]] — applies: Viterbi computes the most likely hidden state sequence for an HMM observation sequence.
[To be populated during integration]