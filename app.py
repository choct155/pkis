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
import subprocess
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml
import frontmatter
import networkx as nx
import numpy as np
from rank_bm25 import BM25Okapi
from functools import wraps
from flask import Flask, request, jsonify, Response, send_from_directory
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
    "frameworks", "problems", "principles", "sources",
    "hypotheses", "clusters", "assets", "bridge-notes"
]

FOLDER_TO_TYPE = {
    "concepts":    "concept",
    "techniques":  "technique",
    "results":     "result",
    "frameworks":  "framework",
    "problems":    "problem",
    "principles":  "principle",
    "sources":     "source",
    "hypotheses":  "hypothesis",
    "clusters":    "research-cluster",
    "assets":      "asset",
    "bridge-notes": "bridge-note",
}

TYPE_TO_FOLDER = {v: k for k, v in FOLDER_TO_TYPE.items()}

# Component names per node type — used to compute anatomy_assessed / anatomy_total
COMPONENT_SCORES_BY_TYPE = {
    "concept":   ["definition", "prerequisites", "boundary", "scope", "application", "formal_statement", "dependents", "transfer"],
    "technique": ["operational_mechanism", "principled_mechanism", "conditions", "implementation", "diagnostics", "alternatives", "failure_modes"],
    "framework": ["structure", "purpose", "primitives", "scope", "application", "limits"],
    "result":    ["statement", "proof_sketch", "conditions", "implications", "limitations"],
    "problem":   ["formulation", "why_hard", "solution_landscape", "instances"],
    "principle": ["statement", "justification", "implications", "violations"],
}

STAGING_DIR = Path(os.environ.get("WIKI_DIR", "/home/pkis/pkis-wiki/wiki")) / "staging"

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

# Write endpoint key — separate from read token; required for write operations
WRITE_KEY = os.environ.get("PKIS_MCP_WRITE_KEY", "")

# Document store + Readwise integration
DOCS_DIR          = Path(os.environ.get("DOCS_DIR", "/home/pkis/docs"))
DOCS_BASE_URL     = os.environ.get("DOCS_BASE_URL", "https://pkis.dev/docs")
READWISE_TOKEN    = os.environ.get("READWISE_TOKEN", "")
READWISE_WEBHOOK_SECRET = os.environ.get("READWISE_WEBHOOK_SECRET", "")
DOCS_USERNAME     = os.environ.get("DOCS_USERNAME", "")
DOCS_PASSWORD     = os.environ.get("DOCS_PASSWORD", "")

