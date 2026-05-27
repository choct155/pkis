"""
PKIS Wiki MCP Server
====================
Implements the full PKIS MCP API as defined in the system design.
Serves the pkis-wiki repository as a knowledge service accessible
from Claude.ai, Claude Code, and any MCP-compatible client.

Deployed to: https://pkis.dev
Wiki source: /home/pkis/pkis-wiki/wiki/
"""

import os
import re
import json
import glob
import uuid
import hashlib
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml
import frontmatter
import networkx as nx
import numpy as np
from rank_bm25 import BM25Okapi
from flask import Flask, request, jsonify, Response
from anthropic import Anthropic

# ============================================================
# Configuration
# ============================================================

WIKI_DIR = Path(os.environ.get("WIKI_DIR", "/home/pkis/pkis-wiki/wiki"))
RAW_DIR = Path(os.environ.get("RAW_DIR", "/home/pkis/pkis-wiki/raw"))
REPO_DIR = Path(os.environ.get("REPO_DIR", "/home/pkis/pkis-wiki"))
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

KNOWLEDGE_DIRS = [
    "concepts", "techniques", "results",
    "frameworks", "problems", "principles", "sources"
]

# Edge type weights for structural ranking (prerequisite-of highest)
EDGE_WEIGHTS = {
    "prerequisite-of": 1.0,
    "uses": 0.8,
    "specializes": 0.6,
    "generalizes": 0.6,
    "extends": 0.5,
    "applies": 0.5,
    "instantiates": 0.4,
    "contrasts-with": 0.2,
}

# Trusted client token — set via env var in production
TRUSTED_TOKEN = os.environ.get("PKIS_TRUSTED_TOKEN", "")

# MCP JSON-RPC 2.0 Streamable HTTP transport constants
JSONRPC_VERSION = "2.0"
MCP_PROTOCOL_VERSION = "2024-11-05"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)

# ============================================================
# In-memory caches (invalidated on git pull via /refresh)
# ============================================================

_alias_registry: dict = {}
_node_cache: dict = {}
_graph: Optional[nx.DiGraph] = None
_bm25_index = None
_bm25_corpus: list = []
_bm25_slugs: list = []


# ============================================================
# Core helpers
# ============================================================

def slug_from_path(path: Path) -> str:
    return path.stem


def iri_from_slug(node_type: str, slug: str) -> str:
    """Generate a stable IRI from node type and slug."""
    return f"pkis:{node_type}:{slug}"


def parse_iri(iri: str) -> tuple:
    """Parse IRI into (namespace, node_type, slug)."""
    parts = iri.split(":")
    if len(parts) >= 3:
        return parts[0], parts[1], parts[2]
    return None, None, None


def find_node_path(slug: str) -> Optional[Path]:
    """Find the file path for a slug, searching all knowledge dirs."""
    for kdir in KNOWLEDGE_DIRS:
        p = WIKI_DIR / kdir / f"{slug}.md"
        if p.exists():
            return p
    return None


def find_node_path_by_iri(iri: str) -> Optional[Path]:
    """Resolve an IRI to a file path."""
    _, node_type, slug = parse_iri(iri)
    if not slug:
        return None
    # Try the typed directory first
    if node_type and node_type in KNOWLEDGE_DIRS:
        p = WIKI_DIR / node_type / f"{slug}.md"
        if p.exists():
            return p
    # Fall back to searching all dirs
    return find_node_path(slug)


def load_node(path: Path) -> dict:
    """Load and parse a wiki node file."""
    if str(path) in _node_cache:
        return _node_cache[str(path)]

    try:
        post = frontmatter.load(str(path))
        node_type = path.parent.name
        slug = path.stem

        # Generate IRI if not in frontmatter
        iri = post.metadata.get("id") or iri_from_slug(node_type, slug)

        result = {
            "iri": iri,
            "slug": slug,
            "node_type": node_type,
            "path": str(path),
            "frontmatter": dict(post.metadata),
            "content": post.content,
            "title": post.metadata.get("title", slug),
            "domain": post.metadata.get("domain", []),
            "aliases": post.metadata.get("aliases", []),
            "coverage": post.metadata.get("coverage", 0),
            "understanding": post.metadata.get("understanding", 0),
            "confidence": post.metadata.get("confidence", 0),
            "date_updated": post.metadata.get("date_updated", ""),
        }
        _node_cache[str(path)] = result
        return result
    except Exception as e:
        logger.error(f"Error loading {path}: {e}")
        return {}


