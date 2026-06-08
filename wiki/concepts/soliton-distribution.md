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
id: pkis:concept:soliton-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch50
tags:
- lt-codes
- degree-distribution
- ideal-soliton
- robust-soliton
- density-evolution
- fountain-codes
title: Soliton Degree Distributions
understanding: 0
---

## Definition
The **degree distribution** $\rho(d)$ — the probability that an LT-encoded packet combines $d$ source packets — is the critical design choice of an LT code, trading two opposing pressures: enough **low-degree** packets so peeling decoding can start and continue, yet some **high-degree** packets so no source packet is left unconnected.

The **ideal soliton distribution** is engineered so that, in expectation, exactly one degree-one check node appears at each peeling step:

$$\rho(1) = \tfrac{1}{K}, \qquad \rho(d) = \frac{1}{d(d-1)}, \quad d = 2,\dots,K,$$

with mean degree $\approx \ln K$. It is optimal *on average* but fragile: fluctuations frequently leave **zero** degree-one nodes, stalling decoding, and a few source nodes get no edges.

The **robust soliton distribution** $\mu(d) \propto \rho(d) + \tau(d)$ fixes this by maintaining an expected $S \equiv c\,\ln(K/\delta)\sqrt{K}$ degree-one checks throughout. The extra term $\tau$ adds a small-$d$ ramp (to keep decoding started) plus a spike at $d = K/S$ (to ensure every source packet is covered). Here $\delta$ bounds decode-failure probability and $c$ is an $O(1)$ tuning constant; receiving $K' = KZ$ packets ($Z$ = normalizer) suffices.

### Why it matters
The soliton design is what makes LT codes *work*: Luby's main theorem guarantees that $K' = K + 2\ln(S/\delta)S$ checks recover all packets with probability $\ge 1-\delta$, while bounding decoding complexity to $O(K\ln K)$. The behaviour of the decoding process under a given $\rho$ is predicted by **density evolution**.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]