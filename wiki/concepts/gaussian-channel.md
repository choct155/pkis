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
id: pkis:concept:gaussian-channel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch11
tags:
- continuous-channel
- awgn
- noise
- signal-to-noise-ratio
- mackay
title: Gaussian Channel (AWGN)
understanding: 0
---

## Definition
The **Gaussian channel** is the canonical model of a real-input, real-output, discrete-time channel: the output is the input plus additive Gaussian noise,
$$P(y\mid x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left[-\tfrac{(y-x)^2}{2\sigma^2}\right],\qquad y=x+n,\; n\sim\mathrm{Normal}(0,\sigma^2).$$
It is also called the **additive white Gaussian noise (AWGN)** channel. Because an unconstrained real input could encode arbitrarily many digits in one use, a **power cost** $v(x)=x^2$ is imposed and codes are constrained to mean power $\overline{x^2}=v$; the relevant figure of merit is the signal-to-noise ratio $v/\sigma^2$.

### Posterior inference
With a Gaussian prior $P(x)=\mathrm{Normal}(0,v)$, the posterior is $\mathrm{Normal}\big(\tfrac{v}{v+\sigma^2}y,\,(1/v+1/\sigma^2)^{-1}\big)$ — the posterior mean blends the data fit $x=y$ and the prior $x=0$, and **precisions add**.

### Why it matters
The Gaussian channel is the bridge from Shannon's discrete theory to physical communication. Almost every real electrical, optical, or radio link is modelled (after orthonormal-basis decomposition) as repeated uses of a Gaussian channel, so it underpins the capacity formulas that govern modems, deep-space links, and mobile telephony.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]