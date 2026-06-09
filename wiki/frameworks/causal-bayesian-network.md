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
- causal-analysis
id: pkis:framework:causal-bayesian-network
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- do-calculus
related_concepts: []
sources:
- pearl-causality-ch01
specializes:
- bayesian-networks
tags:
- causality
- dag
- interventions
- do-operator
- bayesian-networks
- truncated-factorization
title: Causal Bayesian Network
understanding: 0
uses:
- intervention-do-operator
- d-separation
---

## Definition
A DAG $G$ over variables $V$ that economically encodes not just one joint distribution but the entire space $\mathbf{P}_*$ of interventional distributions $P_x(v)$ produced by every possible intervention $\mathrm{do}(X=x)$.

A one-line intuition: an ordinary Bayesian network tells you only how the world looks; a causal Bayesian network also tells you how the world would look if you reached in and set some variables by force.

### Formal statement
$G$ is a causal Bayesian network compatible with $\mathbf{P}_*$ iff for every $P_x \in \mathbf{P}_*$: (i) $P_x(v)$ is Markov relative to $G$; (ii) $P_x(v_i)=1$ for $V_i \in X$ consistent with $X=x$ (the intervention takes hold); and (iii) $P_x(v_i \mid pa_i)=P(v_i \mid pa_i)$ for $V_i \notin X$ (every untouched mechanism is invariant). These conditions yield, and follow from, the **truncated factorization**
$$P_x(y) = \prod_{\{i \,\mid\, V_i \notin X\}} P(y_i \mid pa_i),$$
obtained by deleting from the chain-rule product exactly the factors $P(x_i \mid pa_i)$ for intervened variables.

### Seeing vs. doing
The effect of an observation $X_3=\text{On}$ is ordinary conditioning $P(\cdot \mid X_3=\text{On})$; the effect of the action $\mathrm{do}(X_3=\text{On})$ is conditioning on a *mutilated* graph with the arrows into $X_3$ removed. Observing the sprinkler on lets you infer it is probably a dry season; forcing it on licenses no such inference.

### Why it matters
This is the bridge from association to causation: it shows that a single graph plus the pre-intervention conditionals $P(v_i \mid pa_i)$ suffices to answer the combinatorially vast family of "what if we intervene" questions, provided each parent–child link is treated as an autonomous, locally modifiable mechanism. It is the object on which the do-calculus and identification theory are built.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[do-calculus]] — prerequisite-of
- [[d-separation]] — uses
- [[intervention-do-operator]] — uses
- [[bayesian-networks]] — specializes
[To be populated during integration]