def load_all_nodes() -> list:
    """Load all wiki nodes across all knowledge directories."""
    nodes = []
    for kdir in KNOWLEDGE_DIRS:
        dir_path = WIKI_DIR / kdir
        if not dir_path.exists():
            continue
        for md_file in dir_path.glob("*.md"):
            node = load_node(md_file)
            if node:
                nodes.append(node)
    return nodes


def build_alias_registry() -> dict:
    """Build flat alias → IRI registry from all node frontmatter."""
    registry = {}
    nodes = load_all_nodes()
    for node in nodes:
        iri = node["iri"]
        # Register canonical title
        title = node.get("title", "")
        if title:
            registry[title.lower()] = iri
        # Register slug
        registry[node["slug"].lower()] = iri
        # Register all aliases
        for alias in node.get("aliases", []):
            registry[alias.lower()] = iri
    return registry


def build_graph() -> nx.DiGraph:
    """Build NetworkX graph from wiki wikilinks and typed edges."""
    G = nx.DiGraph()
    nodes = load_all_nodes()

    for node in nodes:
        G.add_node(node["iri"], **{
            "slug": node["slug"],
            "title": node["title"],
            "node_type": node["node_type"],
            "domain": node["domain"],
            "coverage": node["coverage"],
        })

    # Parse wikilinks from content to build edges
    wikilink_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
    for node in nodes:
        content = node.get("content", "")
        # Also check frontmatter for typed relationships
        fm = node.get("frontmatter", {})

        # Extract edges from typed relationship fields
        for edge_type in EDGE_WEIGHTS.keys():
            targets = fm.get(edge_type.replace("-", "_"), []) or \
                      fm.get(edge_type, [])
            if isinstance(targets, str):
                targets = [targets]
            for target in targets:
                target_slug = target.strip("[]").split("|")[0]
                target_path = find_node_path(target_slug)
                if target_path:
                    target_node = load_node(target_path)
                    if target_node:
                        G.add_edge(
                            node["iri"],
                            target_node["iri"],
                            edge_type=edge_type,
                            weight=EDGE_WEIGHTS[edge_type]
                        )

        # Extract edges from raw wikilinks
        for match in wikilink_pattern.finditer(content):
            target_slug = match.group(1).strip()
            target_path = find_node_path(target_slug)
            if target_path:
                target_node = load_node(target_path)
                if target_node and target_node["iri"] != node["iri"]:
                    if not G.has_edge(node["iri"], target_node["iri"]):
                        G.add_edge(
                            node["iri"],
                            target_node["iri"],
                            edge_type="related",
                            weight=0.3
                        )

    return G


def build_bm25_index():
    """Build BM25 keyword index over all node content."""
    global _bm25_index, _bm25_corpus, _bm25_slugs
    nodes = load_all_nodes()
    corpus = []
    slugs = []
    for node in nodes:
        text = f"{node['title']} {node.get('content', '')} {' '.join(node.get('aliases', []))}"
        tokens = text.lower().split()
        corpus.append(tokens)
        slugs.append(node["iri"])
    _bm25_index = BM25Okapi(corpus)
    _bm25_corpus = corpus
    _bm25_slugs = slugs


def refresh_caches():
    """Invalidate and rebuild all caches."""
    global _alias_registry, _node_cache, _graph, _bm25_index
    _node_cache = {}
    _alias_registry = build_alias_registry()
    _graph = build_graph()
    build_bm25_index()
    logger.info(f"Caches refreshed: {len(_alias_registry)} aliases, "
                f"{_graph.number_of_nodes()} nodes, "
                f"{_graph.number_of_edges()} edges")


def get_alias_registry() -> dict:
    global _alias_registry
    if not _alias_registry:
        _alias_registry = build_alias_registry()
    return _alias_registry


def get_graph() -> nx.DiGraph:
    global _graph
    if _graph is None:
        _graph = build_graph()
    return _graph


def structural_candidates(seed_iri: str, edge_types=None, max_hops=2) -> list:
    """Return structurally connected nodes with weighted scores."""
    G = get_graph()
    if seed_iri not in G:
        return []

    candidates = []
    visited = {seed_iri}

    def traverse(node_iri, depth):
        if depth > max_hops:
            return
        for neighbor in G.successors(node_iri):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            edge_data = G.get_edge_data(node_iri, neighbor) or {}
            etype = edge_data.get("edge_type", "related")
            if edge_types and etype not in edge_types:
                continue
            weight = EDGE_WEIGHTS.get(etype, 0.3)
            # Decay weight by depth
            effective_weight = weight * (0.7 ** (depth - 1))
            candidates.append({
                "iri": neighbor,
                "edge_type": etype,
                "weight": effective_weight,
                "hop_count": depth
            })
            traverse(neighbor, depth + 1)

    traverse(seed_iri, 1)
    return sorted(candidates, key=lambda x: x["weight"], reverse=True)


