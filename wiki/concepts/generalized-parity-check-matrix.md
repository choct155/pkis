---
aliases: []
also_type: []
analogous-to:
- factor-graph
applies:
- repeat-accumulate-codes
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
generalizes:
- linear-block-code
id: pkis:concept:generalized-parity-check-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch49
tags:
- sparse-graph-codes
- parity-check-matrix
- code-representation
- puncturing
- normal-graph
- linear-codes
title: Generalized Parity-Check Matrix
understanding: 0
---

## Definition
A **generalized parity-check matrix** is a unified representation that places repetition, convolutional, turbo, low-density parity-check, MN, and repeat-accumulate codes on a common footing. It is a pair $\{A,\mathbf{p}\}$ where $A$ is a binary matrix and $\mathbf{p}$ lists *punctured* (untransmitted) bits. The matrix defines the set of valid vectors $\mathbf{x}$ satisfying
$$A\mathbf{x}=0;$$
the transmitted codeword $\mathbf{t}(\mathbf{x})$ is obtained by puncturing from $\mathbf{x}$ the bits indicated by $\mathbf{p}$.

### State variables
The extra columns of $A$ beyond the transmitted bits correspond to **state variables** — quantities (e.g. the accumulator's internal sums) that constrain the codeword but are not sent. Equivalently, they are bits punctured before transmission. This is what lets an apparently dense, complex code (such as a non-systematic low-density generator-matrix code) retain a sparse, simple description.

### Rate
If $A$ is $L\times M'$, punctures $S$ bits, and transmits $N=L-S$ bits, the effective constraint count is $M = M'-S$, the source-bit count is $K = N-M = L-M'$, and the rate satisfies
$$R = 1-\frac{M}{N} = 1-\frac{M'-S}{L-S}.$$

### Relation to normal graphs
Forney's (2001) **normal graph** restricts variable nodes to degree one or two and uses only equality and parity factor nodes; the generalized parity-check matrix is the matrix counterpart of this graphical view, with diagrammatic shorthands for identity blocks, band-diagonal structure, and random permutations.

### Why it matters
By distinguishing transmitted from state (punctured) bits, this framework reveals that diverse modern codes are all sparse linear constraint systems differing only in their wiring — clarifying constructions like concatenation and intersection, and exposing the simplicity hidden in turbo and RA codes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[factor-graph]] — analogous-to: the generalized parity-check matrix is the matrix counterpart of Forney's normal graph / factor-graph view of a code
- [[repeat-accumulate-codes]] — applies: RA codes have a compact generalized parity-check matrix with band-diagonal accumulator structure and a permutation
- [[linear-block-code]] — generalizes: extends the parity-check matrix with state/punctured columns to represent any sparse-graph linear code
[To be populated during integration]