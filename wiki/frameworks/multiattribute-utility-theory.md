---
aliases: []
also_type: []
analogous-to:
- bayesian-networks
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- agentic-systems
id: pkis:framework:multiattribute-utility-theory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch16
specializes:
- expected-utility-theory
tags:
- decision-theory
- utility
- preference-independence
- representation-theorem
- public-policy
title: Multiattribute Utility Theory
understanding: 0
uses:
- stochastic-dominance
---

## Definition
## Definition
**Multiattribute utility theory (MAUT)** handles decision problems whose outcomes are characterized by two or more attributes $\mathbf{X}=X_1,\ldots,X_n$ (e.g., an airport site scored on throughput, safety, quietness, frugality). "In essence, it's the theory of comparing apples to oranges." Specifying a full utility $U(x_1,\ldots,x_n)$ over $n$ attributes each taking $d$ values needs $d^n$ entries in the worst case; MAUT identifies structure in preferences that yields a concise representation $U = F[f_1(x_1),\ldots,f_n(x_n)]$ with $F$ a simple function (R&N Section 16.4). The construction assumes attributes are arranged to be monotonically increasing in utility.

### Preference independence → additive value
In the deterministic (no-uncertainty) case the agent has a **value function** $V$. The key regularity is **mutual preferential independence (MPI)**: a set of attributes is MPI if how you trade off any subset does not depend on the values of the rest. Debreu's (1960) representation theorem shows MPI implies an **additive value function** $V(x_1,\ldots,x_n)=\sum_i V_i(x_i)$, reducing assessment from one $n$-dimensional function to $n$ one-dimensional ones — typically an exponential saving in elicitation effort. MPI can fail when attributes interact (e.g., hunting dogs eat chickens unless you also have cages).

### Utility independence → multiplicative utility
Under uncertainty one needs structure over *lotteries*, not just values. **Utility independence** extends preference independence to lotteries; **mutual utility independence (MUI)** holds when every subset is utility-independent of the rest. Keeney's (1974) theorem shows MUI implies a **multiplicative utility function** — for $n$ attributes, just $n$ single-attribute utilities $U_i$ and $n$ constants $k_i$ suffice, each $U_i$ developed independently. Additional assumptions are needed to collapse this to a purely additive form.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-networks]] — analogous-to: additive/multiplicative utility decomposition mirrors BN factorization of a joint distribution
- [[stochastic-dominance]] — uses: stochastic dominance discards dominated options within MAUT
- [[expected-utility-theory]] — specializes: MAUT specializes EU theory to vector-valued outcomes
- Specializes the general expected-utility framework to vector-valued outcomes.
- Uses stochastic dominance to discard dominated options without numeric utilities.
- Structurally analogous to Bayesian-network decomposition of a joint distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]