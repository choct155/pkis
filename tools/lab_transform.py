#!/usr/bin/env python3
"""lab_transform.py — apply a named, versioned Lab Assistant transformation to a
monitoring-snapshot JSONL file.

Transformations live in `lab-assistant/transformations/<name>.py` and expose a pure
`transform(records) -> records` function (see that directory's README). This runner
loads a transform BY NAME and applies it exactly as written — it never reinterprets
or mutates a stored transform, and never writes back to the input file.

    python tools/lab_transform.py cluster_staleness /home/pkis/lab/lab_monitoring_2026-06-30.jsonl
"""
import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
TRANSFORM_DIR = REPO_ROOT / "lab-assistant" / "transformations"


def load_transform(name: str):
    """Return the `transform` callable from lab-assistant/transformations/<name>.py."""
    path = TRANSFORM_DIR / f"{name}.py"
    if not path.exists():
        raise FileNotFoundError(f"no transformation named {name!r} in {TRANSFORM_DIR}")
    spec = importlib.util.spec_from_file_location(f"lab_transform_{name}", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fn = getattr(mod, "transform", None)
    if not callable(fn):
        raise TypeError(f"transformation {name!r} does not expose a callable transform(records)")
    return fn


def read_records(jsonl_path) -> list:
    return [json.loads(ln) for ln in Path(jsonl_path).read_text().splitlines() if ln.strip()]


def apply_named(name: str, records) -> list:
    """Apply transform <name> to records; returns a fresh list (input untouched)."""
    return list(load_transform(name)(list(records)))


def main():
    ap = argparse.ArgumentParser(description="Apply a named Lab Assistant transformation")
    ap.add_argument("name", help="transformation module name (without .py)")
    ap.add_argument("jsonl", help="path to a lab_monitoring_*.jsonl snapshot file")
    args = ap.parse_args()
    for rec in apply_named(args.name, read_records(args.jsonl)):
        print(json.dumps(rec))


if __name__ == "__main__":
    main()
