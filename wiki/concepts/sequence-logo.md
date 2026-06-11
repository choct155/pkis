---
aliases: []
also_type: []
applies:
- entropy
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
- information-theory
- bioinformatics
id: pkis:concept:sequence-logo
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
tags:
- entropy
- DNA
- visualisation
- bioinformatics
- sequence-motif
title: Sequence Logo
understanding: 0
uses:
- binary-entropy-function
---

## Definition
A graphical representation of a DNA (or protein) sequence motif in which each column $t$ has total height $R_t = \log_2(4) - \mathbb{H}(\hat{\theta}_t)$ bits (for a nucleotide alphabet), and within each column the height of letter $k$ is proportional to $\hat{\theta}_{tk} \cdot R_t$.

The column height encodes the information content (conservation) at each position: a perfectly conserved column has height 2 bits; a uniform column has height 0.

### Why it matters
Sequence logos make evolutionary conservation immediately visible: tall, narrow columns identify positions critical to gene function (e.g., transcription-factor binding sites), while short columns indicate variable, less functionally constrained positions. The construction directly instantiates entropy as a measure of uncertainty in biological sequence data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[binary-entropy-function]] — uses
- [[entropy]] — applies
[To be populated during integration]