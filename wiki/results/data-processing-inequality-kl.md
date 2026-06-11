---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- information-theory
- statistics
id: pkis:result:data-processing-inequality-kl
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
specializes:
- data-processing-inequality
tags:
- kl-divergence
- data-processing-inequality
- monotonicity
- channel
- jensen-inequality
title: Data Processing Inequality (KL form)
understanding: 0
uses:
- kl-divergence
- information-inequality
- jensens-inequality
---

## Definition
Let $p(x)$ and $q(x)$ be two distributions and $t(y|x)$ a stochastic channel. Let $p(y) = \int t(y|x)p(x)dx$ and $q(y) = \int t(y|x)q(x)dx$ be the output distributions. Then:

$$D_{\mathrm{KL}}(p(x) \| q(x)) \geq D_{\mathrm{KL}}(p(y) \| q(y))$$

As a corollary (monotonicity under marginalization):

$$D_{\mathrm{KL}}(p(x,y) \| q(x,y)) \geq D_{\mathrm{KL}}(p(x) \| q(x))$$

The proof applies Jensen's inequality to the concave log function.

### Why it matters
This result formalizes the intuition that processing or partial observation can only reduce — never increase — the distinguishability of two distributions. It is the KL-domain counterpart of the mutual-information DPI for Markov chains, and implies that no deterministic or stochastic post-processing of data can increase statistical information.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[jensens-inequality]] — uses
- [[information-inequality]] — uses
- [[data-processing-inequality]] — specializes: KL-domain version of the general DPI for mutual information
- [[kl-divergence]] — uses
[To be populated during integration]