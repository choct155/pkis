#!/usr/bin/env python3
"""Audit asset `kind` (genre) vocabulary against the controlled registry.

An asset's `kind` is open/expandable, but governed: this catches drift —
- kinds used in wiki/assets/*.md but missing from wiki/asset_kinds.json
- registry kinds nobody uses (dead vocabulary)
- kinds that shadow a node knowledge_type, or near-duplicate another kind
  (normalized: lowercased, de-hyphen/underscore/space, naive singular).

Exit non-zero if any drift is found, so it can gate CI / a pre-commit check.
Usage: python tools/audit_asset_kinds.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "wiki" / "assets"
REGISTRY = ROOT / "wiki" / "asset_kinds.json"

# Node knowledge_types a genre must never shadow.
NODE_TYPES = {
    "concept", "technique", "result", "framework", "problem", "principle",
    "source", "asset", "hypothesis", "bridge-note", "research-cluster",
    "discovery-stub",
}


def norm(s: str) -> str:
    s = re.sub(r"[-_\s]+", "", s.strip().lower())
    return s[:-1] if s.endswith("s") else s  # naive singular


def main() -> int:
    reg = json.loads(REGISTRY.read_text())
    registry_kinds = set(reg.get("kinds", {}))

    used = {}
    for f in sorted(ASSETS.glob("*.md")):
        for line in f.read_text(errors="ignore").splitlines():
            m = re.match(r"^kind:\s*(.+?)\s*$", line)
            if m:
                used.setdefault(m.group(1), []).append(f.name)
                break

    problems = []

    # 1. used but unregistered → drift
    for k in sorted(set(used) - registry_kinds):
        problems.append(f"UNREGISTERED kind '{k}' used by {used[k]} — add it to "
                        f"asset_kinds.json with a definition, or fix the typo.")

    # 2. registered but unused (informational, not fatal)
    unused = sorted(registry_kinds - set(used))

    # 3. shadows a node type
    for k in sorted(registry_kinds | set(used)):
        if norm(k) in {norm(t) for t in NODE_TYPES}:
            problems.append(f"COLLISION kind '{k}' shadows a node knowledge_type.")

    # 4. near-duplicate kinds (same normalized form)
    seen = {}
    for k in sorted(registry_kinds | set(used)):
        seen.setdefault(norm(k), []).append(k)
    for n, group in seen.items():
        if len(group) > 1:
            problems.append(f"NEAR-DUPLICATE kinds collapse to '{n}': {group} — "
                            f"pick one canonical spelling.")

    print(f"registry kinds : {sorted(registry_kinds)}")
    print(f"kinds in use   : {sorted(used)}")
    if unused:
        print(f"unused (ok)    : {unused}")
    if problems:
        print("\nDRIFT:")
        for p in problems:
            print(f"  ✗ {p}")
        return 1
    print("\n✓ asset kind vocabulary is clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
