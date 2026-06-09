---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- bayesian-stats
id: pkis:principle:minimal-model-causation
instantiates:
- occams-razor
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch02
tags:
- minimality
- occams-razor
- inferred-causation
- structure-preference
- falsifiability
- latent-structure
title: Minimal-Model Semantics of Inferred Causation
understanding: 0
uses:
- causal-markov-condition
---

## Definition
A normative, Occam's-razor-based definition of when observational data licenses a causal claim, due to Pearl and Verma. The machinery: a *latent structure* L=<D,O> pairs a causal DAG D over V with an observed subset O; L is *preferred* to L' (L precedes L') iff D' can mimic D over O -- for every parameterization of D there is one of D' giving the same P[O] -- so preference is gauged by *expressive power*, not syntactic size (a structure with more parameters can still be preferred if it constrains the observables more, i.e. is more falsifiable). L is *minimal* in a class if no member is strictly preferred to it, and *consistent* with P-hat if some parameterization of D generates P-hat. The payoff definition (2.3.6): given P-hat, C has a causal influence on E iff a directed path C->E exists in *every* minimal latent structure consistent with P-hat. This is the semantical casting of Occam's razor: theories that overfit the data are ruled out, and a causal arrow is asserted only when no simpler explanation (including a latent common cause) can avoid it. The principle yields the slogan 'No causes in -- No causes out; Occam's razor in -- Some causes out': the Markov/minimality assumptions themselves smuggle in no specific causes, yet they force *some* causal conclusions from pure association. Limits: minimality is a normative guarantee about what is *inferable*, not a promise that the true data-generating structure is itself minimal, and the search over the space of minimal structures may be intractable, which motivates the additional stability assumption.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[causal-markov-condition]] — uses: Minimality is defined over Markovian (and their latent) causal structures.
- [[occams-razor]] — instantiates: Inferred-causation minimality is the semantical casting of Occam's razor.
[To be populated during integration]