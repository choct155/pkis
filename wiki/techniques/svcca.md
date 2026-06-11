---
aliases: []
also_type: []
analogous-to:
- partial-least-squares
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- centered-kernel-alignment
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- representation-learning
- linear-algebra
id: pkis:technique:svcca
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- CCA
- representational-similarity
- dimensionality-reduction
- neural-networks
title: Singular Vector CCA (SVCCA)
understanding: 0
uses:
- principal-component-analysis
- singular-value-decomposition
---

## Definition
SVCCA mitigates the curse-of-dimensionality in CCA applied to neural representations by first projecting each representation onto its top-$k$ principal components (retaining, e.g., 99% of variance), then computing canonical correlations on the reduced spaces:

$$\text{SVCCA}(\mathbf{X},\mathbf{Y}) = \text{mean\_CCA}(\mathbf{U}_{:,1:k}^\top, \mathbf{U}'^\top_{:,1:k'})$$

where $\mathbf{U}, \mathbf{U}'$ are the left-singular-vector matrices of the centered representations. The scalar similarity is typically the mean canonical correlation $\bar{\rho}$.

### Why it matters
High-dimensional neural representations have more dimensions than data points, making vanilla CCA degenerate (all correlations equal 1). SVCCA makes the comparison well-posed and focuses similarity on high-variance directions, enabling empirical studies of how representations evolve across training or differ across architectures.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partial-least-squares]] — analogous-to
- [[singular-value-decomposition]] — uses
- [[principal-component-analysis]] — uses: PCA dimensionality reduction precedes CCA in SVCCA
- [[centered-kernel-alignment]] — contrasts-with: Both measure representational similarity but via CCA vs kernel alignment
[To be populated during integration]