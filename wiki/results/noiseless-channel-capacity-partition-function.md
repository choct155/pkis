---
aliases: []
also_type: []
analogous-to:
- constrained-channel-capacity-eigenvalue
applies:
- maximum-entropy-principle
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- information-theory
id: pkis:result:noiseless-channel-capacity-partition-function
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch22
specializes:
- channel-capacity
tags:
- channel-capacity
- partition-function
- jaynes
- noiseless-channel
- lagrange-multipliers
- statistical-mechanics-analogy
- cost-per-symbol
title: Noiseless Channel Capacity via the Partition Function
understanding: 0
uses:
- partition-function
- lagrange-multipliers
---

## Definition
## Definition
For a noiseless channel whose symbol $A_i$ has transmission cost (e.g. time) $t_i$, with no other constraint on admissible sequences, the channel capacity $C \equiv \lim_{t\to\infty} t^{-1}\log W(t)$ is the real root of
$$Z(\lambda) \equiv \sum_i \exp\{-\lambda t_i\} = 1.$$
That is, define the partition function $Z(\lambda)$ over symbols; the capacity is the value $\lambda = C$ making $Z=1$.

### Derivation (most-probable-distribution)
The number of length-$N$ messages with letter counts $n_i$ is the multinomial $W = N!/\prod_i n_i!$, and $W(t)$ sums these over all counts satisfying $\sum_i n_i t_i \le t$. Because the number of contributing terms grows only polynomially ($K(t)\le (Bt)^a$) while the largest term grows exponentially, $\log W(t)$ and $\log W_{\max}$ have the same limit — so $C$ is found by maximizing $\log W(n_1,\dots,n_a)$ subject to the cost constraint via a Lagrange multiplier $\lambda$. The maximizing frequencies are the canonical distribution $f_i = n_i/N = \exp\{-C t_i\}$, and the normalization $\sum_i \exp\{-\lambda t_i\}=1$ identifies $\lambda=C$.

### Generalizations and meaning
- **State machine (channel with memory):** if symbol transitions $S_i\to A_n\to S_j$ cost $t_{inj}$, define the partition matrix $Z_{ij}(\lambda)=\sum_n \exp\{-\lambda t_{inj}\}$; capacity is the greatest real root of $\det[Z_{ij}(\lambda)-\delta_{ij}]=0$, i.e. the $\lambda$ at which $Z_{ij}$ has unit eigenvalue. The single-state case recovers $Z(\lambda)=1$.
- **Cost reinterpretation:** $t_i$ need not be time. If $t_i$ is energy (joules) to send symbol $i$, $C$ is measured in bits per joule and $1/C$ is the minimum joules per transmitted bit — relevant e.g. to a space probe.
- **Variational duality:** equivalently $C$ gives the maximum number $W$ of messages for a fixed transmission time, or the minimum transmission time for fixed $W$.

This is Jaynes's statistical-mechanics rendering of Shannon's noiseless-channel results: the partition-function/canonical-distribution machinery of stat-mech yields capacity directly, before any probability is introduced.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-entropy-principle]] — applies
- [[constrained-channel-capacity-eigenvalue]] — analogous-to
- [[lagrange-multipliers]] — uses
- [[partition-function]] — uses
- [[channel-capacity]] — specializes
[To be populated during integration]