# MCP JSON-RPC 2.0 Streamable HTTP transport constants
JSONRPC_VERSION = "2.0"
MCP_PROTOCOL_VERSION = "2024-11-05"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 200 * 1024 * 1024  # 200 MB — matches nginx client_max_body_size
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
    # Try the typed directory first (using TYPE_TO_FOLDER for correct mapping)
    folder = TYPE_TO_FOLDER.get(node_type, node_type) if node_type else None
    if folder:
        p = WIKI_DIR / folder / f"{slug}.md"
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
        # Anatomy assessment counts for component_scores
        # node["node_type"] is the folder name; map to singular for COMPONENT_SCORES_BY_TYPE
        node_type_key = FOLDER_TO_TYPE.get(node["node_type"], node["node_type"])
        components = COMPONENT_SCORES_BY_TYPE.get(node_type_key)
        anatomy_total = len(components) if components else 0
        anatomy_assessed = 0
        if components:
            cs = node.get("frontmatter", {}).get("component_scores") or {}
            anatomy_assessed = sum(1 for c in components if cs.get(c) is not None)

        results.append({
            "iri": iri,
            "canonical_title": node["title"],
            "node_type": node["node_type"],
            "domain": node["domain"],
            "score": score,
            "excerpt": node["content"][:300] if node.get("content") else "",
            "coverage": node["coverage"],
            "understanding": node["understanding"],
            "anatomy_assessed": anatomy_assessed,
            "anatomy_total": anatomy_total,
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


def is_write_authorized(req) -> bool:
    """Check if request carries the write endpoint key."""
    if not WRITE_KEY:
        return False
    auth = req.headers.get("Authorization", "")
    return auth == f"Bearer {WRITE_KEY}"


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

    # Build component_scores: return from frontmatter if present, else null-dict for known types
    # node["node_type"] is the folder name (e.g. "techniques"); map to singular for COMPONENT_SCORES_BY_TYPE
    node_type_key = FOLDER_TO_TYPE.get(node["node_type"], node["node_type"])
    fm_component_scores = node["frontmatter"].get("component_scores")
    components = COMPONENT_SCORES_BY_TYPE.get(node_type_key)
    if fm_component_scores is not None:
        component_scores = fm_component_scores
    elif components:
        component_scores = {c: None for c in components}
    else:
        component_scores = None

    return {
        "iri": iri,
        "frontmatter": node["frontmatter"],
        "content": node["content"],
        "related_nodes": related,
        "reading_path": node["frontmatter"].get("reading_path", []),
        "component_scores": component_scores,
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


def tool_get_reading_graph(
    scope: str = "all_unread",
    focus_concept: str = None,
    focus_domain: str = None,
    min_edge_weight: int = 2,
    max_nodes: int = 100,
) -> dict:
    """
    Return the source dependency graph.

    scope:
      "queue_only"  — only the 70 actively-tracked sources
      "all_unread"  — all unread sources (default)
      "full"        — all sources including already-read

    focus_concept / focus_domain: return the subgraph reachable from
    sources that cover the given concept slug or domain tag.

    Returns nodes, edges, clusters, gateway_nodes, suggested_sequence.
    """
    graph_path = WIKI_DIR / "source_graph.json"

    # Auto-build if missing
    if not graph_path.exists():
        try:
            import subprocess as _sp
            script = Path(__file__).parent.parent / "scripts" / "build_source_graph.py"
            if script.exists():
                _sp.run([sys.executable, str(script)], check=True, capture_output=True)
        except Exception as e:
            logger.warning(f"Could not auto-build source graph: {e}")
            return {"error": "source_graph.json not found — run scripts/build_source_graph.py"}

    try:
        graph = json.loads(graph_path.read_text())
    except Exception as e:
        return {"error": f"Could not read source_graph.json: {e}"}

    nodes: dict = graph.get("nodes", {})
    edges: list = graph.get("edges", [])

    # ── apply scope filter ────────────────────────────────────────────────
    if scope == "queue_only":
        keep = {s for s, n in nodes.items() if n.get("in_queue")}
    elif scope == "all_unread":
        keep = {s for s, n in nodes.items() if n.get("status") == "unread"}
    else:  # "full"
        keep = set(nodes.keys())

    # ── apply concept / domain focus ─────────────────────────────────────
    # Focus starts from the *full* nodes dict so 1-hop expansion can surface
    # out-of-scope sources worth adding.  We annotate those with out_of_scope=True.
    if focus_concept:
        seed = {s for s in nodes if focus_concept in nodes[s].get("concepts", [])}
        neighbours = set()
        for e in edges:
            if e["from"] in seed: neighbours.add(e["to"])
            if e["to"]   in seed: neighbours.add(e["from"])
        focus_set = seed | neighbours
        # Annotate nodes outside the original scope
        for s in focus_set - keep:
            nodes[s]["out_of_scope"] = True
        keep = focus_set  # replace keep with focused set

    if focus_domain:
        seed = {s for s in nodes
                if focus_domain in (nodes[s].get("domain") or [])}
        neighbours = set()
        for e in edges:
            if e["from"] in seed: neighbours.add(e["to"])
            if e["to"]   in seed: neighbours.add(e["from"])
        focus_set = seed | neighbours
        for s in focus_set - keep:
            nodes[s]["out_of_scope"] = True
        keep = focus_set

    # ── filter edges ─────────────────────────────────────────────────────
    filtered_edges = [
        e for e in edges
        if e["from"] in keep and e["to"] in keep
        and e["weight"] >= min_edge_weight
    ]

    # ── trim to max_nodes (highest lb_score first) ────────────────────────
    if len(keep) > max_nodes:
        keep = set(sorted(keep, key=lambda s: nodes[s].get("lb_score", 0), reverse=True)[:max_nodes])
        filtered_edges = [e for e in filtered_edges if e["from"] in keep and e["to"] in keep]

    filtered_nodes = {s: nodes[s] for s in keep}

    # ── recalculate gateway nodes for this subgraph ──────────────────────
    has_prereq_inbound = {e["to"] for e in filtered_edges if e["direction"] == "prerequisite"}
    lb_vals = sorted([n.get("lb_score", 0) for n in filtered_nodes.values() if n.get("lb_score", 0) > 0])
    q3 = lb_vals[int(len(lb_vals) * 0.75)] if lb_vals else 0
    gateway_nodes = sorted(
        [s for s, n in filtered_nodes.items()
         if n.get("lb_score", 0) >= q3 and s not in has_prereq_inbound],
        key=lambda s: -filtered_nodes[s].get("lb_score", 0)
    )[:20]

    # ── cluster info for retained nodes ──────────────────────────────────
    cluster_ids_in_view = {n.get("cluster_id") for n in filtered_nodes.values()}
    clusters = {
        str(cid): graph["clusters"].get(str(cid), {})
        for cid in cluster_ids_in_view
        if str(cid) in graph.get("clusters", {})
    }

    # ── suggested sequence (queue items in topological order) ─────────────
    sequence = [s for s in graph.get("suggested_sequence", []) if s in keep]

    return {
        "meta": {
            **graph.get("meta", {}),
            "scope":          scope,
            "nodes_returned": len(filtered_nodes),
            "edges_returned": len(filtered_edges),
            "min_edge_weight": min_edge_weight,
        },
        "nodes":              filtered_nodes,
        "edges":              filtered_edges,
        "clusters":           clusters,
        "gateway_nodes":      gateway_nodes,
        "suggested_sequence": sequence[:30],
    }


def tool_rebuild_source_graph() -> dict:
    """Rebuild wiki/source_graph.json from current wiki state. Run after ingest."""
    try:
        import subprocess as _sp
        script = Path(__file__).parent.parent / "scripts" / "build_source_graph.py"
        result = _sp.run(
            [sys.executable, str(script)],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            return {"status": "error", "detail": result.stderr[:500]}
        graph_path = WIKI_DIR / "source_graph.json"
        meta = json.loads(graph_path.read_text()).get("meta", {})
        return {"status": "rebuilt", **meta}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


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
# Write tool helpers — metadata enrichment
# ============================================================

def _fetch_arxiv_metadata(arxiv_id: str) -> dict:
    """Fetch paper metadata from arXiv Atom API."""
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}&max_results=1"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PKIS-Wiki/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            return {}
        title = entry.findtext("atom:title", namespaces=ns) or ""
        abstract = entry.findtext("atom:summary", namespaces=ns) or ""
        published = entry.findtext("atom:published", namespaces=ns) or ""
        year = int(published[:4]) if published and len(published) >= 4 else None
        authors = [
            a.findtext("atom:name", namespaces=ns) or ""
            for a in entry.findall("atom:author", ns)
        ]
        return {
            "title": title.strip().replace("\n", " "),
            "authors": ", ".join(authors),
            "year": year,
            "abstract": abstract.strip().replace("\n", " "),
            "venue": "arXiv",
            "source_type": "paper",
        }
    except Exception as e:
        logger.error(f"arXiv fetch failed for {arxiv_id}: {e}")
        return {}


def _fetch_crossref_metadata(doi: str) -> dict:
    """Fetch paper metadata from CrossRef API."""
    encoded_doi = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded_doi}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PKIS-Wiki/1.0 (mailto:pkis@pkis.dev)"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        msg = data.get("message", {})
        title = (msg.get("title") or [""])[0]
        authors = ", ".join(
            f"{a.get('given', '')} {a.get('family', '')}".strip()
            for a in msg.get("author", [])
        )
        year = None
        for date_field in ("published-print", "published-online", "created"):
            if date_field in msg:
                parts = msg[date_field].get("date-parts", [[]])
                if parts and parts[0]:
                    year = parts[0][0]
                    break
        abstract = msg.get("abstract", "")
        venue = (msg.get("container-title") or [""])[0]
        return {
            "title": title,
            "authors": authors,
            "year": year,
            "abstract": abstract,
            "venue": venue,
            "source_type": "paper",
        }
    except Exception as e:
        logger.error(f"CrossRef fetch failed for {doi}: {e}")
        return {}


# ============================================================
# Write tool implementations
# ============================================================

def tool_create_bridge_note(
    rationale: str,
    source_context: str = "",
    linked_node_refs: list = None,
    proposed_edge_type: str = "",
    origin: str = "conversation",
    title: str = ""
) -> dict:
    """Create a bridge note in the staging area."""
    if not rationale:
        raise ValueError("rationale is required")

    staged_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y%m%d")
    ts_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Generate a descriptor from the rationale (first 5 meaningful words)
    descriptor_words = re.sub(r'[^a-z0-9\s]', '', rationale.lower()).split()[:5]
    descriptor = "-".join(descriptor_words)
    slug = f"bn-{date_str}-{descriptor}"[:60]

    # Resolve fuzzy references
    # linked_nodes stores plain slugs/refs (no wikilink brackets) for clean YAML frontmatter.
    # The body section wraps them in [[...]] for Obsidian wikilink rendering.
    resolution_candidates = {}
    linked_nodes = []
    if linked_node_refs:
        for ref in (linked_node_refs or []):
            path = find_node_path_by_iri(ref)
            if path:
                node = load_node(path)
                linked_nodes.append(node["slug"])
            else:
                results = hybrid_search(ref, max_results=3)
                if results:
                    resolution_candidates[ref] = [r["iri"] for r in results]
                linked_nodes.append(ref)

    fm = {
        "staged_at": ts_str,
        "staged_by": "mcp-create-bridge-note",
        "staged_id": staged_id,
        "review_status": "pending",
        "proposed_edges": [],
        "title": title or (", ".join(linked_nodes[:3]) + " connection" if linked_nodes else rationale[:80]),
        "knowledge_type": "bridge-note",
        "date_created": now.strftime("%Y-%m-%d"),
        "status": "unreviewed",
        "origin": origin,
        "source_context": source_context,
        "linked_nodes": linked_nodes,
        "proposed_edge_type": proposed_edge_type or "",
        "rationale": rationale,
        "integration_target": "",
    }
    if resolution_candidates:
        fm["resolution_candidates"] = resolution_candidates

    body = f"""## Connection
{rationale}

## Nodes Involved
{chr(10).join(f'- [[{n}]]' for n in linked_nodes) if linked_nodes else '_To be determined_'}

## Integration Notes
Pending review.
"""

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged_path = STAGING_DIR / f"{slug}.md"
    counter = 1
    while staged_path.exists():
        staged_path = STAGING_DIR / f"{slug}-{counter}.md"
        counter += 1

    staged_path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}")

    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(f"\n## [{now.strftime('%Y-%m-%d')}] staged | bridge-note\n- Staged: {staged_path.stem} (id: {staged_id})\n- Rationale: {rationale[:100]}\n")

    return {
        "staged_id": staged_id,
        "staged_at": ts_str,
        "slug": staged_path.stem,
        "resolution_candidates": resolution_candidates,
        "review_url": f"https://github.com/choct155/pkis/blob/main/wiki/staging/{staged_path.name}",
    }


def tool_create_source_stub(
    title: str = "",
    url: str = "",
    doi: str = "",
    authors: str = "",
    year: int = None,
    notes: str = "",
    priority: str = "normal"
) -> dict:
    """Create a source stub in staging with automated metadata enrichment."""
    if not any([title, url, doi]):
        raise ValueError("At least one of title, url, or doi must be provided")

    # ---- Enrichment ----
    metadata = {}
    enrichment_status = "minimal"

    # Detect arXiv
    arxiv_id = None
    if url and "arxiv.org" in url:
        m = re.search(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]+v?[0-9]*)', url)
        if m:
            arxiv_id = m.group(1)
    if arxiv_id:
        metadata = _fetch_arxiv_metadata(arxiv_id)
        if metadata.get("title"):
            enrichment_status = "full" if metadata.get("abstract") else "partial"

    # CrossRef fallback
    if not metadata.get("title") and doi:
        metadata = _fetch_crossref_metadata(doi)
        if metadata.get("title"):
            enrichment_status = "full" if metadata.get("abstract") else "partial"

    # Merge caller-provided fields (override enriched values)
    if title:
        metadata["title"] = title
    if authors:
        metadata["authors"] = authors
    if year:
        metadata["year"] = year

    # ---- Slug generation ----
    final_title = metadata.get("title") or title or doi or url or "unknown"
    final_authors = metadata.get("authors") or authors or ""
    final_year = metadata.get("year") or year

    first_author_last = ""
    if final_authors:
        first_author = final_authors.split(",")[0].strip()
        first_author_last = re.sub(r'[^a-z0-9]', '', first_author.split()[-1].lower()) if first_author else ""

    title_words = re.sub(r'[^a-z0-9\s]', '', final_title.lower()).split()
    key_word = title_words[0] if title_words else "source"
    year_str = str(final_year) if final_year else ""

    slug_parts = [p for p in [first_author_last, key_word, year_str] if p]
    base_slug = "-".join(slug_parts)[:55] if slug_parts else "source-stub"
    slug = base_slug
    counter = 1
    while (STAGING_DIR / f"{slug}.md").exists() or find_node_path(slug):
        slug = f"{base_slug}-{counter}"
        counter += 1

    # ---- Connection candidates ----
    search_text = f"{final_title} {metadata.get('abstract', '')[:400]}"
    connection_candidates = []
    try:
        results = hybrid_search(search_text, max_results=8)
        connection_candidates = [r["iri"] for r in results if r["node_type"] != "sources"]
    except Exception:
        pass

    # ---- Build staged file ----
    staged_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    ts_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    fields_populated = [k for k, v in {
        "title": metadata.get("title"),
        "authors": metadata.get("authors") or authors,
        "year": metadata.get("year") or year,
        "abstract": metadata.get("abstract"),
        "venue": metadata.get("venue"),
    }.items() if v]

    fm = {
        "staged_at": ts_str,
        "staged_by": "mcp-create-source-stub",
        "staged_id": staged_id,
        "review_status": "pending",
        "proposed_edges": [],
        "id": f"pkis:source:{slug}",
        "aliases": [],
        "title": metadata.get("title") or title or "",
        "authors": metadata.get("authors") or authors or "",
        "year": final_year,
        "type": metadata.get("source_type", "paper"),
        "domain": [],
        "tags": [],
        "source_url": url or "",
        "doi": doi or "",
        "drive_id": "",
        "drive_path": "",
        "status": "unread",
        "date_added": now.strftime("%Y-%m-%d"),
        "concepts": [],
        "connection_candidates": connection_candidates[:8],
        "priority": priority,
    }

    abstract = metadata.get("abstract", "")
    body = f"""## Summary
{abstract[:500] if abstract else '[To be filled during ingest]'}

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
{chr(10).join(f'- {iri}' for iri in connection_candidates[:5]) if connection_candidates else '[None identified]'}
{f'{chr(10)}## Notes{chr(10)}{notes}' if notes else ''}
"""

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged_path = STAGING_DIR / f"{slug}.md"
    staged_path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}")

    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(
            f"\n## [{now.strftime('%Y-%m-%d')}] staged | source-stub\n"
            f"- Staged: {slug} (id: {staged_id})\n"
            f"- Title: {metadata.get('title') or title or '(unknown)'}\n"
            f"- Enrichment: {enrichment_status}\n"
        )

    return {
        "staged_id": staged_id,
        "staged_at": ts_str,
        "slug": slug,
        "enrichment_status": enrichment_status,
        "fields_populated": fields_populated,
        "connection_candidates": connection_candidates[:5],
        "review_url": f"https://github.com/choct155/pkis/blob/main/wiki/staging/{staged_path.name}",
    }


