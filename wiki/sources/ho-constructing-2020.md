---
aliases: []
authors: Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, Akiko Aizawa
concepts: []
date_added: '2026-06-07'
doi: ''
domain: []
drive_id: ''
drive_path: ''
id: pkis:source:ho-constructing-2020
source_url: https://aclanthology.org/2020.coling-main.580/
status: unread
tags: []
title: Constructing A Multi-hop QA Dataset for Comprehensive Evaluation of Reasoning
  Steps (2WikiMultiHopQA)
type: paper
year: 2020
---

## Summary
[To be filled during ingest]

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:problem:knowledge-graph-question-answering
- pkis:concept:knowledge-graph
- pkis:source:cheng-cograg
- pkis:concept:multi-hop-reasoning
- pkis:source:cetoli-named-2018

## Notes
2WikiMultiHopQA: multi-hop QA combining Wikidata structure with Wikipedia text. Comparison + composition reasoning types. ~167,000 questions. Some instances have annotated ground-truth reasoning paths. Metrics: EM, F1, AND path overlap ratio. Contamination risk: high. Role: most important benchmark for VGT — path overlap metric directly tests whether variational traversal recovers ground-truth paths more efficiently than heuristic beam search.