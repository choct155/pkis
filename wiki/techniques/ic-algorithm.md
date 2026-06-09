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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- statistical-learning
id: pkis:technique:ic-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch02
tags:
- constraint-based
- structure-learning
- pattern
- pc-algorithm
- verma-pearl
title: IC Algorithm (Inductive Causation)
understanding: 0
---

## Definition
A constraint-based causal-discovery algorithm (Verma and Pearl 1990) that takes a stable distribution P-hat over variables V and outputs a *pattern* -- a partially directed DAG representing the Markov-equivalence class of the underlying DAG D0. Three steps: (1) for each pair a,b search for a separating set S_ab with (a indep b | S_ab); connect a,b by an undirected edge iff no such set exists (yielding the skeleton); (2) for each nonadjacent pair a,b with common neighbor c, if c is NOT in S_ab orient the v-structure a->c<-b (collider detection); (3) propagate orientations by rules that avoid creating new v-structures or directed cycles -- Verma-Pearl's four rules R1-R4, shown sufficient by Meek (1995), produce a maximally oriented pattern. Steps 1 and 3 are underspecified; the PC refinement (Spirtes-Glymour 1991) searches separating sets by increasing cardinality starting from a complete graph and limits the search to adjacent nodes, achieving polynomial time in bounded-degree graphs. The IC* variant handles latent variables: it returns a *marked pattern* with four edge types -- marked arrow (genuine directed path), unmarked arrow (directed path OR latent common cause), bidirected edge (latent common cause / spurious), and undirected edge (undetermined) -- using rules that add arrowheads to individual endpoints rather than orienting whole edges. IC* carries a one-sided guarantee: it never marks a->b genuine unless a truly causally influences b, provided the distribution is stable relative to its causal model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]