def tool_commit_staged_node(
    staged_id: str,
    edits: dict = None,
    confirmed_links: dict = None,
    action: str = "commit"
) -> dict:
    """Promote a reviewed staged node from staging to the live graph."""
    STAGING_DIR.mkdir(parents=True, exist_ok=True)

    # Find staged file by staged_id
    staged_file = None
    for f in STAGING_DIR.glob("*.md"):
        try:
            post = frontmatter.load(str(f))
            if post.metadata.get("staged_id") == staged_id:
                staged_file = f
                break
        except Exception:
            continue

    if not staged_file:
        raise ValueError(f"No staged node found with staged_id: {staged_id}")

    post = frontmatter.load(str(staged_file))
    fm = dict(post.metadata)
    body_content = post.content

    if action == "discard":
        staged_file.unlink()
        log_path = WIKI_DIR / "log.md"
        with open(log_path, "a") as lf:
            lf.write(
                f"\n## [{datetime.now(timezone.utc).strftime('%Y-%m-%d')}] discarded | {fm.get('knowledge_type', 'unknown')}\n"
                f"- Discarded: {staged_file.stem} (id: {staged_id})\n"
            )
        return {"status": "discarded", "staged_id": staged_id}

    # Apply field-level edits
    if edits:
        for key, value in edits.items():
            fm[key] = value

    # Apply confirmed_links: replace fuzzy refs with canonical slug.
    # linked_nodes stores plain refs (no brackets); body has [[ref]] wikilinks.
    if confirmed_links:
        for fuzzy_ref, confirmed_iri in confirmed_links.items():
            _, _nt, slug_part = parse_iri(confirmed_iri)
            if slug_part:
                linked = fm.get("linked_nodes", [])
                # Update frontmatter list: plain ref → plain confirmed slug
                fm["linked_nodes"] = [slug_part if ref == fuzzy_ref else ref for ref in linked]
                # Update body: [[fuzzy_ref]] → [[confirmed-slug]]
                body_content = body_content.replace(f"[[{fuzzy_ref}]]", f"[[{slug_part}]]")

    # Remove staging-only fields
    for field in ["staged_at", "staged_by", "staged_id", "review_status", "proposed_edges",
                  "resolution_candidates", "connection_candidates", "priority"]:
        fm.pop(field, None)

    # Determine knowledge type and target folder
    knowledge_type = fm.get("knowledge_type") or fm.get("type") or "source"
    # Map paper/book/article/talk/video → source
    if knowledge_type in ("paper", "book", "article", "talk", "video"):
        fm["type"] = knowledge_type
        fm.pop("knowledge_type", None)
        knowledge_type = "source"

    folder = TYPE_TO_FOLDER.get(knowledge_type, "sources")
    target_dir = WIKI_DIR / folder
    target_dir.mkdir(parents=True, exist_ok=True)

    slug = staged_file.stem
    target_path = target_dir / f"{slug}.md"

    # Ensure IRI is set
    if "id" not in fm:
        fm["id"] = f"pkis:{knowledge_type}:{slug}"

    # Write promoted file
    new_post = frontmatter.Post(body_content, **fm)
    target_path.write_text(frontmatter.dumps(new_post))
    staged_file.unlink()

    # Invalidate node cache
    global _node_cache
    _node_cache = {}

    # Update index.md
    section_map = {
        "concept": "## Concepts", "technique": "## Techniques",
        "result": "## Results", "framework": "## Frameworks",
        "problem": "## Problems", "principle": "## Principles",
        "source": "## Sources", "hypothesis": "## Hypotheses",
        "research-cluster": "## Research Clusters", "asset": "## Assets",
        "bridge-note": "## Bridge Notes",
    }
    index_path = WIKI_DIR / "index.md"
    if index_path.exists():
        idx_content = index_path.read_text()
        node_domain = fm.get("domain", [])
        domain_str = ", ".join(node_domain) if isinstance(node_domain, list) else str(node_domain)
        now_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        new_entry = f"- [[{slug}]] — {fm.get('title', slug)} ({domain_str}) ({now_date})\n"
        section = section_map.get(knowledge_type, "## Sources")
        if section in idx_content:
            idx_content = idx_content.replace(section + "\n", section + "\n" + new_entry)
        else:
            idx_content += f"\n{section}\n{new_entry}"
        index_path.write_text(idx_content)

    # Append to log.md
    iri = fm.get("id", f"pkis:{knowledge_type}:{slug}")
    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(
            f"\n## [{datetime.now(timezone.utc).strftime('%Y-%m-%d')}] committed | {knowledge_type}\n"
            f"- Committed: {slug} → {folder}/{slug}.md\n"
            f"- IRI: {iri}\n"
        )

    # Git commit and push
    git_sha = ""
    git_pushed = False
    try:
        repo_dir = str(REPO_DIR)
        files_to_add = [str(target_path), str(index_path), str(log_path)]
        subprocess.run(["git", "-C", repo_dir, "add"] + files_to_add, check=True, capture_output=True)
        result = subprocess.run(
            ["git", "-C", repo_dir, "commit", "-m",
             f"[mcp-commit] {knowledge_type}: {fm.get('title', slug)[:60]}"],
            check=True, capture_output=True, text=True
        )
        sha_match = re.search(r'\[.+? ([a-f0-9]{7,})\]', result.stdout)
        git_sha = sha_match.group(1) if sha_match else result.stdout.strip()[:12]
        logger.info(f"Git committed locally: {git_sha}")
        try:
            subprocess.run(["git", "-C", repo_dir, "push"], check=True, capture_output=True, timeout=30)
            git_pushed = True
            logger.info(f"Git pushed: {git_sha}")
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as push_err:
            logger.warning(f"Git push failed (local commit retained): {push_err}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Git commit failed: {e.stderr.decode() if isinstance(e.stderr, bytes) else e.stderr}")

    return {
        "status": "committed",
        "iri": iri,
        "git_commit": git_sha,
        "git_pushed": git_pushed,
        "url": f"https://github.com/choct155/pkis/blob/main/wiki/{folder}/{slug}.md",
    }


