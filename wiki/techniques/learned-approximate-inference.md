---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- mean-field-variational-inference
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- variational-methods
generalizes:
- wake-sleep-algorithm
id: pkis:technique:learned-approximate-inference
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- variational-autoencoder
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
specializes:
- amortized-inference
tags:
- encoder-network
- VAE
- inference-network
- amortization
- approximate-inference
title: Learned Approximate Inference (Amortized Inference)
understanding: 0
uses:
- inference-as-optimization
- neural-networks
---

## Definition
Instead of solving the variational optimization $q^* = \arg\max_q \mathcal{L}(v, q)$ independently for each input $v$ at test time, amortized inference trains a parametric function (typically a neural network) $\hat{f}(v; \phi)$ to directly output the variational parameters:

$$q^*(h|v) \approx \hat{f}(v; \phi)$$

The parameters $\phi$ are learned end-to-end by maximizing the ELBO, with $\phi$ shared across all inputs. This replaces a per-example iterative optimization with a single forward pass.

### Why it matters
Amortized inference is the core idea behind the **variational autoencoder**: the encoder network is an amortized inference network, and the ELBO is jointly optimized over generative parameters $\theta$ and encoder parameters $\phi$ using the reparameterization trick. Earlier instantiations include wake-sleep (recognition network trained on generated samples) and PSD/LISTA (shallow/deep encoders approximating sparse MAP inference). Amortized inference dramatically reduces test-time cost at the expense of some inference quality (amortization gap).

### Amortization Gap
The gap between the ELBO achieved by amortized inference and by per-example optimization is called the amortization gap, and can be reduced by using more expressive encoder networks or by performing a few steps of iterative refinement after the encoder pass.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mean-field-variational-inference]] — contrasts-with
- [[neural-networks]] — uses
- [[inference-as-optimization]] — uses
- [[variational-autoencoder]] — prerequisite-of
- [[wake-sleep-algorithm]] — generalizes
- [[amortized-inference]] — specializes
[To be populated during integration]