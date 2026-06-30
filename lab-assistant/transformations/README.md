# Lab Assistant Transformations

Versioned, inspectable **pure Python** transformations the PKIS Lab Assistant applies
to monitoring-snapshot records (the JSONL written by `tools/lab_monitor.py`). This
directory is the PKIS-side instantiation of the canonical Lab Assistant pattern —
distinct from `wiki/` (it is analysis code, not research content).

## Interface contract

Each transformation is a `.py` module in this directory exposing a single function:

```python
def transform(records: Iterable[dict]) -> Iterable[dict]:
    ...
```

- **Pure.** Takes records in, returns records out. No side effects, no mutation of the
  input records or the underlying JSONL files, no I/O.
- Input is an iterable of snapshot dicts (or the output of a prior transformation).

## Discipline (non-negotiable)

- Transformations are **stored code, never ephemeral natural-language instructions**.
- A natural-language request **drafts a new versioned function for human review** — the
  runner never reinterprets or silently "improves" a stored transform. To change
  behavior, add or edit a function here deliberately and commit it.
- The Lab Assistant is descriptive: transformations summarize/reshape what the data
  shows. They do not assert causal conclusions or change research state.

## Running

```bash
python tools/lab_transform.py <name> <snapshot.jsonl>   # apply transforms/<name>.py
```

See `cluster_staleness.py` for a worked example.
