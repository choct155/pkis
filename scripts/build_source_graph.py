#!/usr/bin/env python3
"""
Build Source Dependency Graph
==============================
Constructs wiki/source_graph.json from the existing wiki data:

  - concepts: frontmatter in each source node  → source covers concept X
  - ## Reading Path sections in knowledge nodes → citation count per source
  - wiki/queue.md                              → marks "actively tracking" sources

Edge semantics
--------------
Two sources are connected if they share ≥ MIN_EDGE_WEIGHT concepts.
Direction is inferred: if source A's load-bearing score is ≥ DIRECTION_RATIO × B's,
A is flagged as the prerequisite. Edges below the ratio are marked "overlap".

Node load-bearing score
-----------------------
The number of distinct knowledge nodes (concepts, techniques, results, …) whose
## Reading Path sections cite this source. High score = many downstream nodes
depend on understanding it.

Gateway nodes
-------------
Sources with lb_score in the top quartile AND no inbound prerequisite edges in
the directed graph. These are the "start here" nodes — high value, nothing you
need to read first.

Clusters
--------
Connected components of the undirected overlap graph. Named by the concept that
appears in the most sources within the cluster.

Usage:
    python3 scripts/build_source_graph.py [--min-weight N] [--dry-run]
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml")
    sys.exit(1)

WIKI_DIR   = Path(__file__).parent.parent / "wiki"
OUTPUT     = WIKI_DIR / "source_graph.json"

# Tuning parameters (overridable via CLI later)
MIN_EDGE_WEIGHT = 2      # minimum shared concepts to draw an edge
DIRECTION_RATIO = 1.5    # lb_score ratio required to infer A→B direction

KNOWLEDGE_DIRS = ["concepts", "techniques", "results", "frameworks", "problems", "principles"]


# ── helpers ────────────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except Exception:
        return {}


def extract_wikilinks(text: str) -> list[str]:
    return re.findall(r'\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]', text)


# ── Step 1: load-bearing scores from Reading Path citations ────────────────

def build_lb_scores() -> tuple[dict, dict]:
    """
    Returns:
        lb_scores:          source_slug → int (# knowledge nodes citing it)
        concept_rp_sources: concept_slug → [source_slug, ...]
    """
    lb_scores: dict[str, int] = defaultdict(int)
    concept_rp_sources: dict[str, list] = defaultdict(list)

    for folder in KNOWLEDGE_DIRS:
        d = WIKI_DIR / folder
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            text = f.read_text(encoding="utf-8")
            if "## Reading Path" not in text:
                continue
            rp_section = text.split("## Reading Path")[1].split("\n##")[0]
            for src_slug in extract_wikilinks(rp_section):
                lb_scores[src_slug] += 1
                concept_rp_sources[f.stem].append(src_slug)

    return dict(lb_scores), dict(concept_rp_sources)


# ── Step 2: parse source nodes ─────────────────────────────────────────────

def load_source_nodes(lb_scores: dict) -> dict:
    """Returns dict slug → node_info."""
    nodes = {}
    sources_dir = WIKI_DIR / "sources"
    if not sources_dir.exists():
        return nodes

    for f in sorted(sources_dir.glob("*.md")):
        fm = parse_frontmatter(f.read_text(encoding="utf-8"))
        slug = f.stem

        # Parse concepts field — may be a list of wikilinks or plain slugs
        raw_concepts = fm.get("concepts", [])
        concepts: list[str] = []
        if isinstance(raw_concepts, list):
            for c in raw_concepts:
                s = re.sub(r'[\[\]]', '', str(c)).strip()
                if s:
                    concepts.append(s)
        elif isinstance(raw_concepts, str):
            concepts = extract_wikilinks(raw_concepts) or [
                c.strip() for c in raw_concepts.split(",") if c.strip()
            ]

        nodes[slug] = {
            "iri":       fm.get("id", f"pkis:source:{slug}"),
            "slug":      slug,
            "title":     fm.get("title", slug),
            "status":    fm.get("status", "unread"),
            "type":      fm.get("type", "unknown"),
            "year":      fm.get("year"),
            "authors":   fm.get("authors", ""),
            "domain":    fm.get("domain", []),
            "concepts":  concepts,
            "lb_score":  lb_scores.get(slug, 0),
            "in_queue":  False,   # filled in step 3
        }
    return nodes


# ── Step 3: mark queue membership ─────────────────────────────────────────

def mark_queue_items(nodes: dict) -> set:
    """
    Returns set of queued source slugs; mutates nodes in place.
    Only the FIRST wikilink on each checkbox line is treated as the queued source —
    subsequent wikilinks are concept/context references in the description.
    """
    queue_path = WIKI_DIR / "queue.md"
    if not queue_path.exists():
        return set()
    text = queue_path.read_text(encoding="utf-8")
    queue_slugs: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("- ["):
            continue
        # Take only the first wikilink on the line
        m = re.search(r'\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]', stripped)
        if m:
            slug = m.group(1).strip()
            queue_slugs.add(slug)
    for slug in queue_slugs:
        if slug in nodes:
            nodes[slug]["in_queue"] = True
    return queue_slugs


# ── Step 4: build edges ────────────────────────────────────────────────────

def build_edges(nodes: dict) -> list[dict]:
    """
    For each pair of sources sharing ≥ MIN_EDGE_WEIGHT concepts, emit an edge.
    Direction inferred from lb_score ratio.
    """
    # concept → set of source slugs that cover it
    concept_to_slugs: dict[str, set] = defaultdict(set)
    for slug, info in nodes.items():
        for c in info["concepts"]:
            concept_to_slugs[c].add(slug)

    # accumulate shared concepts per (a, b) pair
    pair_shared: dict[tuple, set] = defaultdict(set)
    for concept, slugs in concept_to_slugs.items():
        slugs_list = sorted(slugs)
        for i in range(len(slugs_list)):
            for j in range(i + 1, len(slugs_list)):
                pair = (slugs_list[i], slugs_list[j])
                pair_shared[pair].add(concept)

    edges = []
    for (a, b), shared in pair_shared.items():
        if len(shared) < MIN_EDGE_WEIGHT:
            continue
        sa = nodes[a]["lb_score"]
        sb = nodes[b]["lb_score"]
        # Determine direction
        if sa > 0 and sb > 0 and sa >= DIRECTION_RATIO * sb:
            direction = "prerequisite"   # a → b
            from_slug, to_slug = a, b
        elif sb > 0 and sa > 0 and sb >= DIRECTION_RATIO * sa:
            direction = "prerequisite"   # b → a
            from_slug, to_slug = b, a
        else:
            direction = "overlap"
            from_slug, to_slug = a, b   # arbitrary for undirected

        edges.append({
            "from":            from_slug,
            "to":              to_slug,
            "weight":          len(shared),
            "shared_concepts": sorted(shared),
            "direction":       direction,
        })

    return edges


# ── Step 5: find connected components (clusters) ──────────────────────────

def find_clusters(nodes: dict, edges: list[dict]) -> dict[str, int]:
    """
    Union-Find over the undirected overlap graph.
    Returns slug → cluster_id mapping.
    """
    parent = {slug: slug for slug in nodes}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    for e in edges:
        if e["from"] in nodes and e["to"] in nodes:
            union(e["from"], e["to"])

    # Assign integer cluster IDs by order of first encounter
    root_to_id: dict[str, int] = {}
    slug_to_cluster: dict[str, int] = {}
    for slug in sorted(nodes):
        root = find(slug)
        if root not in root_to_id:
            root_to_id[root] = len(root_to_id)
        slug_to_cluster[slug] = root_to_id[root]

    return slug_to_cluster


def name_clusters(nodes: dict, edges: list[dict], slug_to_cluster: dict) -> dict[int, dict]:
    """
    Name each cluster by the concept that appears most across its members.
    Returns cluster_id → {name, size, top_concepts, top_sources_by_lb}.
    """
    cluster_concept_count: dict[int, dict] = defaultdict(lambda: defaultdict(int))
    cluster_members: dict[int, list] = defaultdict(list)

    for slug, info in nodes.items():
        cid = slug_to_cluster[slug]
        cluster_members[cid].append(slug)
        for c in info["concepts"]:
            cluster_concept_count[cid][c] += 1

    clusters: dict[int, dict] = {}
    for cid, members in cluster_members.items():
        top_concepts = sorted(
            cluster_concept_count[cid].items(), key=lambda x: x[1], reverse=True
        )[:5]
        top_sources = sorted(members, key=lambda s: nodes[s]["lb_score"], reverse=True)[:5]
        label = top_concepts[0][0].replace("-", " ").title() if top_concepts else f"Cluster {cid}"
        clusters[cid] = {
            "id":                   cid,
            "label":                label,
            "size":                 len(members),
            "top_concepts":         [c for c, _ in top_concepts],
            "top_sources_by_lb":    top_sources,
        }

    return clusters


# ── Step 6: identify gateway nodes ────────────────────────────────────────

def find_gateway_nodes(nodes: dict, edges: list[dict]) -> list[str]:
    """
    Gateway = high lb_score AND no inbound 'prerequisite' edges
    (nothing you're required to read first).
    """
    has_prerequisite_inbound: set[str] = set()
    for e in edges:
        if e["direction"] == "prerequisite":
            has_prerequisite_inbound.add(e["to"])

    lb_scores = [info["lb_score"] for info in nodes.values() if info["lb_score"] > 0]
    if not lb_scores:
        return []
    # Top quartile threshold
    lb_scores_sorted = sorted(lb_scores)
    q3 = lb_scores_sorted[int(len(lb_scores_sorted) * 0.75)]

    gateways = [
        slug for slug, info in nodes.items()
        if info["lb_score"] >= q3 and slug not in has_prerequisite_inbound
    ]
    return sorted(gateways, key=lambda s: nodes[s]["lb_score"], reverse=True)


# ── Step 7: suggested reading sequence ────────────────────────────────────

def suggested_sequence(nodes: dict, edges: list[dict], queue_slugs: set) -> list[str]:
    """
    Topological-ish sort over queue items using Kahn's algorithm
    on the directed prerequisite subgraph, with lb_score as tiebreaker.
    Falls back gracefully when cycles exist.
    """
    queue_set = {s for s in queue_slugs if s in nodes}
    in_degree: dict[str, int] = defaultdict(int)
    adj: dict[str, list] = defaultdict(list)

    for e in edges:
        if e["direction"] != "prerequisite":
            continue
        if e["from"] in queue_set and e["to"] in queue_set:
            in_degree[e["to"]] += 1
            adj[e["from"]].append(e["to"])

    # Ensure all queue items are in in_degree
    for s in queue_set:
        if s not in in_degree:
            in_degree[s] = 0

    import heapq
    # Max-heap by lb_score (negate for min-heap)
    heap = [(-nodes[s]["lb_score"], s) for s, d in in_degree.items() if d == 0]
    heapq.heapify(heap)

    order = []
    while heap:
        _, slug = heapq.heappop(heap)
        order.append(slug)
        for neighbor in adj.get(slug, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, (-nodes[neighbor]["lb_score"], neighbor))

    # Any remaining queue items not in the DAG (isolated or in cycles)
    remaining = sorted(
        [s for s in queue_set if s not in order],
        key=lambda s: -nodes[s]["lb_score"]
    )
    return order + remaining


# ── main ───────────────────────────────────────────────────────────────────

def build_graph(dry_run: bool = False, min_weight: int = MIN_EDGE_WEIGHT) -> dict:
    global MIN_EDGE_WEIGHT
    MIN_EDGE_WEIGHT = min_weight

    print("Building source dependency graph...")

    lb_scores, _ = build_lb_scores()
    print(f"  Load-bearing scores computed for {len(lb_scores)} sources")

    nodes = load_source_nodes(lb_scores)
    print(f"  Loaded {len(nodes)} source nodes")

    queue_slugs = mark_queue_items(nodes)
    print(f"  Marked {len(queue_slugs)} queue items")

    edges = build_edges(nodes)
    print(f"  Built {len(edges)} edges (min_weight={MIN_EDGE_WEIGHT})")

    slug_to_cluster = find_clusters(nodes, edges)
    cluster_info    = name_clusters(nodes, edges, slug_to_cluster)
    print(f"  Found {len(cluster_info)} connected components")

    gateway_nodes   = find_gateway_nodes(nodes, edges)
    sequence        = suggested_sequence(nodes, edges, queue_slugs)

    # Annotate nodes with cluster ID
    for slug in nodes:
        nodes[slug]["cluster_id"] = slug_to_cluster.get(slug, -1)

    # Summary stats
    unread_count   = sum(1 for n in nodes.values() if n["status"] == "unread")
    queued_count   = sum(1 for n in nodes.values() if n["in_queue"])
    prereq_edges   = sum(1 for e in edges if e["direction"] == "prerequisite")
    overlap_edges  = sum(1 for e in edges if e["direction"] == "overlap")

    graph = {
        "meta": {
            "generated_at":    __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "min_edge_weight": MIN_EDGE_WEIGHT,
            "direction_ratio": DIRECTION_RATIO,
            "total_sources":   len(nodes),
            "unread_sources":  unread_count,
            "queued_sources":  queued_count,
            "total_edges":     len(edges),
            "prerequisite_edges": prereq_edges,
            "overlap_edges":   overlap_edges,
            "cluster_count":   len(cluster_info),
        },
        "nodes":            nodes,
        "edges":            edges,
        "clusters":         cluster_info,
        "gateway_nodes":    gateway_nodes[:20],
        "suggested_sequence": sequence,
    }

    if not dry_run:
        OUTPUT.write_text(json.dumps(graph, indent=2, ensure_ascii=False))
        print(f"\nWrote {OUTPUT}")
    else:
        print("\n[DRY RUN — not written]")

    print(f"\nSummary:")
    print(f"  {unread_count} unread sources, {queued_count} in queue")
    print(f"  {prereq_edges} prerequisite edges, {overlap_edges} overlap edges")
    print(f"  {len(cluster_info)} thematic clusters")
    print(f"  {len(gateway_nodes)} gateway nodes (start here)")
    print(f"\nTop 10 gateway nodes:")
    for slug in gateway_nodes[:10]:
        n = nodes[slug]
        q = "★" if n["in_queue"] else " "
        print(f"  {q} [{n['lb_score']:3d}] {slug}")
        print(f"       {n['title'][:65]}")

    return graph


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    min_w   = MIN_EDGE_WEIGHT
    for arg in sys.argv[1:]:
        if arg.startswith("--min-weight="):
            min_w = int(arg.split("=")[1])
    build_graph(dry_run=dry_run, min_weight=min_w)