def rrf_score(rank: int, k: int = 60) -> float:
    return 1.0 / (k + rank)


def hybrid_search(query: str, domains=None, node_types=None, max_results=10) -> list:
    """Hybrid BM25 + structural search with RRF fusion."""
    global _bm25_index, _bm25_slugs

    if _bm25_index is None:
        build_bm25_index()

    # BM25 semantic ranking
    tokens = query.lower().split()
    bm25_scores = _bm25_index.get_scores(tokens)
    bm25_ranked = sorted(
        enumerate(bm25_scores),
        key=lambda x: x[1],
        reverse=True
    )[:max_results * 3]

    # Build RRF score map
    rrf_scores = {}
    for rank, (idx, score) in enumerate(bm25_ranked):
        iri = _bm25_slugs[idx]
        rrf_scores[iri] = rrf_scores.get(iri, 0) + rrf_score(rank)

    # Apply filters
    all_nodes = load_all_nodes()
    node_map = {n["iri"]: n for n in all_nodes}

    results = []
    seen = set()
    for iri, score in sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True):
        if iri in seen:
            continue
        seen.add(iri)
        node = node_map.get(iri)
        if not node:
            continue
        if domains and not any(d in node.get("domain", []) for d in domains):
            continue
        if node_types and node.get("node_type") not in node_types:
            continue
        results.append({
            "iri": iri,
            "canonical_title": node["title"],
            "node_type": node["node_type"],
            "domain": node["domain"],
            "score": score,
            "excerpt": node["content"][:300] if node.get("content") else "",
            "coverage": node["coverage"],
            "understanding": node["understanding"],
        })
        if len(results) >= max_results:
            break

    return results


def is_trusted(req) -> bool:
    """Check if request carries trusted client token."""
    if not TRUSTED_TOKEN:
        return False
    auth = req.headers.get("Authorization", "")
    return auth == f"Bearer {TRUSTED_TOKEN}"


# ============================================================
# MCP Tool implementations
# ============================================================

def tool_resolve_concept(surface_form: str) -> dict:
    registry = get_alias_registry()
    normalized = surface_form.lower().strip()
    iri = registry.get(normalized)

    if iri:
        path = find_node_path_by_iri(iri)
        node = load_node(path) if path else {}
        return {
            "status": "found",
            "iri": iri,
            "canonical_title": node.get("title", ""),
            "confidence": 1.0,
            "aliases": node.get("aliases", [])
        }

    # Fuzzy fallback — find closest alias
    candidates = []
    for alias, candidate_iri in registry.items():
        if normalized in alias or alias in normalized:
            candidates.append({"iri": candidate_iri, "alias": alias})

    if candidates:
        return {
            "status": "ambiguous",
            "candidates": candidates[:5],
            "message": f"No exact match for '{surface_form}', found {len(candidates)} partial matches"
        }

    return {"status": "not_found", "surface_form": surface_form}


def tool_detect_concepts(text: str, threshold: float = 0.7) -> list:
    """Detect PKIS concepts in arbitrary text using BM25 + LLM judgment."""
    if _bm25_index is None:
        build_bm25_index()

    # BM25 pass to get candidates
    candidates = hybrid_search(text, max_results=10)
    if not candidates:
        return []

    # Use LLM to judge which candidates are genuinely instantiated
    candidate_descriptions = "\n".join([
        f"- {c['iri']}: {c['canonical_title']} (score: {c['score']:.3f})"
        for c in candidates
    ])

    prompt = f"""You are analyzing text to detect which PKIS knowledge concepts are instantiated in it.

Text to analyze:
{text[:2000]}

Candidate concepts (from keyword search):
{candidate_descriptions}

For each candidate, determine:
1. Is this concept genuinely present in the text (explicitly named, implicitly described, or structurally implied)?
2. What is your confidence (0.0-1.0)?
3. What type of reference is it: "explicit" (named directly), "semantic" (described without naming), or "structural" (implied by dependency)?

Return JSON array only, no other text:
[{{"iri": "...", "confidence": 0.0, "reference_type": "explicit|semantic|structural"}}]

Only include candidates with confidence >= {threshold}."""

    try:
        response = anthropic_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        result_text = response.content[0].text.strip()
        # Strip markdown fences if present
        result_text = re.sub(r'^```json\s*|\s*```$', '', result_text, flags=re.MULTILINE)
        results = json.loads(result_text)

        # Enrich with canonical titles
        all_nodes = {n["iri"]: n for n in load_all_nodes()}
        for r in results:
            node = all_nodes.get(r["iri"], {})
            r["canonical_title"] = node.get("title", r["iri"])

        return sorted(results, key=lambda x: x["confidence"], reverse=True)
    except Exception as e:
        logger.error(f"detect_concepts LLM call failed: {e}")
        # Fall back to BM25 results above threshold
        return [
            {
                "iri": c["iri"],
                "canonical_title": c["canonical_title"],
                "confidence": min(c["score"], 1.0),
                "reference_type": "semantic"
            }
            for c in candidates
            if c["score"] >= threshold
        ]


