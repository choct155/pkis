---
aliases: []
also_type: []
analogous-to:
- noisy-channel-coding-theorem
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
extends:
- sqrt-g-advantage-of-sex
id: pkis:result:maximum-tolerable-mutation-rate
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch19
tags:
- evolution
- error-correction
- mutation-rate
- error-threshold
- genome-size
title: Maximum Tolerable Mutation Rate and Genome Size
understanding: 0
---

## Definition
Viewing the species as an **error-correcting system**, MacKay asks how much mutation a genome can withstand before deleterious flips outrun selection. For an asexual species, fitness can increase only if
$$m < \frac{1}{G}\frac{1}{(2\delta f)^2},$$
i.e. the tolerable mutation rate is pinned near $1/G$. A non-sexual mother cannot escape this by larger litters: since the chance a child suffers no flip is $\approx e^{-mG}$, she would need $\sim e^{mG}$ offspring — exponential in $mG$.

With **sex**, the bound is far more generous,
$$m < \eta\sqrt{\frac{f(1-f)}{G}},$$
of order $1/\sqrt{G}$ — a factor $\sim\sqrt{G}$ larger. Inverting, the **largest sustainable genome** for fixed per-nucleotide rate $m$ is $\sim 1/m$ for parthenogens but $\sim 1/m^2$ for sexual species. With $m\approx 10^{-8}$ and brood size $\sim 2\times10^4$, MacKay predicts every species with $G > 10^9$ coding nucleotides must use recombination.

### Why it matters
This is the population-genetics analogue of an **error threshold**: just as a code fails above a critical noise level, a genome 'melts' above a critical mutation rate. The same redundancy/recombination that protects codewords protects genomes, making the species-as-error-correcting-code analogy quantitative and predictive.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[noisy-channel-coding-theorem]] — analogous-to: The error-threshold view treats the genome as a code over a mutation channel; tolerable mutation rate plays the role of a capacity-like noise limit.
- [[sqrt-g-advantage-of-sex]] — extends: The same √G factor that speeds sexual learning also raises the tolerable mutation rate and the sustainable genome size.
[To be populated during integration]