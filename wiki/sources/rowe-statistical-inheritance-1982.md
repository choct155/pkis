---
title: "Inheritance of Statistical Properties"
authors: "Neil C. Rowe"
year: 1982
type: paper
domain: [knowledge-representation, bayesian-stats]
tags: [statistics, default-reasoning, expert-systems, production-systems]
source_url: ""
drive_id: "1gtWxuFYDpggXTqe141_ODHkWNOH5GopZ"
drive_path: "PKIS/sources/papers/Inheritance of Statistical Properties.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[statistical-inheritance]]", "[[default-reasoning]]"]
---

## Summary

Presented at AAAI-82, this short Stanford paper by Neil Rowe addresses a rarely examined question: do statistical aggregate properties (mean, maximum, mode, standard deviation) "inherit" from a set to its subsets in the way that nominal properties do? Rowe argues they do, but only in a weaker sense: rather than inheriting exact values, the four-tuple of (upper bound, lower bound, best estimate, standard deviation of possibilities) often inherits with high reliability.

For example, the best estimate of a subset's mean is the parent set's mean (in the absence of further information), and the standard deviation of that estimate is approximately σ_set · √(1/n_subset − 1/n_set). This "weak inheritance" is useful for answering approximate statistical queries over large databases without recomputing from raw data.

Rowe identifies six types of statistical inheritance: downward (set to subset), upward (subset to set, via disjoint union or sampling), lateral (between siblings with common parent), diagonal (combining downward and lateral to estimate unknown sibling from known siblings), intra-concept (between different statistics on the same set, e.g., mean estimated from max and min), and value-description-level (between different levels of detail). A production-system architecture is proposed for combining results from multiple inference paths, using interval intersection for ranges and the classical formula for combining independent normal estimates. The system was implemented as part of the KBMS project at Stanford.

## Key Knowledge Objects

- [[statistical-inheritance]] (concept, moderate — could be technique) — the propagation of approximate statistical aggregate properties (mean, maximum, etc.) from parent sets to subsets via a four-characteristic characterization (bounds, estimate, uncertainty)
- [[default-reasoning]] (concept, high) — inference from absence of explicit information using a closed-world assumption; Rowe invokes it to handle the combinatorial explosion of possible subsets

## Key Extractions

1. **Four-characteristic representation**: Each inherited statistical property is characterized by: an upper bound, a lower bound, a best estimate, and a standard deviation of possibilities for the estimate — enabling "weak inheritance" without requiring exact value propagation.

2. **Best estimate rule**: "A best estimate of the mean of a subset, in the absence of further information, is the mean of the set." The corresponding uncertainty is σ_subset ≈ σ_set · √(1/n_subset − 1/n_set).

3. **Six inheritance directions**: downward (set→subset), upward (subset→set via union/sampling), lateral (between siblings), diagonal (downward + lateral hybrid), intra-concept (between statistics on same set), and value-description-level (between levels of detail).

4. **Closed-world default reasoning**: "the idea that 'sufficiently important' sets whose statistics are not explicitly noted must be not 'unusual' in regard to those statistics." The CWA allows the system to infer approximate values without exhaustive lookup.

5. **Architecture**: Production-rule system with "weakest-first" inference; ranges intersected for cumulative range, normal-independence assumption for combining estimates from different inference paths (yields standard deviation at most 70% of what it would be without independence assumption).

## Connection Candidates

- [[directed-graphical-models]] — contrasts-with: DGMs encode conditional independence among random variables in a DAG; statistical inheritance encodes cruder set-subset statistical propagation without full probabilistic structure
- [[default-reasoning]] — uses: the system invokes CWA-style defaults when no explicit information is available for a subset
- [[probability-theory]] — uses: interval arithmetic and normal combination formulas underpin the merging of multiple inheritance paths

## Awaiting Classification

- **statistical-inheritance** — candidate types: concept or technique
  - Case for concept: it's an idea with a definition (weak inheritance of statistical aggregates via four-characteristic representation)
  - Case for technique: the production-rule implementation is a procedure for answering approximate statistical queries
  - What makes this hard: the paper introduces both the concept and a technique instantiating it; the concept is more primary here
