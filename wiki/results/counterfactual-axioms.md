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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
id: pkis:result:counterfactual-axioms
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch07
tags:
- counterfactuals
- structural-causal-models
- potential-outcomes
- identifiability
- causality
title: 'Counterfactual Axioms: Composition, Effectiveness, Reversibility'
understanding: 0
---

## Definition
Three properties of the potential-response function $Y_x(u)$ that are **sound and complete** for structural-model semantics (Galles and Pearl 1997/1998; Halpern 1998): every truth about counterfactuals in causal models follows from them.

**Composition.** $\;W_x(u)=w \Rightarrow Y_{xw}(u) = Y_x(u)$—forcing a variable to the value it would have taken anyway changes nothing. Yields the **consistency rule** $X(u)=x \Rightarrow Y(u)=Y_x(u)$ (Robins 1987).

**Effectiveness.** $\;X_{xw}(u)=x$—intervening to set $X=x$ does make $X$ equal $x$.

**Reversibility.** $\;(Y_{xw}(u)=y)\,\&\,(W_{xy}(u)=w) \Rightarrow Y_x(u)=y$—rules out multiple feedback solutions; trivial in recursive systems where it follows from composition.

*Intuition:* these are the algebraic "laws of motion" for counterfactual subscripts, letting one manipulate $Y_x$ symbolically the way one manipulates probabilities.

### Soundness and completeness
**Soundness** (Theorem 7.3.3): all three hold in every causal model. **Completeness** (Theorems 7.3.5–7.3.6): for recursive models, composition + effectiveness + recursiveness suffice; for general models, composition + effectiveness + reversibility suffice.

### Why it matters
This is the bridge between identification and symbolic algebra. **Soundness** means: if you reduce a counterfactual quantity $Q$ to a counterfactual-free probability expression using these axioms, $Q$ is identifiable. **Completeness** means the converse: failure to reduce certifies non-identifiability. The smoking–tar–cancer front-door formula is re-derived purely by composition and effectiveness. The axioms also establish the formal equivalence of structural models and the Neyman–Rubin potential-outcome framework—supplying the semantics the latter takes as primitive.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]