def tool_get_staged_nodes(
    node_type: str = None,
    staged_by: str = None,
    limit: int = 20
) -> list:
    """List all pending staged nodes awaiting review."""
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    staged_files = sorted(STAGING_DIR.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    for staged_file in staged_files:
        try:
            post = frontmatter.load(str(staged_file))
            fm = post.metadata
            if fm.get("staged_id") is None:
                continue
            effective_type = fm.get("knowledge_type") or fm.get("type") or "unknown"
            if node_type and effective_type != node_type:
                continue
            if staged_by and fm.get("staged_by") != staged_by:
                continue
            first_line = post.content.strip().split("\n")[0].lstrip("#").strip()[:200] if post.content.strip() else ""
            results.append({
                "staged_id": fm.get("staged_id"),
                "slug": staged_file.stem,
                "node_type": fm.get("knowledge_type") or fm.get("type") or "unknown",
                "staged_at": fm.get("staged_at", ""),
                "staged_by": fm.get("staged_by", ""),
                "title": fm.get("title", staged_file.stem),
                "review_status": fm.get("review_status", "pending"),
                "description": first_line,
                "review_url": f"https://github.com/choct155/pkis/blob/main/wiki/staging/{staged_file.name}",
            })
        except Exception as e:
            logger.error(f"Error reading staged file {staged_file}: {e}")
        if len(results) >= limit:
            break
    return results


# ============================================================
# Document store helpers
# ============================================================

ALLOWED_DOC_EXTENSIONS = {".pdf", ".epub", ".md", ".html", ".txt", ".docx"}


def _require_docs_auth(f):
    """
    Flask decorator: HTTP Basic Auth gated on DOCS_USERNAME / DOCS_PASSWORD env vars.
    If neither is set, the route is unprotected (dev/local mode).
    Applied to /docs/upload, /docs/list, and /docs/sources/<path>.
    /readwise/webhook is intentionally NOT wrapped — Readwise needs public access.
    """
    @wraps(f)
    def _decorated(*args, **kwargs):
        if not DOCS_USERNAME:
            return f(*args, **kwargs)   # no credentials configured — open
        import base64 as _b64
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Basic "):
            try:
                decoded = _b64.b64decode(auth[6:]).decode("utf-8", errors="replace")
                username, _, password = decoded.partition(":")
                if username == DOCS_USERNAME and password == DOCS_PASSWORD:
                    return f(*args, **kwargs)
            except Exception:
                pass
        return Response(
            "Authentication required",
            401,
            {"WWW-Authenticate": 'Basic realm="PKIS Docs"'},
        )
    return _decorated


_SLUG_STOP_WORDS = {
    'a', 'an', 'the', 'to', 'of', 'in', 'on', 'at', 'for', 'with',
    'and', 'or', 'but', 'is', 'are', 'was', 'be', 'as', 'by', 'from',
    'into', 'via', 'its', 'this', 'that', 'some', 'how', 'why', 'when',
    'using', 'toward', 'towards', 'about', 'beyond', 'through',
}


def _compute_slug(title: str, authors: str, year) -> str:
    """
    Derive a slug from paper metadata: {last_name}-{key_title_word}-{year}.
    Skips stop-words and short words when picking the key title word so
    'A Conceptual Introduction…' → 'conceptual', not 'a'.
    Returns a collision-free slug (appends -2, -3, … if needed).
    """
    first_author = (authors or "").split(",")[0].strip()
    last_name = ""
    if first_author:
        last_name = re.sub(r"[^a-z0-9]", "", first_author.split()[-1].lower())

    words = re.sub(r"[^a-z0-9\s]", "", (title or "").lower()).split()
    key_words = [w for w in words if w not in _SLUG_STOP_WORDS and len(w) > 2]
    key_word  = key_words[0] if key_words else (words[0] if words else "source")

    year_str  = str(year) if year else ""
    parts     = [p for p in [last_name, key_word, year_str] if p]
    base      = "-".join(parts)[:55] or "source"

    slug, n = base, 1
    while find_node_path(slug) or (STAGING_DIR / f"{slug}.md").exists():
        slug = f"{base}-{n}"
        n   += 1
    return slug


def _arxiv_url_to_pdf_url(url_or_id: str) -> tuple[str, str]:
    """
    Given an arXiv URL (abs, pdf, html) or bare ID like '1701.02434',
    return (arxiv_id, pdf_fetch_url).
    Returns ('', '') if not recognised as arXiv.
    """
    # Bare ID pattern
    m = re.match(r'^(\d{4}\.\d{4,5})(v\d+)?$', url_or_id.strip())
    if m:
        return m.group(1), f"https://arxiv.org/pdf/{m.group(1)}"
    # URL pattern
    m = re.search(r'arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]+)(v\d+)?', url_or_id)
    if m:
        return m.group(1), f"https://arxiv.org/pdf/{m.group(1)}"
    return "", ""


def _readwise_save(doc_url: str, title: str = "", author: str = "",
                   slug: str = "", abstract: str = "",
                   year: int = None, arxiv_id: str = "") -> dict:
    """
    Push a document to Readwise Reader. Returns Readwise response dict.

    For arXiv papers (arxiv_id provided):
      - Pushes https://ar5iv.org/abs/{id} so Reader gets full article view
        with TTS, proper typography, and highlight support.
      - Records the VPS PDF URL in the document notes for traceability.
      - category: article (not pdf — avoids the embedded viewer)

    For all other documents:
      - Pushes the VPS PDF URL directly.
      - category: pdf

    Full metadata (title, author, summary, published_date) is sent in both
    cases to populate Readwise's document record correctly.
    """
    if not READWISE_TOKEN:
        return {"error": "READWISE_TOKEN not configured"}

    tags = [f"pkis:source:{slug}"] if slug else []

    if arxiv_id:
        push_url = f"https://ar5iv.org/abs/{arxiv_id}"
        category = "article"
        notes    = f"VPS copy: {doc_url}"
    else:
        push_url = doc_url
        category = "pdf"
        notes    = ""

    payload: dict = {
        "url":      push_url,
        "location": "new",   # "new" = Inbox; "later" = Later shelf (not visible in inbox)
        "category": category,
    }
    if title:    payload["title"]          = title
    if author:   payload["author"]         = author
    if tags:     payload["tags"]           = tags
    if abstract: payload["summary"]        = abstract[:600]
    if year:     payload["published_date"] = f"{year}-01-01T00:00:00+00:00"
    if notes:    payload["notes"]          = notes

    try:
        data = json.dumps(payload).encode()
        req = urllib.request.Request(
            "https://readwise.io/api/v3/save/",
            data=data,
            headers={
                "Authorization": f"Token {READWISE_TOKEN}",
                "Content-Type":  "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        logger.error(f"Readwise save failed: {e}")
        return {"error": str(e)}


def _find_source_by_readwise_id(readwise_id: str) -> Optional[str]:
    """Find a source node's slug given its Readwise document ID."""
    if not readwise_id:
        return None
    for node in load_all_nodes():
        if node.get("node_type") == "sources":
            if node.get("frontmatter", {}).get("readwise_id") == readwise_id:
                return node["slug"]
    return None


def _update_source_frontmatter(slug: str, updates: dict) -> bool:
    """Apply field-level updates to a source node's frontmatter in place."""
    path = find_node_path(slug)
    if not path:
        return False
    try:
        post = frontmatter.load(str(path))
        for key, value in updates.items():
            post.metadata[key] = value
        path.write_text(frontmatter.dumps(post))
        global _node_cache
        _node_cache = {}
        return True
    except Exception as e:
        logger.error(f"Frontmatter update failed for {slug}: {e}")
        return False


def _git_commit_files(files: list, message: str) -> str:
    """Stage, commit, and push a list of file paths. Returns SHA or ''."""
    git_sha = ""
    try:
        subprocess.run(
            ["git", "-C", str(REPO_DIR), "add"] + [str(f) for f in files],
            check=True, capture_output=True
        )
        result = subprocess.run(
            ["git", "-C", str(REPO_DIR), "commit", "-m", message],
            check=True, capture_output=True, text=True
        )
        m = re.search(r'\[.+? ([a-f0-9]{7,})\]', result.stdout)
        git_sha = m.group(1) if m else result.stdout.strip()[:12]
        subprocess.run(
            ["git", "-C", str(REPO_DIR), "push"],
            check=True, capture_output=True, timeout=30
        )
    except Exception as e:
        logger.error(f"Git commit failed: {e}")
    return git_sha


def _append_reading_notes(source_slug: str, text: str, note: str,
                           highlight_id: str) -> Path:
    """
    Append an untagged highlight to a per-source reading-notes staging file.
    Creates the file if it doesn't exist.
    """
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    notes_path = STAGING_DIR / f"{source_slug}-reading-notes.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if not notes_path.exists():
        fm = {
            "knowledge_type":  "reading-notes",
            "source":          source_slug,
            "staged_at":       ts,
            "staged_by":       "readwise-webhook",
            "review_status":   "pending",
        }
        notes_path.write_text(
            f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n"
            f"# Reading Notes — {source_slug}\n\n"
        )

    with open(notes_path, "a", encoding="utf-8") as f:
        f.write(f"\n## Highlight `{highlight_id[:8]}`\n")
        f.write(f"> {text}\n")
        if note:
            f.write(f"\n**Note:** {note}\n")
        f.write(f"\n*{ts}*\n")

    return notes_path


def _route_highlight(payload: dict, source_slug: str) -> dict:
    """
    Route a Readwise highlight based on its tags:
      #bridge      → staged bridge note
      #stub        → append to reading-notes with stub flag
      #concept:X   → append to reading-notes with concept tag
      (none)       → append to reading-notes for Librarian review
    """
    text         = (payload.get("text") or payload.get("content") or "").strip()
    note         = (payload.get("note") or "").strip()
    highlight_id = str(payload.get("id", ""))
    raw_tags     = payload.get("tags") or []
    tags         = [t["name"] if isinstance(t, dict) else str(t) for t in raw_tags]

    if not text:
        return {"action": "skipped", "reason": "empty highlight"}

    # ── #bridge → staged bridge note ─────────────────────────────────────
    if "bridge" in tags:
        rationale = note if note else text
        result = tool_create_bridge_note(
            rationale=rationale,
            title=text[:80] if note else "",
            source_context=source_slug,
            origin="reading",
        )
        return {"action": "bridge_note", "staged_id": result.get("staged_id")}

    # ── #stub → reading-notes with stub flag ─────────────────────────────
    if "stub" in tags:
        path = _append_reading_notes(source_slug, text, f"[STUB CANDIDATE] {note}", highlight_id)
        return {"action": "stub_candidate", "notes_file": path.name}

    # ── #concept:X → reading-notes with concept annotation ───────────────
    concept_tags = [t[len("concept:"):] for t in tags if t.startswith("concept:")]
    if concept_tags:
        path = _append_reading_notes(
            source_slug, text,
            f"[CONCEPT: {', '.join(concept_tags)}] {note}",
            highlight_id
        )
        return {"action": "concept_enrichment",
                "concepts": concept_tags, "notes_file": path.name}

    # ── default → reading-notes ───────────────────────────────────────────
    path = _append_reading_notes(source_slug, text, note, highlight_id)
    return {"action": "reading_note", "notes_file": path.name}


# ── Auto source node creation on upload ──────────────────────────────────────

def _arxiv_id_from_filename(filename: str) -> str:
    """
    Extract an arXiv ID from a filename like '1701.02434v2.pdf' or
    '2301.07041.pdf'.  Returns '' if no arXiv ID pattern is found.
    """
    stem = Path(filename).stem          # e.g. '1701.02434v2'
    m = re.match(r'^(\d{4}\.\d{4,5})(v\d+)?$', stem)
    return m.group(1) if m else ""


def _auto_create_source_node(slug: str, filename: str,
                              fetch_url: str = "") -> dict:
    """
    Create a live wiki/sources/{slug}.md entry automatically when a document
    is uploaded for an unknown slug.  Tries arXiv enrichment first (from the
    filename pattern); falls back to a bare stub.

    Returns the frontmatter dict of the newly created node so the caller can
    proceed with a Readwise push without reloading from disk.
    """
    now  = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    # ── Try metadata enrichment ───────────────────────────────────────────
    metadata: dict = {}
    source_url = ""

    arxiv_id = _arxiv_id_from_filename(filename)
    if not arxiv_id and fetch_url and "arxiv.org" in fetch_url:
        m = re.search(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]+)', fetch_url)
        if m:
            arxiv_id = m.group(1)

    if arxiv_id:
        metadata   = _fetch_arxiv_metadata(arxiv_id)
        source_url = f"https://arxiv.org/abs/{arxiv_id}"

    title   = metadata.get("title")   or slug.replace("-", " ").title()
    authors = metadata.get("authors") or ""
    year    = metadata.get("year")
    abstract = metadata.get("abstract", "")

    doc_path = f"sources/{slug}/{filename}"

    # ── Build source file ─────────────────────────────────────────────────
    fm = {
        "id":          f"pkis:source:{slug}",
        "aliases":     [],
        "title":       title,
        "authors":     authors,
        "year":        year,
        "type":        metadata.get("source_type", "paper"),
        "domain":      [],
        "tags":        [],
        "source_url":  source_url,
        "drive_id":    "",
        "drive_path":  "",
        "doc_path":    doc_path,
        "readwise_id": "",
        "isbn":        "",
        "toc_source":  "",
        "parent_book": "",
        "chapter":     None,
        "status":      "unread",
        "date_added":  today,
        "date_read":   "",
        "concepts":    [],
    }
    body_summary = (abstract[:600] + "…") if len(abstract) > 600 else abstract
    body = (
        f"## Summary\n"
        f"{body_summary if body_summary else '[To be filled by Librarian ingest]'}\n\n"
        f"## Key Knowledge Objects\n[To be identified during Librarian ingest]\n\n"
        f"## Key Extractions\n[To be identified during Librarian ingest]\n\n"
        f"## Connection Candidates\n[To be identified during Librarian ingest]\n"
    )

    dest = WIKI_DIR / "sources" / f"{slug}.md"
    dest.write_text(
        f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}"
    )

    # Invalidate node cache so subsequent lookups see the new node
    global _node_cache
    _node_cache = {}

    enrichment = "arxiv" if arxiv_id and metadata.get("title") else "minimal"
    logger.info(f"Auto-created source node {slug} (enrichment={enrichment})")
    return {**fm, "_enrichment": enrichment,
            "_arxiv_id": arxiv_id, "_abstract": abstract}


# ── Cross-store duplicate detection ──────────────────────────────────────────

def _find_duplicate_doc(file_bytes: bytes,
                        exclude_path: Path = None) -> Optional[tuple[str, str]]:
    """
    Scan every file in DOCS_DIR/sources/ for content identical to file_bytes.
    Uses file-size as a pre-filter so only same-size files are hashed.
    exclude_path: skip this exact path (allows same-slug/same-name overwrites
                  with different content — the annotated replacement workflow).
    Returns (slug, filename) of the first match, or None.
    """
    incoming_size = len(file_bytes)
    incoming_hash: str = ""           # computed lazily on first size match

    sources_dir = DOCS_DIR / "sources"
    if not sources_dir.exists():
        return None

    for slug_dir in sources_dir.iterdir():
        if not slug_dir.is_dir():
            continue
        for f in slug_dir.iterdir():
            if f.suffix.lower() not in ALLOWED_DOC_EXTENSIONS:
                continue
            if exclude_path and f.resolve() == exclude_path.resolve():
                continue
            try:
                if f.stat().st_size != incoming_size:
                    continue
                if not incoming_hash:
                    incoming_hash = hashlib.sha256(file_bytes).hexdigest()
                if hashlib.sha256(f.read_bytes()).hexdigest() == incoming_hash:
                    return (slug_dir.name, f.name)
            except OSError:
                continue
    return None


# ── MCP tool functions ────────────────────────────────────────────────────────

def tool_upload_document(
    slug: str,
    filename: str,
    fetch_url: str = "",
    content_b64: str = "",
    push_to_readwise: bool = True,
) -> dict:
    """
    Store a document in the doc store for a given source slug.
    Provide either fetch_url (VPS fetches the file) or content_b64 (base64 payload).
    Optionally pushes the served URL to Readwise Reader.

    Duplicate detection (content-hash):
    - Same content + different filename → rejected with name of existing file
    - Same filename + same content     → rejected as already uploaded (no-op)
    - Same filename + different content → allowed (annotated replacement workflow)
    """
    import base64 as _b64

    if not slug:
        raise ValueError("slug is required")
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_DOC_EXTENSIONS:
        raise ValueError(f"Extension {ext} not allowed. Permitted: {ALLOWED_DOC_EXTENSIONS}")

    # ── Fetch bytes into memory first (needed for hash check) ────────────────
    if fetch_url:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": "PKIS/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            file_bytes = resp.read()
    elif content_b64:
        file_bytes = _b64.b64decode(content_b64)
    else:
        raise ValueError("Either fetch_url or content_b64 must be provided")

    # ── Cross-store duplicate check ───────────────────────────────────────────
    dest_dir  = DOCS_DIR / "sources" / slug
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / filename

    # exclude_path = dest_path so same-slug/same-name with NEW content is allowed
    # (annotated PDF replacing pristine copy)
    dup = _find_duplicate_doc(file_bytes, exclude_path=dest_path)
    if dup:
        dup_slug, dup_file = dup
        if dup_slug == slug:
            raise ValueError(
                f"Duplicate: identical content already stored as "
                f"'{dup_file}' under source '{slug}'. Upload rejected."
            )
        else:
            raise ValueError(
                f"Duplicate: identical content already stored as "
                f"'{dup_file}' under source '{dup_slug}'. Upload rejected."
            )

    # ── Write ────────────────────────────────────────────────────────────────
    dest_path.write_bytes(file_bytes)

    doc_url  = f"{DOCS_BASE_URL}/sources/{slug}/{filename}"
    doc_path = f"sources/{slug}/{filename}"

    # ── Ensure a wiki source node exists ────────────────────────────────────
    node_path = find_node_path(slug)
    auto_created = False
    if not node_path:
        auto_fm = _auto_create_source_node(slug, filename, fetch_url=fetch_url)
        node_path = find_node_path(slug)
        auto_created = True

    node    = load_node(node_path) if node_path else None
    title   = node["title"]                          if node else ""
    authors = node["frontmatter"].get("authors", "") if node else ""
    year    = node["frontmatter"].get("year")        if node else None

    # ── Resolve arXiv ID + abstract for enriched Readwise push ──────────────
    if auto_created:
        arxiv_id = auto_fm.get("_arxiv_id", "")
        abstract = auto_fm.get("_abstract", "")
    else:
        # Existing node — try to extract arXiv ID from source_url or filename
        arxiv_id = _arxiv_id_from_filename(filename)
        if not arxiv_id and node:
            src_url = node["frontmatter"].get("source_url", "")
            m = re.search(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]+)', src_url)
            if m:
                arxiv_id = m.group(1)
        abstract = ""
        if arxiv_id:
            meta = _fetch_arxiv_metadata(arxiv_id)
            abstract = meta.get("abstract", "")

    # ── Readwise push ────────────────────────────────────────────────────────
    readwise_result = {}
    fm_updates: dict = {"doc_path": doc_path}
    if push_to_readwise and READWISE_TOKEN:
        readwise_result = _readwise_save(
            doc_url, title=title, author=authors, slug=slug,
            abstract=abstract, year=year, arxiv_id=arxiv_id,
        )
        if readwise_result.get("id"):
            fm_updates["readwise_id"] = readwise_result["id"]

    # ── Persist frontmatter + commit ─────────────────────────────────────────
    if node_path:
        _update_source_frontmatter(slug, fm_updates)
        _git_commit_files(
            [node_path],
            f"[doc-store] {'auto-create + ' if auto_created else ''}add doc: {slug}/{filename}"
        )

    return {
        "slug":              slug,
        "filename":          filename,
        "doc_url":           doc_url,
        "source_auto_created": auto_created,
        "readwise_pushed":   bool(readwise_result.get("id")),
        "readwise_url":      readwise_result.get("url", ""),
        "readwise_id":       readwise_result.get("id", ""),
    }


