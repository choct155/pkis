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
id: pkis:concept:low-density-parity-check-code
instantiates:
- noisy-channel-coding-theorem
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch47
specializes:
- linear-block-code
tags:
- error-correction
- linear-codes
- gallager-codes
- sparse-graph-codes
- channel-coding
title: Low-Density Parity-Check Code (Gallager Code)
understanding: 0
uses:
- tanner-graph
---

## Definition
A **low-density parity-check (LDPC) code**, or **Gallager code**, is a linear block code defined by a parity-check matrix $\mathbf{H}$ that is *sparse*: every row and every column contains only a few 1s. Codewords are the binary vectors $\mathbf{t}$ satisfying
$$\mathbf{H}\mathbf{t} = \mathbf{0} \pmod 2.$$
A **regular** $(j,k)$ Gallager code has exactly $j$ ones in every column and $k$ in every row, constructed at random subject to those constraints; each transmitted bit then participates in $j$ parity checks and each check ties together $k$ bits.

### Why the sparsity matters
Sparsity is not a property of the *code* (a fixed subspace) but of the chosen $\mathbf{H}$ — and it is exactly what makes practical decoding possible. Because each check couples only $k \ll N$ bits, the associated graph is locally tree-like, so message-passing decoders run in time linear in $N$. By contrast, a generic random linear code provably *cannot* be given a low-density $\mathbf{H}$ (a pigeonhole counting argument: there are far fewer sparse matrices than distinct codes).

### Goodness
LDPC codes are simultaneously simple to construct and theoretically excellent. Under an optimal decoder they are *good* codes with *good distance* for any column weight $j \ge 3$ (Gallager 1963; MacKay 1999), and suitable sequences are *very good* — approaching the Shannon limit. The optimal decoder is intractable (decoding is NP-complete), but sparsity rescues us by enabling near-optimal iterative decoding.

### Why it matters
Gallager invented these codes in 1962; they were forgotten for thirty years, then rediscovered in the 1990s and shown to come within a fraction of a decibel of channel capacity. They are now deployed everywhere from hard drives to satellite and wireless standards, and constitute one of the central practical realizations of Shannon's promise.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[noisy-channel-coding-theorem]] — instantiates: LDPC codes are a practical, capacity-approaching realization of Shannon's noisy-channel coding theorem.
- [[tanner-graph]] — uses: An LDPC code's sparse H is naturally represented as a sparse bipartite Tanner graph.
- [[linear-block-code]] — specializes: An LDPC code is a linear block code whose parity-check matrix H is sparse.
[To be populated during integration]