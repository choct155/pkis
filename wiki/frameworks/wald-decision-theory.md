---
aliases: []
also_type: []
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
id: pkis:framework:wald-decision-theory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch13
specializes:
- decision-theory-foundations
tags:
- decision-theory
- wald
- states-of-nature
- loss-matrix
- risk
- sampling-theory
title: Wald's Decision Theory
understanding: 0
uses:
- expected-loss
---

## Definition
Abraham Wald's (1950) formalization of decision-making under uncertainty, originally built with no apparent connection to probability theory. Its primitives are: (1) an enumeration of possible **states of nature** $\{\theta_1,\dots,\theta_N\}$ — a description of one's *state of knowledge* about the range of possibilities, not a verifiable property of nature (exactly one $\theta_j$ is in fact true); (2) an enumeration of feasible **decisions** $\{D_1,\dots,D_k\}$, where 'making decision $D_i$' means 'deciding to act as if $D_i$ were correct'; and (3) a **loss function** $L(D_i,\theta_j)$ (a loss matrix $L_{ij}$ in the discrete case) encoding the cost of taking decision $D_i$ when $\theta_j$ is true. Given additional evidence $E$, Wald defines a **strategy** $S$ (a rule mapping evidence to decisions), the sampling probability $p(D_k\mid\theta_j S)=\sum_i p(D_k\mid E_i\theta_j S)p(E_i\mid\theta_j)$, and the **risk** $R_j(S)=\langle L\rangle_j=\sum_k p(D_k\mid\theta_j S)L_{kj}$ as expected loss over the sampling distribution. Jaynes regards Wald's strategy/admissibility detour as 'long, difficult, and unnecessary', but credits Wald's framework with giving a fundamental justification to Bernoulli's and Laplace's intuitive ideas. The decision rule is invariant under any proper linear transformation $L'=a+bL$ ($b>0$) of the loss function. Wald's theory does not cover problems where the state of nature tomorrow is influenced by today's decision (a step toward game theory / dynamic programming).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[decision-theory-foundations]] — specializes: Wald's framework is one formalization of the general decision-theory framework.
- [[expected-loss]] — uses: Wald's risk is expected loss over the sampling distribution.
[To be populated during integration]