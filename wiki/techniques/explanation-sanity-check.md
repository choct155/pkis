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
- machine-learning
- interpretability
id: pkis:technique:explanation-sanity-check
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
tags:
- sanity-check
- faithfulness
- evaluation
- interpretability
- adversarial
title: Explanation Property Sanity Check
understanding: 0
---

## Definition
An **explanation sanity check** is an empirical or formal test of the form:
$$\text{If explanation } E \text{ is faithful, phenomenon } X \text{ should not occur.}$$
If a test construction succeeds in producing $X$, the explanation method fails the check.

Two canonical instantiations:
1. **Randomization test** [Adebayo et al. 2018]: Compare $E(f_\text{trained}, x)$ vs. $E(f_\text{random}, x)$ where $f_\text{random}$ has randomly-initialized (or randomly-permuted) weights. A faithful explanation must change significantly; methods that produce similar saliency maps for both fail.
2. **Input-transformation invariance test** [Kindermans et al. 2019]: Apply a constant shift $x \mapsto x + c$ that does not affect model weights or predictions. A faithful, stable explanation should be invariant; gradient × input methods fail this check.

### Why it matters
Sanity checks provide cheap, scalable pre-screening before expensive user studies. They can reveal systematic failure modes (e.g., an explanation that is a function of the input distribution rather than the model). However, passing a sanity check is necessary but not sufficient for a good explanation—it only rules out specific failure modes and cannot certify positive fidelity properties.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]