def tool_list_documents(slug: str = None) -> list:
    """List stored documents, optionally filtered to a single source slug."""
    sources_dir = DOCS_DIR / "sources"
    if not sources_dir.exists():
        return []
    results = []
    search_dirs = [sources_dir / slug] if slug else sorted(sources_dir.iterdir())
    for d in search_dirs:
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if f.suffix.lower() in ALLOWED_DOC_EXTENSIONS:
                results.append({
                    "slug":     d.name,
                    "filename": f.name,
                    "url":      f"{DOCS_BASE_URL}/sources/{d.name}/{f.name}",
                    "size_kb":  round(f.stat().st_size / 1024, 1),
                    "modified": datetime.fromtimestamp(
                        f.stat().st_mtime, tz=timezone.utc
                    ).strftime("%Y-%m-%dT%H:%M:%SZ"),
                })
    return results


# ============================================================
# Flask routes — Document store + Readwise webhook
# ============================================================

_UPLOAD_FORM = """<!DOCTYPE html>
<html><head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>PKIS Upload</title>
<style>
  body {{ font-family: system-ui, sans-serif; max-width: 520px;
          margin: 40px auto; padding: 0 16px; }}
  label {{ display: block; margin: 12px 0 4px; font-weight: 600; }}
  input {{ width: 100%; padding: 8px; box-sizing: border-box;
           font-size: 16px; border: 1px solid #ccc; border-radius: 4px; }}
  .hint {{ font-size: 13px; color: #666; margin: 2px 0 0; }}
  .divider {{ text-align: center; color: #999; margin: 16px 0 4px;
              font-size: 13px; font-style: italic; }}
  button {{ margin-top: 16px; width: 100%; padding: 12px;
            background: #1a56db; color: white; border: none;
            border-radius: 4px; font-size: 16px; cursor: pointer; }}
  .msg {{ margin-top: 16px; padding: 12px; border-radius: 4px; }}
  .ok  {{ background: #d1fae5; color: #065f46; }}
  .err {{ background: #fee2e2; color: #991b1b; }}
</style></head><body>
<h2>PKIS Doc Upload</h2>
{msg}
<form method="POST" enctype="multipart/form-data">
  <label>arXiv URL / ID or direct PDF URL <span style="font-weight:400">(optional)</span></label>
  <input name="source_url" placeholder="https://arxiv.org/abs/1701.02434  or  1701.02434"
         value="{source_url}" autocomplete="off">
  <p class="hint">arXiv papers: PDF fetched automatically, Reader gets the HTML version.</p>

  <div class="divider">— or attach a file —</div>

  <label>File <span style="font-weight:400">(optional when URL given)</span></label>
  <input type="file" name="file" accept=".pdf,.epub,.md,.html,.txt,.docx">

  <label>Slug <span style="font-weight:400">(leave blank to auto-compute)</span></label>
  <input name="slug" placeholder="auto-computed from metadata" value="{slug}"
         autocomplete="off">
  <p class="hint">Override only if you want a specific identifier, e.g. betancourt-hmc.</p>

  <label style="margin-top:14px">
    <input type="checkbox" name="push_readwise" value="1" {rw_checked}>
    Push to Readwise Reader
  </label>
  <button type="submit" id="submitBtn">Upload</button>
</form>
<script>
document.getElementById('submitBtn').addEventListener('click', function() {{
  var f = this.form;
  var hasInput = f.source_url.value.trim() || f.file.files.length > 0;
  if (hasInput) {{
    var btn = this;
    // defer so the click event + form submit fire before the button is disabled
    setTimeout(function() {{ btn.disabled = true; btn.textContent = 'Uploading…'; }}, 0);
  }}
}});
</script>
</body></html>"""


