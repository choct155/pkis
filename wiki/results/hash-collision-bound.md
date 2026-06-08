---
aliases: []
also_type: []
applies:
- hash-table
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
- computer-science
id: pkis:result:hash-collision-bound
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch12
tags:
- collisions
- birthday-problem
- hashing
- scaling
- mackay-itila
title: Hash Collision Bound (Birthday Problem)
understanding: 0
---

## Definition
For an ideal random hash function with output alphabet size $T = 2^M$, the probability that a particular pair of the $S$ stored keys collides is $1/T$, and there are $\binom{S}{2}$ pairs, so the **expected number of pairwise collisions** is exactly
$$\mathbb{E}[\text{collisions}] = \frac{S(S-1)}{2T}.$$

### Two scaling regimes
Requiring the expected number of collisions to be below 1 gives
$$T > \tfrac{1}{2}S(S-1) \quad\Longrightarrow\quad M > 2\log_2 S,$$
so a *collision-free* table needs $T \sim S^2$ — **twice** as many bits as the $\log_2 S$ that would merely name each entry uniquely. If instead we tolerate collisions involving a fraction $f$ of the keys, then $T > S/f$, i.e.
$$M > \log_2 S + \log_2(1/f),$$
so for $f \approx 1\%$ only about 7 extra bits are needed and $T \sim S$ suffices.

### Why it matters
This is the **birthday problem** in disguise (cf. the $\sqrt{\,}$ scaling of $2^{M/2}$ in collision attacks): collisions appear far sooner than naive intuition suggests, scaling with $S^2$ rather than $S$. The bound dictates how big a hash you must choose — for clean retrieval ($T\sim S^2$), for cheap retrieval with rare collisions ($T\sim S$), and, as the same arithmetic shows for cryptographic hashing, why a forger seeking *any* matching pair needs only $\sim 2^{M/2}$ trials.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hash-table]] — applies: The collision bound dictates the table size M needed for collision-free or low-collision operation.
[To be populated during integration]