def tool_get_node(iri: str) -> dict:
    path = find_node_path_by_iri(iri)
    if not path:
        return {"error": f"Node not found: {iri}"}

    node = load_node(path)
    G = get_graph()

    # Get related nodes
    related = []
    if iri in G:
        for neighbor in list(G.successors(iri))[:10]:
            edge_data = G.get_edge_data(iri, neighbor) or {}
            neighbor_path = find_node_path_by_iri(neighbor)
            if neighbor_path:
                n = load_node(neighbor_path)
                related.append({
                    "iri": neighbor,
                    "title": n.get("title", neighbor),
                    "edge_type": edge_data.get("edge_type", "related"),
                    "direction": "outbound"
                })
        for predecessor in list(G.predecessors(iri))[:10]:
            edge_data = G.get_edge_data(predecessor, iri) or {}
            pred_path = find_node_path_by_iri(predecessor)
            if pred_path:
                n = load_node(pred_path)
                related.append({
                    "iri": predecessor,
                    "title": n.get("title", predecessor),
                    "edge_type": edge_data.get("edge_type", "related"),
                    "direction": "inbound"
                })

    return {
        "iri": iri,
        "frontmatter": node["frontmatter"],
        "content": node["content"],
        "related_nodes": related,
        "reading_path": node["frontmatter"].get("reading_path", [])
    }


def tool_get_node_stub(iri: str) -> dict:
    path = find_node_path_by_iri(iri)
    if not path:
        return {"error": f"Node not found: {iri}"}
    node = load_node(path)
    content = node.get("content", "")
    first_line = content.split("\n")[0].strip() if content else ""
    return {
        "iri": iri,
        "canonical_title": node["title"],
        "node_type": node["node_type"],
        "domain": node["domain"],
        "coverage": node["coverage"],
        "understanding": node["understanding"],
        "confidence": node["confidence"],
        "one_line_summary": first_line[:200]
    }


def tool_search_wiki(query: str, domains=None, node_types=None, max_results=10) -> list:
    return hybrid_search(query, domains=domains, node_types=node_types, max_results=max_results)


def tool_search_wiki_index(query: str) -> list:
    """Fast keyword-only index scan, no LLM involvement."""
    if _bm25_index is None:
        build_bm25_index()
    tokens = query.lower().split()
    scores = _bm25_index.get_scores(tokens)
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:20]
    all_nodes = {n["iri"]: n for n in load_all_nodes()}
    results = []
    for idx, score in ranked:
        if score <= 0:
            continue
        iri = _bm25_slugs[idx]
        node = all_nodes.get(iri, {})
        content = node.get("content", "")
        first_line = content.split("\n")[0].strip() if content else ""
        results.append({
            "iri": iri,
            "canonical_title": node.get("title", iri),
            "domain": node.get("domain", []),
            "node_type": node.get("node_type", ""),
            "coverage": node.get("coverage", 0),
            "understanding": node.get("understanding", 0),
            "one_line_summary": first_line[:200],
            "score": score
        })
    return results


def tool_get_related(iri: str, edge_types=None, direction="both", max_hops=2) -> list:
    G = get_graph()
    if iri not in G:
        return []

    results = []
    visited = {iri}

    def traverse_out(node_iri, depth):
        if depth > max_hops:
            return
        for neighbor in G.successors(node_iri):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            edge_data = G.get_edge_data(node_iri, neighbor) or {}
            etype = edge_data.get("edge_type", "related")
            if edge_types and etype not in edge_types:
                continue
            path = find_node_path_by_iri(neighbor)
            title = load_node(path).get("title", neighbor) if path else neighbor
            results.append({
                "iri": neighbor,
                "canonical_title": title,
                "edge_type": etype,
                "direction": "outbound",
                "hop_count": depth
            })
            traverse_out(neighbor, depth + 1)

    def traverse_in(node_iri, depth):
        if depth > max_hops:
            return
        for predecessor in G.predecessors(node_iri):
            if predecessor in visited:
                continue
            visited.add(predecessor)
            edge_data = G.get_edge_data(predecessor, node_iri) or {}
            etype = edge_data.get("edge_type", "related")
            if edge_types and etype not in edge_types:
                continue
            path = find_node_path_by_iri(predecessor)
            title = load_node(path).get("title", predecessor) if path else predecessor
            results.append({
                "iri": predecessor,
                "canonical_title": title,
                "edge_type": etype,
                "direction": "inbound",
                "hop_count": depth
            })
            traverse_in(predecessor, depth + 1)

    if direction in ("both", "outbound"):
        traverse_out(iri, 1)
    if direction in ("both", "inbound"):
        traverse_in(iri, 1)

    return results


