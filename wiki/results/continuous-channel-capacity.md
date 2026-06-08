---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:result:continuous-channel-capacity
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch11
tags:
- channel-capacity
- shannon-hartley
- bandwidth
- snr
- awgn
- mackay
title: Continuous-Channel Capacity (Shannon–Hartley)
understanding: 0
---

## Definition
For a Gaussian channel with input power $v$ and noise variance $\sigma^2$, the capacity-achieving input is itself Gaussian and the **capacity per channel use** is
$$C=\tfrac{1}{2}\log\!\Big(1+\tfrac{v}{\sigma^2}\Big)\quad\text{bits}.$$
A continuous-time channel of bandwidth $W$, noise spectral density $N_0$ and power $P$ is equivalent to $2W$ uses per second of such a channel ($\sigma^2=N_0/2$, $\overline{x^2}\le P/2W$), giving the **Shannon–Hartley** law
$$C=W\log\!\Big(1+\tfrac{P}{N_0 W}\Big)\quad\text{bits/s}.$$

### Bandwidth–power tradeoff
With $W_0=P/N_0$, capacity rises to the asymptote $W_0\log e$ as $W\to\infty$. For fixed power it is dramatically better to spread signal at low SNR over wide bandwidth than to push high SNR through a narrow band — the rationale for spread-spectrum and 3G CDMA.

### Why it matters
This is the single most-cited formula in communication engineering: it sets the ceiling on every real link's bit rate and frames the bandwidth/power/SNR design space within which all practical coding operates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]