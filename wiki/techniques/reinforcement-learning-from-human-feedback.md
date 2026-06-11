---
aliases: []
also_type: []
analogous-to:
- inverse-reinforcement-learning
applies:
- value-alignment-problem
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
- reinforcement-learning
- natural-language-processing
- ai-alignment
extends:
- gpt-pretraining
id: pkis:technique:reinforcement-learning-from-human-feedback
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- RLHF
- alignment
- PPO
- reward-model
- InstructGPT
- ChatGPT
- fine-tuning
title: Reinforcement Learning from Human Feedback (RLHF)
understanding: 0
uses:
- reinforcement-learning
---

## Definition
RLHF fine-tunes a pre-trained language model using reinforcement learning so that its outputs better align with human preferences. The pipeline has three stages:
1. **Supervised fine-tuning (SFT)**: train on human-written demonstrations.
2. **Reward model training**: fit a reward model $r_\phi(x, y)$ on human pairwise preference rankings of model outputs.
3. **RL fine-tuning**: optimise the language model policy $\pi_\theta$ with PPO to maximise expected reward, subject to a KL penalty against the SFT model:
$$\mathcal{J}(\theta) = \mathbb{E}_{y \sim \pi_\theta}[r_\phi(x,y)] - \beta\, D_{\text{KL}}(\pi_\theta \| \pi_{\text{SFT}}).$$

### Why it matters
RLHF (introduced in InstructGPT / ChatGPT) is the dominant technique for aligning LLM outputs to human intent, reducing harmful or unhelpful responses. It operationalises the value-alignment problem for language models and connects language generation with reward-based RL fine-tuning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inverse-reinforcement-learning]] — analogous-to: Both infer a reward from human behaviour/preferences
- [[value-alignment-problem]] — applies: RLHF operationalises value alignment for LLMs
- [[reinforcement-learning]] — uses
- [[gpt-pretraining]] — extends: RLHF fine-tunes a GPT-style pre-trained model
[To be populated during integration]