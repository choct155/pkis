---
aliases: []
also_type: []
analogous-to:
- simulated-annealing
applies:
- energy-barrier-mcmc
- mcmc-mixing-time
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
- machine-learning
- statistics
- probabilistic-inference
id: pkis:technique:tempered-transitions
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
tags:
- tempering
- parallel-tempering
- mcmc
- energy-based-models
- mixing
title: Tempered Transitions
understanding: 0
uses:
- temperature-ebm
---

## Definition
A tempering strategy for MCMC that temporarily raises the temperature of an energy-based model to facilitate inter-mode transitions, then returns to unit temperature:
$$p_\beta(\mathbf{x}) \propto \exp(-\beta E(\mathbf{x})), \quad \beta \in (0, 1] \text{ during transitions}$$

A **tempered transition** move follows a sequence $\beta_1 > \beta_2 > \cdots > \beta_K \approx 0$ (heating) then back up, proposing the final state as the next sample.

### Why it matters
By softening the energy landscape at high temperatures, the chain can traverse low-probability barriers between modes, then sharpen the distribution again to produce a valid sample from $p_1$. The technique addresses the fundamental slow-mixing problem of MCMC in multimodal distributions.

### Parallel tempering
A related technique runs chains at many temperatures simultaneously and proposes swaps between adjacent temperature levels, allowing low-temperature chains to inherit the fast mixing of high-temperature chains.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc-mixing-time]] — applies: tempering reduces effective mixing time for multimodal distributions
- [[simulated-annealing]] — analogous-to: both use a cooling schedule; tempered transitions return to unit temperature
- [[energy-barrier-mcmc]] — applies: designed to overcome energy barriers between modes
- [[temperature-ebm]] — uses: temporarily raises temperature to cross energy barriers
[To be populated during integration]