def tool_get_dependency_chain(iri: str) -> list:
    """Follow prerequisite-of edges with no hop limit."""
    G = get_graph()
    if iri not in G:
        return []

    chain = []
    visited = {iri}
    queue = [(iri, 0)]

    while queue:
        current_iri, depth = queue.pop(0)
        for neighbor in G.successors(current_iri):
            if neighbor in visited:
                continue
            edge_data = G.get_edge_data(current_iri, neighbor) or {}
            if edge_data.get("edge_type") != "prerequisite-of":
                continue
            visited.add(neighbor)
            path = find_node_path_by_iri(neighbor)
            title = load_node(path).get("title", neighbor) if path else neighbor
            chain.append({"iri": neighbor, "canonical_title": title, "depth": depth + 1})
            queue.append((neighbor, depth + 1))

    return sorted(chain, key=lambda x: x["depth"])


def tool_get_reading_queue(priority=None) -> list:
    queue_path = WIKI_DIR / "queue.md"
    if not queue_path.exists():
        return []

    content = queue_path.read_text()
    items = []
    current_priority = "normal"

    for line in content.split("\n"):
        if line.startswith("### High"):
            current_priority = "high"
        elif line.startswith("### Normal"):
            current_priority = "normal"
        elif line.startswith("- [ ]"):
            if priority and current_priority != priority.lower():
                continue
            # Parse: - [ ] [[slug]] — reason
            match = re.match(r'- \[ \] \[\[([^\]]+)\]\](?:\s*—\s*(.+))?', line)
            if match:
                slug = match.group(1)
                reason = match.group(2) or ""
                items.append({
                    "slug": slug,
                    "priority": current_priority,
                    "reason": reason.strip()
                })

    return items


def tool_add_to_queue(source_iri=None, reference=None, reason="", priority="normal") -> dict:
    queue_path = WIKI_DIR / "queue.md"
    if not queue_path.exists():
        queue_path.write_text("# Reading Queue\n\n### High\n\n### Normal\n")

    content = queue_path.read_text()

    if source_iri:
        _, _, slug = parse_iri(source_iri)
        entry = f"- [ ] [[{slug}]] — {reason}"
    else:
        entry = f"- [ ] {reference} — {reason}"

    section = "### High" if priority.lower() == "high" else "### Normal"

    if section in content:
        content = content.replace(section, f"{section}\n{entry}")
    else:
        content += f"\n{section}\n{entry}\n"

    queue_path.write_text(content)
    return {"success": True, "entry": entry, "priority": priority}


def tool_get_concept_frontier() -> list:
    """Return concepts that need attention most urgently."""
    nodes = load_all_nodes()
    G = get_graph()

    results = []
    for node in nodes:
        iri = node["iri"]
        coverage = node.get("coverage", 0)
        understanding = node.get("understanding", 0)

        # Count inbound edges as proxy for centrality
        inbound_count = G.in_degree(iri) if iri in G else 0

        # Simple priority score: low coverage + high centrality = high priority
        priority_score = (inbound_count * 0.5) + ((5 - coverage) * 0.3) + ((5 - understanding) * 0.2)

        results.append({
            "iri": iri,
            "canonical_title": node["title"],
            "coverage": coverage,
            "understanding": understanding,
            "inbound_refs": inbound_count,
            "priority_score": priority_score
        })

    return sorted(results, key=lambda x: x["priority_score"], reverse=True)[:20]


def tool_get_index(domain=None, node_type=None) -> list:
    nodes = load_all_nodes()
    results = []
    for node in nodes:
        if domain and domain not in node.get("domain", []):
            continue
        if node_type and node["node_type"] != node_type:
            continue
        results.append({
            "iri": node["iri"],
            "canonical_title": node["title"],
            "domain": node["domain"],
            "node_type": node["node_type"],
            "coverage": node["coverage"],
            "understanding": node["understanding"],
            "date_updated": node.get("date_updated", "")
        })
    return sorted(results, key=lambda x: x["canonical_title"])


