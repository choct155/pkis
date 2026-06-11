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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
- computer-vision
- machine-learning
id: pkis:technique:iterated-conditional-modes
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
tags:
- MAP-inference
- image-denoising
- Ising-model
- coordinate-ascent
- MRF
title: Iterated Conditional Modes (ICM)
understanding: 0
---

## Definition
**Iterated Conditional Modes (ICM)** is a coordinate-wise MAP optimisation algorithm for MRFs: initialise all hidden variables $\{x_i\}$, then repeatedly select one node $x_j$ and set
$$x_j \leftarrow \arg\max_{x_j} p(x_j \mid \mathbf{x}_{\{i \neq j\}})$$
keeping all other variables fixed, until convergence (no variable changes).

ICM is a local greedy ascent on the unnormalised joint energy that converges to a **local** maximum of $p(\mathbf{x}|\mathbf{y})$.

### Why it matters
ICM is computationally simple: each update requires only the local clique energies involving $x_j$, making it practical for dense spatial models such as image denoising with Ising-type priors. It is analogous to coordinate ascent in continuous optimisation. Its main limitation is sensitivity to initialisation and convergence to local (not global) maxima. For certain submodular models (e.g., binary pairwise MRFs with submodular potentials), graph-cut algorithms guarantee the global MAP and typically outperform ICM.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]