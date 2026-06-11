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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- speech-processing
- bioinformatics
id: pkis:concept:hierarchical-hmm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
tags:
- HMM
- hierarchical
- speech-recognition
- plan-recognition
title: Hierarchical HMM (HHMM)
understanding: 0
---

## Definition
An HMM generalization with multiple levels of abstraction $\ell = 1, \ldots, L$, where $Z_t^\ell$ denotes the state at time $t$ and level $\ell$. A transition at level $\ell$ is only permitted when the lower-level chain $\ell - 1$ has completed (entered its end state), as controlled by a finish variable $F_t^{\ell-1}$. This nesting enforces that higher-level chains evolve more slowly:

$$p(Z_t^\ell \mid Z_{t-1}^\ell, F_t^{\ell-1})$$

An HHMM can always be flattened to a standard HMM but benefits from $O(T)$ inference (vs $O(T^3)$ for SCFGs) while still capturing hierarchical structure.

### Why it matters
HHMMs model domains with natural hierarchical decomposition — speech (phonemes → words → sentences), genes, plans, and activities — with an exponentially more compact representation than a flat HMM, and much faster inference than stochastic context-free grammars.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]