def tool_get_health_metrics() -> dict:
    nodes = load_all_nodes()
    G = get_graph()

    total = len(nodes)
    sources = [n for n in nodes if n["node_type"] == "sources"]
    concepts = [n for n in nodes if n["node_type"] != "sources"]

    coverages = [n.get("coverage", 0) for n in nodes]
    understandings = [n.get("understanding", 0) for n in nodes]

    cross_domain_edges = sum(
        1 for u, v, d in G.edges(data=True)
        if G.nodes[u].get("domain") != G.nodes[v].get("domain")
    )

    stubs = [n for n in nodes if n.get("coverage", 0) <= 1]
    queue_items = tool_get_reading_queue()

    return {
        "total_nodes": total,
        "total_sources": len(sources),
        "total_concepts": len(concepts),
        "avg_coverage": round(sum(coverages) / total, 2) if total else 0,
        "avg_understanding": round(sum(understandings) / total, 2) if total else 0,
        "cross_domain_connections": cross_domain_edges,
        "queue_depth": len(queue_items),
        "stubs_awaiting_deepening": len(stubs),
        "total_edges": G.number_of_edges()
    }


def tool_check_alias_collision(surface_form: str) -> dict:
    registry = get_alias_registry()
    normalized = surface_form.lower()
    results = []

    for alias, iri in registry.items():
        if normalized in alias or alias in normalized:
            path = find_node_path_by_iri(iri)
            node = load_node(path) if path else {}
            similarity = len(set(normalized.split()) & set(alias.split())) / \
                        max(len(normalized.split()), len(alias.split()), 1)
            results.append({
                "iri": iri,
                "canonical_title": node.get("title", iri),
                "existing_aliases": node.get("aliases", []),
                "similarity_score": similarity
            })

    return {
        "surface_form": surface_form,
        "collision_candidates": sorted(results, key=lambda x: x["similarity_score"], reverse=True)[:5]
    }


def tool_log_operation(operation_type: str, affected_iris: list, summary: str, agent: str) -> dict:
    log_path = WIKI_DIR / "log.md"
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    iris_str = ", ".join(affected_iris)
    entry = f"\n## [{timestamp}] {operation_type} | {agent}\n- {summary}\n- Affected: {iris_str}\n"

    with open(log_path, "a") as f:
        f.write(entry)

    return {"success": True, "timestamp": timestamp}


def tool_register_operational_reference(
    operational_node_id: str,
    iri: str,
    confidence_class: str,
    source_system: str = "mnemon"
) -> dict:
    """Store operational → PKIS bridge reference."""
    bridge_path = WIKI_DIR / "bridge_references.jsonl"
    record = {
        "operational_node_id": operational_node_id,
        "iri": iri,
        "confidence_class": confidence_class,
        "source_system": source_system,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "reference_id": str(uuid.uuid4())[:8]
    }
    with open(bridge_path, "a") as f:
        f.write(json.dumps(record) + "\n")

    return {"success": True, "reference_id": record["reference_id"]}


def tool_get_operational_references(iri: str) -> list:
    bridge_path = WIKI_DIR / "bridge_references.jsonl"
    if not bridge_path.exists():
        return []

    results = []
    with open(bridge_path) as f:
        for line in f:
            try:
                record = json.loads(line)
                if record.get("iri") == iri:
                    results.append(record)
            except json.JSONDecodeError:
                continue

    return results


def tool_get_concept_operational_load(iri: str) -> dict:
    refs = tool_get_operational_references(iri)
    confirmed = [r for r in refs if r.get("confidence_class") == "confirmed"]
    inferred = [r for r in refs if r.get("confidence_class") != "confirmed"]
    systems = list(set(r.get("source_system") for r in refs))
    timestamps = [r.get("timestamp") for r in refs if r.get("timestamp")]

    return {
        "iri": iri,
        "confirmed_refs": len(confirmed),
        "inferred_refs": len(inferred),
        "source_systems": systems,
        "earliest_ref": min(timestamps) if timestamps else None,
        "latest_ref": max(timestamps) if timestamps else None
    }


# ============================================================
# Flask routes — MCP HTTP transport
# ============================================================

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "wiki_dir": str(WIKI_DIR)})


@app.route("/refresh", methods=["POST"])
def refresh():
    """Called by git webhook or cron to invalidate caches."""
    refresh_caches()
    return jsonify({"status": "refreshed"})


def _jsonrpc_error(req_id, code: int, message: str):
    """Build a JSON-RPC 2.0 error response body."""
    return jsonify({
        "jsonrpc": JSONRPC_VERSION,
        "id": req_id,
        "error": {"code": code, "message": message}
    })


def _jsonrpc_result(req_id, result):
    """Build a JSON-RPC 2.0 success response body."""
    return jsonify({
        "jsonrpc": JSONRPC_VERSION,
        "id": req_id,
        "result": result
    })


