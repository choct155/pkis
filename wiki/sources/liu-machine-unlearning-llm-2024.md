---
id: "pkis:source:liu-machine-unlearning-llm-2024"
aliases: []
title: "Rethinking Machine Unlearning for Large Language Models"
authors: ["Sijia Liu", "Yuanshun Yao", "Jinghan Jia", "Stephen Casper", "Nathalie Baracaldo", "Peter Hase", "Xiaojun Xu", "Yuguang Yao", "Anil Aakash", "Hang Li", "Kush R. Varshney", "Shuai Tang", "Ding Zhao", "Jeffrey Bilmes", "Yang Liu"]
year: 2024
type: paper
domain: [deep-learning, ai-safety]
tags: [llm, model-editing, privacy, knowledge-removal, post-training, neural-networks, right-to-be-forgotten]
source_url: ""
drive_id: "1A31KsAraOwtK6j3TJpeoMn4ju8O0Z2oJ"
drive_path: "PKIS/sources/papers/rethinking-machine-unlearning-llm.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[model-editing]]", "[[selective-forgetting]]", "[[privacy-in-ml]]"]
---

## Summary

*Note: full text extraction was unavailable during ingest. Summary based on title and known publication context.*

This 2024 survey/position paper examines methods for selectively removing specific learned associations from trained large language models after training is complete. The core problem ("machine unlearning") arises from privacy regulations (right-to-be-forgotten), factual correction needs, and safety alignment requirements that demand post-hoc modification of what a model has encoded. The paper surveys approximate unlearning methods (gradient-based, fine-tuning-based), exact unlearning bounds, and evaluation frameworks for verifying that target knowledge has been removed without degrading general model capability. It distinguishes this from ordinary fine-tuning by the requirement for verifiable removal rather than mere suppression.

## Key Knowledge Objects

- [[model-editing]] (technique, high) — post-training modification of specific factual associations in a neural network without full retraining
- [[selective-forgetting]] (concept, high) — the goal of removing a specific piece of learned knowledge from a trained model while preserving everything else
- [[privacy-in-ml]] (concept, moderate) — the set of constraints and techniques governing data privacy in machine learning, including right-to-be-forgotten compliance

## Key Extractions

*Pending full text extraction — entries above reflect the paper's known scope from title and domain context.*

## Connection Candidates

- [[neural-networks]] — uses: the unlearning methods operate on neural network weight spaces
- [[fine-tuning]] — contrasts-with: unlearning requires verifiable removal, not just suppression via fine-tuning
- [[inductive-bias]] — uses: the difficulty of unlearning arises from how distributed representations in LLMs entangle knowledge

## Awaiting Classification

- **model-editing** — could be technique (it is a procedure) or framework (there are multiple sub-methods organized into a system); assigning technique at high confidence with `also_type: framework` as alternative
- **selective-forgetting** — could be concept (a desired property) or problem (a motivating challenge); assigning concept with note
