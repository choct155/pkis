---
aliases: []
authors: Namgyu Ho, Huzama Ahmad, Woosung Koh, Se-Young Yun, Tal Schuster, Cicero
  Nogueira dos Santos
concepts: []
date_added: '2026-09-06'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:ho-language-2026
source_url: https://arxiv.org/abs/2609.02737
status: unread
tags: []
title: Language Models Can Control Their Own Attention
type: paper
year: 2026
---

## Summary
Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter. If the user asks about a previous detail in a 1M-token conversation, global attention layers must scan the full context to generate each token of the reply. A prominent approach mitigates this cost by pre-selecting relevant tokens via lightweight proxy scores, but this extrinsic scoring still incurs O(N) per step. We take an intrinsic approach motiva

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:bridge-note:bn-20260605-mean-field-approximation-achieves-tractability
- pkis:technique:neural-language-model
- pkis:source:serret-understanding-2026
- pkis:technique:attention-mechanism
- pkis:framework:sequence-to-sequence-model