def _get_tools_list():
    """Return the canonical tools list used by both tools/list and the manifest."""
    return [
        {
            "name": "search_wiki",
            "description": "Search the PKIS wiki using hybrid keyword and structural search. Call this FIRST for any question touching the user's learning domains. Returns ranked concept and source nodes.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "domains": {"type": "array", "items": {"type": "string"}},
                    "node_types": {"type": "array", "items": {"type": "string"}},
                    "max_results": {"type": "integer", "default": 10}
                },
                "required": ["query"]
            }
        },
        {
            "name": "get_node",
            "description": "Retrieve full content of a specific PKIS wiki node by IRI. Use after search_wiki or resolve_concept to get full detail.",
            "inputSchema": {
                "type": "object",
                "properties": {"iri": {"type": "string"}},
                "required": ["iri"]
            }
        },
        {
            "name": "resolve_concept",
            "description": "Resolve a concept name, abbreviation, or alias to its canonical PKIS IRI. Use when the user mentions a concept by name.",
            "inputSchema": {
                "type": "object",
                "properties": {"surface_form": {"type": "string"}},
                "required": ["surface_form"]
            }
        },
        {
            "name": "detect_concepts",
            "description": "Detect which PKIS concepts are present in arbitrary text, even when not explicitly named. Use for implicit concept instantiation.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "threshold": {"type": "number", "default": 0.7}
                },
                "required": ["text"]
            }
        },
        {
            "name": "get_related",
            "description": "Get structurally connected nodes via typed relationship edges. Use to explore concept dependencies and connections.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "iri": {"type": "string"},
                    "edge_types": {"type": "array", "items": {"type": "string"}},
                    "direction": {"type": "string", "enum": ["inbound", "outbound", "both"]},
                    "max_hops": {"type": "integer", "default": 2}
                },
                "required": ["iri"]
            }
        },
        {
            "name": "add_to_queue",
            "description": "Add a source or reference to the reading queue. Use when the user wants to note something for later ingestion.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "source_iri": {"type": "string"},
                    "reference": {"type": "string"},
                    "reason": {"type": "string"},
                    "priority": {"type": "string", "enum": ["high", "normal"]}
                }
            }
        },
        {
            "name": "get_reading_queue",
            "description": "Get the current reading queue contents.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "priority": {"type": "string", "enum": ["high", "normal"]}
                }
            }
        },
        {
            "name": "get_concept_frontier",
            "description": "Get the concepts that most need attention — low coverage, high centrality, or high operational load.",
            "inputSchema": {"type": "object", "properties": {}}
        },
        {
            "name": "get_health_metrics",
            "description": "Get summary health statistics for the wiki.",
            "inputSchema": {"type": "object", "properties": {}}
        }
    ]


def handle_jsonrpc(body):
    """
    Handle a JSON-RPC 2.0 MCP Streamable HTTP request.

    Supported methods:
      initialize            — handshake; returns protocol version + capabilities
      notifications/initialized — client ready notification; return 202
      tools/list            — enumerate available tools
      tools/call            — invoke a tool by name
      ping                  — liveness check
    """
    req_id = body.get("id")
    method = body.get("method", "")
    params = body.get("params") or {}

    if method == "initialize":
        return _jsonrpc_result(req_id, {
            "protocolVersion": MCP_PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "PKIS Wiki", "version": "1.0.0"}
        })

    elif method.startswith("notifications/"):
        # Client-to-server notifications — no response body required
        return Response(status=202)

    elif method == "tools/list":
        return _jsonrpc_result(req_id, {"tools": _get_tools_list()})

    elif method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments") or {}
        if not tool_name:
            return _jsonrpc_error(req_id, -32602, "Missing 'name' in params"), 422
        try:
            result = dispatch_tool(tool_name, tool_args, request)
            return _jsonrpc_result(req_id, {
                "content": [{"type": "text", "text": json.dumps(result, default=str)}]
            })
        except PermissionError as e:
            return _jsonrpc_error(req_id, -32001, str(e)), 403
        except ValueError as e:
            return _jsonrpc_error(req_id, -32601, str(e))
        except Exception as e:
            logger.error(f"tools/call error [{tool_name}]: {e}", exc_info=True)
            return _jsonrpc_error(req_id, -32603, str(e)), 500

    elif method == "ping":
        return _jsonrpc_result(req_id, {})

    else:
        return _jsonrpc_error(req_id, -32601, f"Method not found: {method}"), 404


