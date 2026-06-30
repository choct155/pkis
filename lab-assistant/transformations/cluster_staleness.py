"""Example transformation: project each monitoring snapshot to just its cluster
staleness picture — a focused view for "which clusters have gone quiet?".

Pure: takes snapshot records in, returns reshaped records out. No side effects.
"""
from typing import Iterable


def transform(records: Iterable[dict]) -> Iterable[dict]:
    out = []
    for r in records:
        clusters = r.get("clusters") or {}
        stale = {slug: c.get("staleness_days") for slug, c in clusters.items()}
        out.append({
            "generated_at": r.get("generated_at"),
            "cluster_count": len(clusters),
            "staleness_days_by_cluster": stale,
            "max_staleness_days": max([v for v in stale.values() if v is not None], default=None),
        })
    return out
