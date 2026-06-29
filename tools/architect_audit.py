#!/usr/bin/env python3
"""Architect drift audit — emit ATOMIC, individually-acceptable doc-drift items.

Fortnightly, the Architect reads the backend code and the living docs (ARCHITECTURE,
ABOUT, USAGE) and reports where the docs have drifted from the code — NOT as one
monolithic rewrite, but as discrete items, each a single self-contained change with
an exact anchor→replacement edit. A major revision is decomposed into the smallest
independently-applyable pieces. Items land in /home/pkis/architect_drift.json and
surface in the owner inbox (Docs drift lane) with accept/dismiss; accepting one
applies just that edit. (STATUS.md is handled separately by architect_reconcile.py.)

  python tools/architect_audit.py            # audit + write pending items
  python tools/architect_audit.py --dry      # print items, no write
"""
import os, re, sys, json, glob, hashlib, datetime

REPO = "/home/pkis/pkis-wiki"
DRIFT_JSON = "/home/pkis/architect_drift.json"
MODEL = os.environ.get("PKIS_ARCHITECT_MODEL", "claude-sonnet-4-6")

# Code the audit reads, and the docs it may propose edits to (relative to REPO).
CODE = ["app.py", "config.py", "store.py", "adapters.py", "usage.py", "paths.py",
        "ask.py", "conversations.py"]
DOCS = ["docs/ARCHITECTURE.md", "docs/ABOUT.md", "docs/USAGE.md"]

SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "doc": {"type": "string", "description": "one of the doc paths, e.g. docs/ARCHITECTURE.md"},
                    "title": {"type": "string", "description": "≤8-word summary of this one change"},
                    "rationale": {"type": "string", "description": "what the doc says vs what the code does"},
                    "anchor": {"type": "string", "description": "EXACT, UNIQUE existing substring of the doc to replace (verbatim, incl. whitespace)"},
                    "replacement": {"type": "string", "description": "the corrected substring to put in its place"},
                },
                "required": ["doc", "title", "rationale", "anchor", "replacement"],
            },
        }
    },
    "required": ["items"],
}

SYSTEM = (
    "You are the PKIS Architect performing a documentation drift audit. You are given "
    "the backend source and the living docs (ARCHITECTURE/ABOUT/USAGE). Find places "
    "where a doc no longer matches the code. Emit each discrepancy as a SEPARATE, "
    "atomic item — one self-contained change each — never a bundled rewrite. Decompose "
    "a large/major revision into the smallest independently-applyable pieces (e.g. three "
    "separate auth-section fixes, not one). For each item give an `anchor`: an EXACT, "
    "VERBATIM, UNIQUE substring of the current doc (copy it character-for-character, "
    "including punctuation and surrounding words enough to be unique), and a `replacement` "
    "that corrects only that span. Be conservative: only report real drift you can point "
    "to in the code; do not restyle, do not invent. If a doc is accurate, emit nothing for it."
)


def _build_input():
    parts = []
    for f in CODE:
        p = os.path.join(REPO, f)
        if os.path.exists(p):
            parts.append(f"=== CODE {f} ===\n{open(p).read()}")
    for f in DOCS:
        p = os.path.join(REPO, f)
        if os.path.exists(p):
            parts.append(f"=== DOC {f} (audit this) ===\n{open(p).read()}")
    return "\n\n".join(parts)


def _item_id(it):
    return "drift-" + hashlib.sha1((it["doc"] + "::" + it["anchor"]).encode()).hexdigest()[:12]


def audit():
    import anthropic
    c = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    r = c.messages.create(
        model=MODEL, max_tokens=8000, system=SYSTEM,
        tools=[{"name": "report_drift", "description": "Report doc-drift items", "input_schema": SCHEMA}],
        tool_choice={"type": "tool", "name": "report_drift"},
        messages=[{"role": "user", "content": _build_input()}],
    )
    for block in r.content:
        if getattr(block, "type", None) == "tool_use":
            return block.input.get("items", [])
    return []


def main():
    dry = "--dry" in sys.argv
    raw = audit()
    # validate each item's anchor actually exists (uniquely) in its doc; drop the rest.
    items, dropped = [], 0
    for it in raw:
        doc = it.get("doc", "")
        p = os.path.join(REPO, doc)
        if doc not in DOCS or not os.path.exists(p):
            dropped += 1; continue
        text = open(p).read()
        if text.count(it.get("anchor", "\x00")) != 1:
            dropped += 1; continue            # anchor missing or ambiguous → unapplyable
        it["id"] = _item_id(it)
        it["status"] = "pending"
        items.append(it)

    # merge with history: keep prior accepted/dismissed decisions, don't resurface them.
    prev = {}
    if os.path.exists(DRIFT_JSON):
        try:
            prev = {x["id"]: x for x in json.load(open(DRIFT_JSON)).get("items", [])}
        except Exception:
            prev = {}
    merged = []
    seen = set()
    for it in items:
        seen.add(it["id"])
        old = prev.get(it["id"])
        merged.append(old if old and old.get("status") in ("accepted", "dismissed") else it)
    # carry forward prior decided items (history) even if no longer detected
    for pid, old in prev.items():
        if pid not in seen and old.get("status") in ("accepted", "dismissed"):
            merged.append(old)

    out = {"items": merged}
    npend = sum(1 for x in merged if x.get("status") == "pending")
    if dry:
        print(json.dumps(out, indent=2)[:4000]); print(f"\n[{npend} pending, {dropped} dropped (bad anchor)]"); return
    json.dump(out, open(DRIFT_JSON, "w"), indent=2)
    print(f"wrote {DRIFT_JSON}: {npend} pending drift items ({dropped} dropped for bad anchor)")


if __name__ == "__main__":
    main()
