---
aliases: []
also_type: []
applies:
- channel-capacity
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
id: pkis:concept:redundancy-of-natural-language
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch18
tags:
- redundancy
- entropy-of-english
- language-modelling
- constrained-channel
- crosswords
title: Redundancy of Natural Language
understanding: 0
uses:
- entropy
---

## Definition
Natural language carries far less information per character than its alphabet allows: the per-character entropy $H$ of English is well below $\log_2 26 \approx 4.7$ bits, and the **redundancy** $1 - H/\log_2|A|$ is large and positive. Redundancy arises from two sources MacKay isolates: non-uniform letter use (lowering the monogram entropy $H_0$ to $\approx 4.2$ bits) and inter-symbol dependence (only a finite dictionary of words occurs). Modelling 'word-English' as Wenglish — $W$ words all of length $L$ — gives a per-character entropy, spaces included, of
$$H_W \equiv \frac{\log_2 W}{L+1}.$$

### Why it matters
Redundancy is the slack that error-correcting structure (and human readers) exploit, and the quantity compression aims to remove. Bounding it links a linguistic fact to a hard information-theoretic number.

### Crosswords as a redundancy probe
A language with zero redundancy would make any grid of letters a valid crossword; high redundancy makes crosswords nearly impossible. So the empirical fact that many crosswords exist is a *lower bound on the entropy* of word-English. Counting typical valid fillings of an $S$-square grid, the log-count grows with $S$ only if $H_W$ exceeds a threshold set by the word/letter packing fractions $f_w, f_1$:
$$(f_1 - f_w L)H_0 + f_w(L+1)H_W > 0.$$
For type-A (American) grids this needs $H_W > \tfrac12\tfrac{L}{L+1}H_0$; the looser type-B (British) grids need only $\tfrac14\tfrac{L}{L+1}H_0$ — explaining why type-A crosswords lean on obscure words. The crossword grid is itself a two-dimensional constrained channel whose positive capacity is what permits puzzles at all (Shannon 1948).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[channel-capacity]] — applies: A crossword grid is a two-dimensional constrained channel; puzzles exist only if its capacity exceeds zero.
- [[entropy]] — uses: Redundancy is defined as 1 - H/log|A|; the crossword bound is stated in terms of per-character entropy H_W.
[To be populated during integration]