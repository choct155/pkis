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
- statistical-learning
id: pkis:result:rate-of-information-acquisition-mutation
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch19
tags:
- evolution
- mutation
- truncation-selection
- asexual-reproduction
- maynard-smith
title: Rate of Information Acquisition Under Mutation (≈1 bit/generation)
understanding: 0
---

## Definition
For an **asexual** population in which variation comes only from mutations (each bit flipped with probability $m$) followed by truncation selection of the fittest $N$ children, MacKay derives the rate of fitness increase. Mutation lowers the mean excess fitness ($\overline{\delta f}_{\text{child}} = (1-2m)\delta f$) but adds variance $\sim m/G$; selection then keeps the upper tail. In dynamic equilibrium of the variance the net rate is
$$\frac{df}{dt} \approx -2m\,\delta f + \sqrt{\frac{m}{G}},$$
maximized at $m_{\text{opt}} = 1/(16G(\delta f)^2)$, giving
$$\left(\frac{dF}{dt}\right)_{\text{opt}} = \frac{1}{8\,\delta f}\ \text{bits per generation}.$$

### Consequence
For a fit population ($\delta f > 0.125$) this is **less than one fitness unit per generation**, vindicating John Maynard Smith's estimate of order 1 bit acquired per generation, independent of population size $N$ — a larger population merely corrects the same defects more often. Only a low-fitness population ($\delta f \lesssim 1/\sqrt{G}$) can briefly gain at rate $\sim\sqrt{G}$, and that spurt lasts only $\sim\sqrt{G}$ generations.

### Why it matters
This is the baseline against which sex is judged: it shows mutation-only evolution is information-starved, learning only ~1 bit/generation no matter how big the population, far too slow to plausibly account for the ape–human genomic gap.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]