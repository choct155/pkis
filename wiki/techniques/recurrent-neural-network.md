---
aliases: []
also_type: []
analogous-to:
- kalman-filter
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- multilayer-perceptron
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
id: pkis:technique:recurrent-neural-network
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- sequence-to-sequence-model
related_concepts: []
sources:
- russell-norvig-aima-ch21
- russell-norvig-aima-ch24
tags:
- sequential-data
- internal-state
- weight-sharing
- backpropagation-through-time
title: Recurrent Neural Network (RNN)
understanding: 0
uses:
- backpropagation
---

## Definition
A neural network whose computation graph contains cycles, so that units may take as input a value computed from their own output at an earlier time step. Each cycle carries a one-step delay, giving the network internal state (memory): inputs received at earlier time steps influence the response to the current input. The canonical model has input x_t, a recurrently-connected hidden layer z_t, and output y_t, with the update z_t = f_w(z_{t-1}, x_t) = g_z(W_{z,z} z_{t-1} + W_{x,z} x_t) and y_hat_t = g_y(W_{z,y} z_t). The weight matrices are shared across all time steps, encoding a time-homogeneous process (a universally-quantified assertion that the dynamics hold for all t). Like HMMs, dynamic Bayes nets, and Kalman filters, an RNN makes a Markov assumption: the hidden state z_t summarizes all previous inputs. Trained by 'unrolling' the network for T steps into a feedforward graph and applying backpropagation through time. RNNs add expressive power over feedforward networks for sequential data, which a fixed-input-size feedforward net could only handle within a finite window, missing long-distance dependencies.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sequence-to-sequence-model]] — prerequisite-of
- [[kalman-filter]] — analogous-to: both summarize past inputs in a hidden state under a Markov assumption for sequential data
- [[multilayer-perceptron]] — contrasts-with: adds cyclic connections and internal state vs. a strictly feedforward network
- [[backpropagation]] — uses: trained by backpropagation through time on the unrolled network
[To be populated during integration]