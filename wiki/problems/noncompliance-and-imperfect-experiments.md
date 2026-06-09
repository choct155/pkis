---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
contrasts-with:
- local-average-treatment-effect
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
id: pkis:problem:noncompliance-and-imperfect-experiments
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch08
tags:
- noncompliance
- imperfect-compliance
- indirect-experiment
- intent-to-treat
- encouragement-design
- randomized-trial
- self-selection
title: Noncompliance and Imperfect Experiments
understanding: 0
uses:
- instrumental-variables
- average-treatment-effect
---

## Definition
An *imperfect experiment* deviates from the ideal randomized-control protocol: subjects are randomly *assigned* (Z) to a program but are merely *encouraged* rather than forced to take it, so the treatment actually received (X) is self-selected and the assignment Z acts only as an instrument. This is the canonical *noncompliance* setting -- a randomized clinical trial in which patients with adverse reactions reduce dosage, or controls obtain the drug elsewhere. Randomization is questioned on three grounds: perfect control is hard to ascertain, denying controls the best treatment raises ethical/legal issues (e.g. AIDS placebo arms), and randomization itself can change participation and behavior (Heckman 1992).

The core difficulty: because the same unobserved factors U drive both treatment choice X and response Y (U->X, U->Y), naively comparing the treated and untreated fractions is biased, and the treatment effect P(y|do(x)) is *nonidentifiable* even with infinite samples and complete records (Pearl, Section 3.5). Two common but flawed fixes are critiqued: (1) **intent-to-treat (ITT)** analysis compares groups by *assignment* regardless of treatment received -- it measures how assignment, not the treatment itself, affects the outcome, and is only valid when experimental incentives mimic field incentives (it can credit recovery to a drug when subjects actually recovered by *avoiding* it); (2) the **instrumental-variable correction** (ITT divided by the compliance fraction; Angrist et al. 1996) is valid only for the LATE subpopulation of responsive compliers, which is unidentifiable and instrument-dependent, so it cannot ground policy over the whole population. The chapter's resolution is to seek the *stable, instrument-independent* aspect of the treatment via assumption-free bounds.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[average-treatment-effect]] — uses: ACE/ETT are the estimands of interest under noncompliance
- [[local-average-treatment-effect]] — contrasts-with: LATE/IV-correction targets unstable instrument-dependent compliers; Pearl seeks instrument-independent population bounds
- [[instrumental-variables]] — uses: the randomized assignment is treated as an instrument encouraging treatment
[To be populated during integration]