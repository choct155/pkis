---
aliases: []
also_type: []
analogous-to:
- partial-dependence
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- human-ai-collaboration-failure
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- interpretability
id: pkis:concept:concept-bottleneck-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
specializes:
- inherently-interpretable-model
tags:
- concept-bottleneck
- interpretability
- human-AI-collaboration
- test-time-intervention
title: Concept Bottleneck Model
understanding: 0
uses:
- neural-networks
---

## Definition
A **concept bottleneck model** (CBM) is a two-stage architecture:
$$x \xrightarrow{h} c \xrightarrow{g} y$$
where $h: \mathcal{X} \to \mathcal{C}$ maps raw inputs to a vector of human-interpretable concept activations $c \in [0,1]^K$, and $g: \mathcal{C} \to \mathcal{Y}$ maps concepts to predictions. Both stages are trained jointly (or sequentially) with concept-level supervision.

The bottleneck enforces that $Y \perp\!\!\!\perp X \mid C$: all predictive information must pass through the interpretable concept layer.

### Why it matters
CBMs enable *test-time concept intervention*: a clinician who knows that a patient no longer has insomnia can set $c_{\text{insomnia}} = 0$ and re-run $g$ to obtain updated recommendations without retraining. This supports human+ML collaboration and provides a modular, auditable prediction pipeline. Key challenges: (1) obtaining concept-level annotations is expensive; (2) if concepts do not capture all relevant information, a residual information leak may reduce accuracy; (3) learned concept representations may not perfectly align with human semantic understanding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partial-dependence]] — analogous-to: Both expose intermediate model behavior with respect to interpretable summaries of input influence.
- [[human-ai-collaboration-failure]] — contrasts-with: Test-time concept intervention supports effective human+AI teaming.
- [[neural-networks]] — uses
- [[inherently-interpretable-model]] — specializes: The g: C -> Y stage is interpretable; concept bottlenecks combine deep feature extraction with an interpretable decision layer.
[To be populated during integration]