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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- state-space-models
- time-series
id: pkis:concept:filtering-prediction-smoothing
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch14
tags:
- filtering
- state-estimation
- prediction
- smoothing
- most-likely-explanation
- recursive-estimation
- belief-state
- forward-message
- backward-message
- inference-tasks
title: Filtering, Prediction, Smoothing, and Most Likely Explanation
understanding: 0
uses:
- markov-chains
---

## Definition
The four canonical inference tasks of a temporal probability model, all expressible over the same transition/sensor model independently of its specific form (HMM, Kalman filter, or DBN):

1. **Filtering / state estimation**: compute the belief state P(X_t | e_{1:t}), the posterior over the *current* state given all evidence to date. This is what a rational agent maintains to act, and an almost identical recursion yields the evidence likelihood P(e_{1:t}).
2. **Prediction**: compute P(X_{t+k} | e_{1:t}) for k > 0, the posterior over a *future* state. Prediction is filtering without new evidence; iterating it drives the belief toward the transition model's stationary distribution, so accurate prediction is impossible far beyond the mixing time.
3. **Smoothing**: compute P(X_k | e_{1:t}) for 0 <= k < t, the posterior over a *past* state given all evidence up to now - a better estimate than was available at time k because it incorporates later evidence.
4. **Most likely explanation**: compute argmax over x_{1:t} of P(x_{1:t} | e_{1:t}), the single most probable *state sequence*, which can differ from the sequence of per-step most-probable states.

## Recursive estimation and message passing
Filtering is made efficient by *recursive estimation*: P(X_{t+1} | e_{1:t+1}) = f(e_{t+1}, P(X_t | e_{1:t})), decomposed into a prediction step (project forward through the transition model) and an update step (multiply by the sensor likelihood and normalize). The filtered estimate is propagated as a forward message f_{1:t+1} = FORWARD(f_{1:t}, e_{t+1}); when state variables are discrete the time and space per update are constant. Smoothing adds a backward message b_{k+1:t} = P(e_{k+1:t} | X_k) computed by a backward recursion, with the smoothed posterior given by the pointwise product alpha f_{1:k} x b_{k+1:t}.

## Practical issues
The likelihood and Viterbi messages shrink toward underflow, handled by normalization or log-space arithmetic. Online smoothing typically uses *fixed-lag smoothing*, computing P(X_{t-d} | e_{1:t}) as t advances, which can be done in constant time per update.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-chains]] — uses: The recursive filtering and smoothing decompositions rely on the (first-order) Markov property of the state process.
[To be populated during integration]