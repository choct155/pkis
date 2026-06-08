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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:maximum-entropy-image-reconstruction
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch46
tags:
- maximum-entropy
- deconvolution
- image-reconstruction
- entropic-prior
- positivity
- astronomy
title: Maximum-Entropy Image Reconstruction
understanding: 0
---

## Definition
Maximum-entropy (MaxEnt) image reconstruction (Gull & Daniell, 1978) replaces the Gaussian image prior of the optimal linear filter with an *entropic prior* that enforces positivity of pixel intensities. The 'classic' MaxEnt model assigns
$$P(\mathbf{f}\mid\alpha,\mathbf{m},H) \propto \exp\big(\alpha\, S(\mathbf{f},\mathbf{m})\big),\qquad S(\mathbf{f},\mathbf{m}) = \sum_i \big(f_i\ln(m_i/f_i) + f_i - m_i\big),$$
where $\mathbf{m}$ is a default image and $\alpha$ sets the dynamic range by which pixels may deviate from it.

### Why positivity matters
The Gaussian prior is badly mismatched to real images: it permits negative pixels. Applied to astronomical data, optimal linear filters yield reconstructions with negative-flux regions, i.e. patches of sky that *suck energy out of telescopes*. The entropic prior, supported only on $f_i>0$, eliminates these spurious negative areas and their complementary positive artefacts, dramatically improving reconstruction quality, especially for high-contrast images with large dark regions.

### Correlated extensions
The intrinsic-correlation-function MaxEnt model (Gull, 1989) injects spatial correlation by writing $\mathbf{f}=\mathbf{G}\mathbf{h}$, with $\mathbf{G}$ a smoothing convolution and a classic MaxEnt prior on the hidden image $\mathbf{h}$.

### Why it matters
It is a flagship demonstration of MacKay's thesis that *the better the prior matches the world, the better the inference and the less data needed*. Improving the image model, not the algorithm, is what delivered the breakthrough.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]