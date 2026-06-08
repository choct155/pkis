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
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:technique:sum-product-decoding-ldpc
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch47
tags:
- error-correction
- belief-propagation
- message-passing
- iterative-decoding
- ldpc
title: Sum-Product Decoding of LDPC Codes
understanding: 0
---

## Definition
**Sum-product (belief-propagation) decoding** is the practical iterative algorithm for LDPC codes. It runs the sum-product algorithm on the code's Tanner graph to approximate the bitwise posteriors $P(x_n=1\mid \mathbf{z},\mathbf{H})$ for the generic problem 'find $\mathbf{x}$ maximizing $P^*(\mathbf{x}) = P(\mathbf{x})\,\mathbb{1}[\mathbf{H}\mathbf{x}=\mathbf{z}]$'. Two equivalent viewpoints exist: *codeword decoding* ($\mathbf{x}=\mathbf{t}$, $\mathbf{z}=\mathbf{0}$) and *syndrome decoding* ($\mathbf{x}=\mathbf{n}$, $\mathbf{z}=\mathbf{H}\mathbf{r}$); they are isomorphic.

### Horizontal and vertical steps
Messages $q_{mn}^x$ (bit-to-check: probability bit $n$ is $x$ given checks other than $m$) and $r_{mn}^x$ (check-to-bit: probability check $m$ is satisfied with bit $n$ fixed at $x$) are alternately updated. Using differences $\delta q \equiv q^0-q^1$, the check update is the elegant product
$$\delta r_{mn} = (-1)^{z_m}\!\!\prod_{n'\in N(m)\setminus n}\!\! \delta q_{mn'},$$
and the bit update normalizes $q_{mn}^x \propto p_n^x \prod_{m'\in M(n)\setminus m} r_{m'n}^x$. Pseudoposteriors $q_n^x \propto p_n^x \prod_{m\in M(n)} r_{mn}^x$ give a tentative decoding $\hat{\mathbf{x}}$.

### Stop-when-it's-done
Set $\hat{x}_n=1$ if $q_n^1>0.5$ and **halt as soon as $\mathbf{H}\hat{\mathbf{x}}=\mathbf{z}$**; declare a (detected) failure after a maximum iteration count. This cleanly separates detected from undetected errors and saves computation versus running a fixed number of iterations. Cost is about $6Nj$ multiplies per iteration — roughly $120j/R$ operations per decoded bit, independent of blocklength.

### Why it matters
Because the Tanner graph has cycles the algorithm is not exact, but for a good code at an achievable rate the posterior is sharply peaked on one codeword, so loopy belief propagation reliably finds it. This is the engine that lets LDPC codes approach the Shannon limit in practice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]