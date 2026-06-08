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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:result:zipf-mandelbrot-law
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch18
tags:
- zipfs-law
- power-law
- word-frequency
- language-modelling
- monogram-model
title: Zipf–Mandelbrot Law
understanding: 0
uses:
- redundancy-of-natural-language
---

## Definition
An empirical regularity of monogram language statistics: the probability of the $r$-th most frequent word falls off as a power of its rank. **Zipf's law** (1949) states
$$P(r) = \frac{\kappa}{r^{\alpha}},\qquad \alpha \approx 1,$$
so a log–log plot of frequency versus rank is approximately a straight line of slope $-\alpha$. **Mandelbrot's** modification adds a shift parameter $v$ that bends the head of the curve:
$$P(r) = \frac{\kappa}{(r+v)^{\alpha}}.$$

### Why it matters
The law constrains any generative monogram model of language: a credible model must reproduce the observed rank–frequency curve and the unbounded growth of vocabulary with corpus size. It motivates exchangeable, vocabulary-growing priors (e.g. Dirichlet-process-style models) over naive fixed-alphabet sources.

### Generating the slope
A plain Dirichlet process does *not* reproduce Zipf curves. MacKay's tweak does: run a Dirichlet process over elementary *characters* (small concentration $\alpha$ giving $\approx 27$ frequent symbols), nominate one as the space, and read off the inter-space strings as 'words'. The resulting word frequencies trace clean Zipf plots, and the chosen space character's probability sets the slope — a rarer space yields a richer vocabulary and shallower slope.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[redundancy-of-natural-language]] — uses: The power-law rank-frequency curve is a quantitative signature of the monogram-level structure that gives language its redundancy.
[To be populated during integration]