@app.route("/docs/upload", methods=["GET", "POST"])
@_require_docs_auth
def docs_upload():
    """HTML upload form — protected by HTTP Basic Auth (DOCS_USERNAME/DOCS_PASSWORD)."""
    msg        = ""
    slug_val   = ""
    src_url_val = ""
    rw_checked = "checked" if READWISE_TOKEN else ""

    if request.method == "POST":
        slug_val    = request.form.get("slug", "").strip()
        src_url_val = request.form.get("source_url", "").strip()
        push_rw     = bool(request.form.get("push_readwise"))
        file        = request.files.get("file")
        has_file    = bool(file and file.filename)

        if not src_url_val and not has_file:
            msg = '<div class="msg err">Provide a URL or a file (or both).</div>'
        else:
            try:
                # ── Resolve fetch_url and filename ───────────────────────────
                fetch_url = ""
                filename  = ""

                if src_url_val:
                    arxiv_id, pdf_url = _arxiv_url_to_pdf_url(src_url_val)
                    if pdf_url:
                        fetch_url = pdf_url
                        filename  = f"{arxiv_id}.pdf"
                    elif src_url_val.lower().endswith(tuple(ALLOWED_DOC_EXTENSIONS)):
                        fetch_url = src_url_val
                        filename  = Path(urllib.parse.urlparse(src_url_val).path).name
                    else:
                        raise ValueError(
                            f"URL not recognised as arXiv or a direct document link: {src_url_val}"
                        )

                # File takes priority over URL-derived filename if both given
                content_b64 = ""
                if has_file:
                    import base64 as _b64
                    content_b64 = _b64.b64encode(file.read()).decode()
                    filename    = Path(file.filename).name
                    fetch_url   = ""   # don't double-fetch

                if not filename:
                    raise ValueError("Could not determine filename.")

                # ── Auto-compute slug if not provided ────────────────────────
                if not slug_val:
                    # Try arXiv metadata first
                    arxiv_id_for_slug, _ = _arxiv_url_to_pdf_url(src_url_val) if src_url_val else ("", "")
                    if not arxiv_id_for_slug:
                        arxiv_id_for_slug = _arxiv_id_from_filename(filename)
                    if arxiv_id_for_slug:
                        meta = _fetch_arxiv_metadata(arxiv_id_for_slug)
                        slug_val = _compute_slug(
                            meta.get("title", ""), meta.get("authors", ""), meta.get("year")
                        )
                    else:
                        # Fallback: clean filename stem
                        stem = re.sub(r'[^a-z0-9]+', '-', Path(filename).stem.lower()).strip('-')
                        slug_val = stem[:55] or "source"

                result = tool_upload_document(
                    slug=slug_val,
                    filename=filename,
                    fetch_url=fetch_url,
                    content_b64=content_b64,
                    push_to_readwise=push_rw and bool(READWISE_TOKEN),
                )
                rw_note  = (f" · <a href='{result['readwise_url']}'>Open in Reader</a>"
                            if result.get("readwise_url") else "")
                new_node = " · wiki node created" if result.get("source_auto_created") else ""
                msg = (f'<div class="msg ok">Stored as <strong>{result["slug"]}</strong>: '
                       f'<a href="{result["doc_url"]}">{filename}</a>{rw_note}{new_node}</div>')
                slug_val = src_url_val = ""
            except Exception as e:
                msg = f'<div class="msg err">Error: {e}</div>'

    return _UPLOAD_FORM.format(
        msg=msg, slug=slug_val, source_url=src_url_val, rw_checked=rw_checked
    )


