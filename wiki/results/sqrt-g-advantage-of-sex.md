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
id: pkis:result:sqrt-g-advantage-of-sex
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch19
tags:
- evolution
- recombination
- sexual-reproduction
- crossover
- deterministic-mutation-hypothesis
title: The √G Advantage of Sexual Reproduction
understanding: 0
---

## Definition
Under **recombination** (sex), a child's bits are drawn locus-by-locus from one of two parents. Crucially, the children's mean fitness *equals* the parents' fitness — recombination produces variation **without** the average-fitness deficit that mutation incurs. Assuming rapid gene-pool mixing and homogeneity (fraction $f$ good at every locus), the child fitness is
$$F_{\text{child}} \sim \mathrm{Normal}\!\left(fG,\ \tfrac{1}{2}f(1-f)G\right),$$
so its standard deviation scales as $\sqrt{Gf(1-f)}$. Since truncation selection raises mean fitness by an amount proportional to this spread, the fitness gain per generation scales as the **square root of the genome size**:
$$\frac{d\bar{F}}{dt} \approx \eta\sqrt{f(t)(1-f(t))\,G}, \qquad \eta \equiv \sqrt{\tfrac{2}{\pi+2}}\approx 0.62.$$
Integrating gives $f(t)=\tfrac{1}{2}[1+\sin(\tfrac{\eta}{\sqrt G}(t+c))]$, reaching perfection in $(\pi/\eta)\sqrt{G}$ generations.

### Why it matters
A sexual species acquires information from selection $\sim\sqrt{G}$ times faster than an asexual one ($\sim\sqrt{G}\approx 10^4$ for $G\approx10^8$). This is Kondrashov's 'deterministic mutation hypothesis' answer to *why have sex?* — recombination lets good mutations spread and bad ones be purged in parallel, decisively outweighing the 'cost of males' for large genomes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]