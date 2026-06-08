---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
id: pkis:problem:blind-source-separation
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch34
tags:
- latent-variables
- ica
- identifiability
- unmixing
- mackay-itila
title: Blind Source Separation
understanding: 0
---

## Definition
Blind source separation (BSS) is the problem of recovering a set of $I$ unobserved source signals $\mathbf{s}$ from $J$ observed mixtures $\mathbf{x}$, given *only* the mixtures and no knowledge of the mixing process:

$$\mathbf{x} = G\mathbf{s} \quad (\text{or } \mathbf{x}=G\mathbf{s}+\mathbf{n}),$$

with $G$ unknown. "Blind" means both the sources and the mixing matrix $G$ must be inferred jointly from data. The classic illustration is the cocktail-party problem: several microphones each record a different superposition of several simultaneous speakers, and the aim is to isolate the individual voices.

### Identifiability and ambiguities
BSS is solvable only up to inherent ambiguities: sources can be recovered only within arbitrary scaling factors and an arbitrary permutation, because rescaling a source while inversely rescaling its column of $G$ leaves $\mathbf{x}$ unchanged. A statistical assumption is needed to break the rotational symmetry — most commonly that the sources are mutually independent and non-Gaussian, or alternatively non-stationary or temporally structured.

### Why it matters
BSS frames a recurring scientific situation — disentangling additively superposed causes (audio, EEG/MEG, fMRI, financial signals, hyperspectral imaging) — and motivates ICA as its workhorse solution. It also clarifies *what* must be assumed: with Gaussian sources and only second-order statistics the problem is fundamentally underdetermined.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]