@app.route("/docs/list", methods=["GET"])
@_require_docs_auth
def docs_list():
    """JSON listing of stored documents — protected by Basic Auth."""
    slug = request.args.get("slug")
    return jsonify(tool_list_documents(slug))


@app.route("/docs/sources/<path:filepath>")
def docs_serve(filepath: str):
    """
    Serve files from the document store (NO auth — Readwise must be able to fetch).
    URL pattern: /docs/sources/<slug>/<filename>
    Maps to DOCS_DIR/sources/<slug>/<filename> on disk.

    The management endpoints (/docs/upload, /docs/list) are auth-protected;
    the file URLs themselves are public-but-opaque (slug + filename required).
    If we ever need stronger file security, replace with a signed-token scheme.

    send_from_directory handles path-traversal protection automatically.
    """
    sources_dir = DOCS_DIR / "sources"
    return send_from_directory(str(sources_dir), filepath)


# ── Readwise webhook ──────────────────────────────────────────────────────────

@app.route("/readwise/webhook", methods=["POST"])
def readwise_webhook():
    """
    Receive Readwise webhook events and route them:

    reader.document.finished / .archived
      → update source status: read + date_read + git commit

    readwise.highlight.created
      → route by highlight tags (#bridge / #stub / #concept:X / default)
    """
    # force=True: parse regardless of Content-Type header
    # silent=True: return None instead of raising on bad/empty body
    payload = request.get_json(force=True, silent=True) or {}

    # Verify shared secret (Readwise includes it in the payload body)
    if READWISE_WEBHOOK_SECRET:
        if payload.get("secret") != READWISE_WEBHOOK_SECRET:
            logger.warning("Readwise webhook: invalid secret")
            return jsonify({"error": "invalid secret"}), 401

    event_type = payload.get("event_type", "")
    logger.info(f"Readwise webhook: {event_type}")

    # ── document finished / archived → mark read ─────────────────────────
    if event_type in ("reader.document.finished", "reader.document.archived"):
        doc_id   = payload.get("id", "")
        # Try readwise_id lookup first, fall back to pkis tag in document tags
        slug = _find_source_by_readwise_id(doc_id)
        if not slug:
            for tag in (payload.get("tags") or []):
                name = tag["name"] if isinstance(tag, dict) else str(tag)
                if name.startswith("pkis:source:"):
                    slug = name[len("pkis:source:"):]
                    break

        if slug:
            date_read = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            if _update_source_frontmatter(slug, {"status": "read", "date_read": date_read}):
                source_path = find_node_path(slug)
                if source_path:
                    sha = _git_commit_files(
                        [source_path],
                        f"[readwise] mark read: {slug}"
                    )
                    logger.info(f"Marked {slug} read (commit {sha})")
                return jsonify({"status": "marked_read", "slug": slug})
        else:
            logger.warning(f"Readwise webhook: no PKIS source found for id={doc_id}")
        return jsonify({"status": "no_match"})

    # ── highlight created → route by tags ────────────────────────────────
    if event_type == "readwise.highlight.created":
        book_id = payload.get("book_id", "")
        slug    = _find_source_by_readwise_id(book_id)
        if not slug:
            # Fall back: check if source slug is in the document URL
            logger.warning(f"Readwise webhook: no source for book_id={book_id}")
            return jsonify({"status": "no_source_match"})

        result = _route_highlight(payload, slug)
        logger.info(f"Highlight routed: {result.get('action')} for {slug}")
        return jsonify({"status": "ok", "route": result})

    # ── other events — log and acknowledge ───────────────────────────────
    logger.info(f"Readwise webhook: unhandled event {event_type!r}")
    return jsonify({"status": "acknowledged", "event_type": event_type})


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
        },
        {
            "name": "get_reading_graph",
            "description": "Return the source dependency graph — nodes are sources, edges encode conceptual overlap and inferred prerequisite order. Use to answer: what should I read first? what is load-bearing? what does reading X unlock? Supports scoping to queue items, all unread, or the full corpus; can focus on a concept or domain.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "scope": {
                        "type": "string",
                        "enum": ["queue_only", "all_unread", "full"],
                        "default": "all_unread",
                        "description": "queue_only: 70 actively tracked sources; all_unread: full unread corpus; full: everything"
                    },
                    "focus_concept": {
                        "type": "string",
                        "description": "Concept slug — return subgraph of sources covering this concept plus 1-hop neighbours"
                    },
                    "focus_domain": {
                        "type": "string",
                        "description": "Domain tag (e.g. 'knowledge-representation') — restrict to sources in that domain"
                    },
                    "min_edge_weight": {
                        "type": "integer",
                        "default": 2,
                        "description": "Minimum shared concepts to show an edge. Higher = sparser, more confident connections"
                    },
                    "max_nodes": {
                        "type": "integer",
                        "default": 100,
                        "description": "Cap on nodes returned (highest load-bearing first)"
                    }
                }
            }
        },
        {
            "name": "get_staged_nodes",
            "description": "List all staged nodes awaiting review. Use to check what's pending in the two-phase write queue.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "node_type": {"type": "string"},
                    "staged_by": {"type": "string"},
                    "limit": {"type": "integer", "default": 20}
                }
            }
        },
        {
            "name": "create_bridge_note",
            "description": "Capture an epiphany or cross-domain connection. Creates a staged bridge note for later review. Accepts fuzzy node references — they are resolved to candidates automatically.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "rationale": {"type": "string", "description": "The insight or connection being captured"},
                    "title": {"type": "string", "description": "Short title for the bridge note (auto-generated from linked nodes if omitted)"},
                    "source_context": {"type": "string", "description": "Fuzzy reference to what prompted this"},
                    "linked_node_refs": {"type": "array", "items": {"type": "string"}, "description": "Node IRIs or fuzzy text references"},
                    "proposed_edge_type": {"type": "string", "description": "One of the 8 relationship predicates"},
                    "origin": {"type": "string", "enum": ["voice-capture", "conversation", "reading", "spontaneous"], "default": "conversation"}
                },
                "required": ["rationale"]
            }
        },
        {
            "name": "create_source_stub",
            "description": "Register a new source from any identifying fragment. Enriches metadata from arXiv, CrossRef, or Semantic Scholar. Creates a staged stub for Librarian review.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "url": {"type": "string", "description": "arXiv URL, DOI URL, blog URL, etc."},
                    "doi": {"type": "string"},
                    "authors": {"type": "string"},
                    "year": {"type": "integer"},
                    "notes": {"type": "string"},
                    "priority": {"type": "string", "enum": ["high", "normal"], "default": "normal"}
                }
            }
        },
        {
            "name": "commit_staged_node",
            "description": "Promote a reviewed staged node to the live wiki graph. Commits and pushes to git. Use after reviewing a staged node via get_staged_nodes.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "staged_id": {"type": "string", "description": "UUID from create_bridge_note or create_source_stub"},
                    "edits": {"type": "object", "description": "Field-level edits to apply before committing"},
                    "confirmed_links": {"type": "object", "description": "Resolution of fuzzy refs: {fuzzy_ref: confirmed_iri}"},
                    "action": {"type": "string", "enum": ["commit", "discard"], "default": "commit"}
                },
                "required": ["staged_id"]
            }
        },
        {
            "name": "rebuild_source_graph",
            "description": "Rebuild wiki/source_graph.json from current wiki state. Call after ingesting new sources or marking sources as read. Returns updated graph metadata.",
            "inputSchema": {"type": "object", "properties": {}}
        },
        {
            "name": "upload_document",
            "description": "Store a source document in the PKIS doc store and optionally push it to Readwise Reader. Provide either fetch_url (VPS fetches the file) or content_b64 (base64-encoded bytes).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "slug":             {"type": "string", "description": "Source slug, e.g. hastie-esl-ch08"},
                    "filename":         {"type": "string", "description": "Filename to store as, e.g. hastie-esl-ch08.pdf"},
                    "fetch_url":        {"type": "string", "description": "URL the VPS should fetch the file from"},
                    "content_b64":      {"type": "string", "description": "Base64-encoded file content"},
                    "push_to_readwise": {"type": "boolean", "default": True,
                                        "description": "Push the doc URL to Readwise Reader after storing"}
                },
                "required": ["slug", "filename"]
            }
        },
        {
            "name": "list_documents",
            "description": "List documents stored in the PKIS doc store, optionally filtered to a single source slug.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "slug": {"type": "string", "description": "Filter to a specific source slug"}
                }
            }
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
        "get_reading_graph": lambda p: tool_get_reading_graph(
            scope=p.get("scope", "all_unread"),
            focus_concept=p.get("focus_concept"),
            focus_domain=p.get("focus_domain"),
            min_edge_weight=p.get("min_edge_weight", 2),
            max_nodes=p.get("max_nodes", 100),
        ),
        "get_index": lambda p: tool_get_index(
            domain=p.get("domain"),
            node_type=p.get("node_type")
        ),
        "get_health_metrics": lambda p: tool_get_health_metrics(),
        "list_documents": lambda p: tool_list_documents(p.get("slug")),
        "check_alias_collision": lambda p: tool_check_alias_collision(p["surface_form"]),
        "get_operational_references": lambda p: tool_get_operational_references(p["iri"]),
        "get_concept_operational_load": lambda p: tool_get_concept_operational_load(p["iri"]),
    }

    # Trusted-only tools — require PKIS_TRUSTED_TOKEN
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

    # Write tools — require PKIS_MCP_WRITE_KEY
    write_tools = {
        "create_bridge_note": lambda p: tool_create_bridge_note(
            rationale=p["rationale"],
            title=p.get("title", ""),
            source_context=p.get("source_context", ""),
            linked_node_refs=p.get("linked_node_refs"),
            proposed_edge_type=p.get("proposed_edge_type", ""),
            origin=p.get("origin", "conversation"),
        ),
        "create_source_stub": lambda p: tool_create_source_stub(
            title=p.get("title", ""),
            url=p.get("url", ""),
            doi=p.get("doi", ""),
            authors=p.get("authors", ""),
            year=p.get("year"),
            notes=p.get("notes", ""),
            priority=p.get("priority", "normal"),
        ),
        "commit_staged_node": lambda p: tool_commit_staged_node(
            staged_id=p["staged_id"],
            edits=p.get("edits"),
            confirmed_links=p.get("confirmed_links"),
            action=p.get("action", "commit"),
        ),
        "get_staged_nodes": lambda p: tool_get_staged_nodes(
            node_type=p.get("node_type"),
            staged_by=p.get("staged_by"),
            limit=p.get("limit", 20),
        ),
        "rebuild_source_graph": lambda p: tool_rebuild_source_graph(),
        "upload_document": lambda p: tool_upload_document(
            slug=p["slug"],
            filename=p["filename"],
            fetch_url=p.get("fetch_url", ""),
            content_b64=p.get("content_b64", ""),
            push_to_readwise=p.get("push_to_readwise", True),
        ),
    }

    if tool_name in read_tools:
        return read_tools[tool_name](params)
    elif tool_name in trusted_tools:
        if not is_trusted(req):
            raise PermissionError(f"Tool '{tool_name}' requires trusted client token")
        return trusted_tools[tool_name](params)
    elif tool_name in write_tools:
        if not is_write_authorized(req):
            raise PermissionError(f"Tool '{tool_name}' requires write authorization key")
        return write_tools[tool_name](params)
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