@app.route("/mcp", methods=["GET", "POST"])
def mcp_endpoint():
    """
    MCP Streamable HTTP transport endpoint.

    GET  → 405 (SSE server-push not implemented)
    POST → JSON-RPC 2.0 if body has {"jsonrpc": "2.0", ...}
           Legacy format {"tool": "...", "params": {...}} still accepted for
           backward compatibility.
    """
    if request.method == "GET":
        return Response("Server-Sent Events not supported", status=405)

    try:
        body = request.get_json(silent=True)
        if not body:
            return jsonify({"error": "Empty or non-JSON request body"}), 400

        # JSON-RPC 2.0 path
        if body.get("jsonrpc") == JSONRPC_VERSION:
            return handle_jsonrpc(body)

        # Legacy path: {"tool": "...", "params": {...}}
        tool_name = body.get("tool")
        params = body.get("params", {})
        if not tool_name:
            return jsonify({"error": "Missing 'tool' or 'jsonrpc' field"}), 400

        result = dispatch_tool(tool_name, params, request)
        return jsonify({"result": result, "error": None})

    except Exception as e:
        logger.error(f"MCP endpoint error: {e}", exc_info=True)
        return jsonify({"result": None, "error": str(e)}), 500


def dispatch_tool(tool_name: str, params: dict, req) -> any:
    """Dispatch tool call to implementation."""

    # Read-only tools — available to all clients
    read_tools = {
        "resolve_concept": lambda p: tool_resolve_concept(p["surface_form"]),
        "resolve_or_detect": lambda p: {
            "registry": tool_resolve_concept(p["text"]),
            "detected": tool_detect_concepts(p["text"], p.get("threshold", 0.7))
        },
        "detect_concepts": lambda p: tool_detect_concepts(
            p["text"], p.get("threshold", 0.7)
        ),
        "get_node": lambda p: tool_get_node(p["iri"]),
        "get_node_stub": lambda p: tool_get_node_stub(p["iri"]),
        "search_wiki": lambda p: tool_search_wiki(
            p["query"],
            domains=p.get("domains"),
            node_types=p.get("node_types"),
            max_results=p.get("max_results", 10)
        ),
        "search_wiki_index": lambda p: tool_search_wiki_index(p["query"]),
        "get_related": lambda p: tool_get_related(
            p["iri"],
            edge_types=p.get("edge_types"),
            direction=p.get("direction", "both"),
            max_hops=p.get("max_hops", 2)
        ),
        "get_dependency_chain": lambda p: tool_get_dependency_chain(p["iri"]),
        "get_reading_queue": lambda p: tool_get_reading_queue(p.get("priority")),
        "add_to_queue": lambda p: tool_add_to_queue(
            source_iri=p.get("source_iri"),
            reference=p.get("reference"),
            reason=p.get("reason", ""),
            priority=p.get("priority", "normal")
        ),
        "get_concept_frontier": lambda p: tool_get_concept_frontier(),
        "get_index": lambda p: tool_get_index(
            domain=p.get("domain"),
            node_type=p.get("node_type")
        ),
        "get_health_metrics": lambda p: tool_get_health_metrics(),
        "check_alias_collision": lambda p: tool_check_alias_collision(p["surface_form"]),
        "get_operational_references": lambda p: tool_get_operational_references(p["iri"]),
        "get_concept_operational_load": lambda p: tool_get_concept_operational_load(p["iri"]),
    }

    # Trusted-only tools — require Bearer token
    trusted_tools = {
        "register_operational_reference": lambda p: tool_register_operational_reference(
            p["operational_node_id"],
            p["iri"],
            p["confidence_class"],
            p.get("source_system", "mnemon")
        ),
        "log_operation": lambda p: tool_log_operation(
            p["operation_type"],
            p.get("affected_iris", []),
            p.get("summary", ""),
            p.get("agent", "unknown")
        ),
    }

    if tool_name in read_tools:
        return read_tools[tool_name](params)
    elif tool_name in trusted_tools:
        if not is_trusted(req):
            raise PermissionError(f"Tool '{tool_name}' requires trusted client token")
        return trusted_tools[tool_name](params)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")


# ============================================================
# MCP manifest — tells Claude what tools are available
# ============================================================

@app.route("/.well-known/mcp", methods=["GET"])
def mcp_manifest():
    """MCP server manifest for Claude connector registration."""
    return jsonify({
        "name": "PKIS Wiki",
        "description": "Personal Knowledge Integration System — semantic wiki covering Bayesian statistics, deep learning, reinforcement learning, causal analysis, knowledge representation, and symbolic/sub-symbolic AI",
        "version": "1.0.0",
        "tools": _get_tools_list()
    })


# ============================================================
# Entry point
# ============================================================

if __name__ == "__main__":
    # Build caches on startup
    logger.info("Building caches on startup...")
    refresh_caches()
    logger.info("PKIS MCP server ready")
    app.run(host="127.0.0.1", port=5000, debug=False)
