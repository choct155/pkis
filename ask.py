"""ask.py — the shared natural-language "ask brain" over the PKIS graph.

One agentic retrieve-and-synthesize loop, reused by both front-ends so behaviour
is identical everywhere:

  - the viewer Ask view        (POST /pkis-api/ask)
  - the MCP ``ask_pkis`` tool  (claude.ai / Claude Code)   [later phase]

Read tier — available to everyone — gives the model four tools to explore the
graph: ``search_wiki``, ``get_node``, ``get_related`` and
``get_dependency_chain`` (multi-hop traversal). Answers are grounded strictly in
retrieved nodes and cite them as ``[[slug]]`` wikilinks, which the viewer already
renders as live links.

The engine is **stateless**: the caller passes the full multi-turn message
history on every call (the viewer holds the conversation client-side). Owner
agentic writes are a deliberate later phase — this module is read-only.

``app`` is imported lazily inside functions: ``app.py`` imports this module when
wiring its route, so importing ``app`` at module load would be circular. By call
time both modules are fully initialised and ``import app`` is a cached lookup.
"""

import re

# Sonnet is the default per the build decision — fast and cheap enough for an
# interactive loop, strong enough for retrieve+synthesise. Matches the
# discovery/reader pipelines.
DEFAULT_MODEL = "claude-sonnet-4-6"

# Bounds on the agentic loop. Most questions resolve in 1–3 tool turns; the cap
# is a backstop against a model that keeps searching without answering.
MAX_TOOL_TURNS = 8

# A single node's body can be large; cap what we feed back per get_node call so a
# few fat nodes don't blow the context (and cost) of the loop.
_NODE_CONTENT_CAP = 8000

SYSTEM_PROMPT = """\
You are the assistant for PKIS — a personal knowledge graph of interconnected \
markdown "nodes" (concepts, techniques, sources, hypotheses, …) spanning \
probability, machine learning, causal inference, information theory and related \
fields. The user is a technical expert; be precise and concise, and do not \
over-explain fundamentals.

Your job: answer questions **strictly from the graph**. You have tools to search \
and traverse it. Always retrieve before answering — never answer from your own \
prior knowledge alone. Typical flow: `search_wiki` to find entry nodes, \
`get_node` to read them, then `get_related` / `get_dependency_chain` to follow \
edges for multi-hop questions ("how does X connect to Y?", "what does X \
depend on?").

Grounding rules:
- Cite every substantive claim with the `[[slug]]` of the node it came from, \
using the exact `slug` field from tool results. These render as live links.
- Never invent a slug or a node. If the graph does not contain what's needed, \
say so plainly and, if useful, suggest what the user might capture to fill the \
gap. Partial answers are fine — be explicit about the boundary.
- Prefer the graph's own framing and terminology over generic textbook phrasing.
- When traversal reveals a connection the user may not have asked about but that \
matters, surface it briefly.

Keep answers tight. Lead with the answer, then support it with cited nodes."""


def _slug_from_iri(iri):
    """`pkis:concept:bayesian-inference` -> `bayesian-inference` (the wikilink
    form and the markdown filename stem)."""
    return (iri or "").split(":")[-1]


# Anthropic tool schemas for the read tier. Names mirror the MCP/REST tools so
# the loop's behaviour matches what a connector would do by hand.
READ_TOOL_SCHEMAS = [
    {
        "name": "search_wiki",
        "description": (
            "Hybrid keyword+semantic search over the knowledge graph. Returns "
            "ranked nodes with iri, slug, title, type, domain and an excerpt. "
            "Use this first to find entry points for a question."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Natural-language or keyword query."},
                "max_results": {"type": "integer", "description": "Default 8.", "default": 8},
            },
            "required": ["query"],
        },
    },
    {
        "name": "get_node",
        "description": (
            "Fetch a node's full content and its immediate neighbours by iri. "
            "Use after search to actually read a node before citing it."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "iri": {"type": "string", "description": "e.g. pkis:concept:bayesian-inference"},
            },
            "required": ["iri"],
        },
    },
    {
        "name": "get_related",
        "description": (
            "Traverse edges from a node up to max_hops away. Returns connected "
            "nodes with edge_type, direction and hop_count. Use for multi-hop / "
            "'how are X and Y connected' questions."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "iri": {"type": "string"},
                "edge_types": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional filter, e.g. ['prerequisite-of','analogous-to'].",
                },
                "direction": {"type": "string", "enum": ["both", "outbound", "inbound"], "default": "both"},
                "max_hops": {"type": "integer", "default": 2},
            },
            "required": ["iri"],
        },
    },
    {
        "name": "get_dependency_chain",
        "description": (
            "Follow prerequisite-of edges (no hop limit) to get the full "
            "dependency chain a node rests on. Use for 'what do I need to "
            "understand X' questions."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"iri": {"type": "string"}},
            "required": ["iri"],
        },
    },
]


def _enrich_search_results(results):
    """Add the `slug` field (derived from iri) so the model can cite directly,
    and drop nothing else — the REST/MCP shape is already model-friendly."""
    for r in results:
        if "iri" in r and "slug" not in r:
            r["slug"] = _slug_from_iri(r["iri"])
    return results


def _execute_tool(name, args, surfaced):
    """Run one read tool, recording every iri it surfaces so we can build a
    reliable citation set even if the model's inline [[...]] are imperfect.
    Returns a JSON-serialisable result for the tool_result block."""
    import app

    if name == "search_wiki":
        res = app.tool_search_wiki(args["query"], max_results=args.get("max_results", 8))
        res = _enrich_search_results(res or [])
        for r in res:
            surfaced.add(r.get("iri"))
        return res

    if name == "get_node":
        iri = args["iri"]
        node = app.tool_get_node(iri)
        if isinstance(node, dict) and "error" not in node:
            surfaced.add(iri)
            node["slug"] = _slug_from_iri(iri)
            content = node.get("content") or ""
            if len(content) > _NODE_CONTENT_CAP:
                node["content"] = content[:_NODE_CONTENT_CAP] + "\n…[truncated]"
            for rel in node.get("related_nodes", []) or []:
                rel["slug"] = _slug_from_iri(rel.get("iri", ""))
        return node

    if name == "get_related":
        res = app.tool_get_related(
            args["iri"],
            edge_types=args.get("edge_types"),
            direction=args.get("direction", "both"),
            max_hops=args.get("max_hops", 2),
        )
        for r in res or []:
            r["slug"] = _slug_from_iri(r.get("iri", ""))
            surfaced.add(r.get("iri"))
        return res

    if name == "get_dependency_chain":
        res = app.tool_get_dependency_chain(args["iri"])
        for r in res or []:
            r["slug"] = _slug_from_iri(r.get("iri", ""))
            surfaced.add(r.get("iri"))
        return res

    return {"error": f"Unknown tool: {name}"}


_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")


def _build_citations(answer, surfaced):
    """Resolve the [[slug]] wikilinks the model actually cited into structured
    {slug, iri, title}. A slug resolves if it's a real node; we prefer the iri
    we already surfaced during the loop, else look it up. Unresolvable slugs are
    dropped from the structured list (they still render in the prose)."""
    import app

    surfaced_by_slug = {_slug_from_iri(i): i for i in surfaced if i}
    seen = set()
    citations = []
    for raw in _WIKILINK_RE.findall(answer or ""):
        slug = raw.strip().strip("/").lower().replace(" ", "-")
        if not slug or slug in seen:
            continue
        seen.add(slug)
        iri = surfaced_by_slug.get(slug)
        path = None
        if not iri:
            path = app.find_node_path(slug)
            if path:
                iri = (app.load_node(path) or {}).get("iri")
        if not iri:
            continue  # dangling — not a real node
        title = slug
        try:
            path = path or app.find_node_path(slug)
            if path:
                title = (app.load_node(path) or {}).get("title") or slug
        except Exception:
            pass
        citations.append({"slug": slug, "iri": iri, "title": title})
    return citations


def run_ask(messages, tier="reader", model=DEFAULT_MODEL, max_tool_turns=MAX_TOOL_TURNS):
    """Run one agentic ask turn.

    Args:
        messages: full conversation so far, Anthropic message dicts
            ([{role, content}, …]). The caller owns multi-turn state.
        tier: "reader" (default) or "owner". Reserved for the later
            agentic-write phase; today both tiers get the read tools only.
        model: override the default model.
        max_tool_turns: backstop on tool-use iterations.

    Returns dict: {answer, citations, surfaced, model, turns, usage}.
    """
    import app

    convo = list(messages)
    surfaced = set()
    in_tokens = out_tokens = 0
    turns = 0

    def _account(resp):
        """Record this call's tokens for the running total AND in the Comptroller
        usage ledger (best-effort — log_usage never raises)."""
        nonlocal in_tokens, out_tokens
        in_tokens += resp.usage.input_tokens
        out_tokens += resp.usage.output_tokens
        app.log_usage(app.USAGE_DB_PATH, resp, origin="pkis-ask", project="pkis",
                      attributes={"surface": "ask", "tier": tier})

    while True:
        resp = app.anthropic_client.messages.create(
            model=model,
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            tools=READ_TOOL_SCHEMAS,
            messages=convo,
        )
        _account(resp)

        if resp.stop_reason != "tool_use":
            answer = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
            return {
                "answer": answer,
                "citations": _build_citations(answer, surfaced),
                "surfaced": sorted(surfaced),
                "model": model,
                "turns": turns,
                "usage": {"input_tokens": in_tokens, "output_tokens": out_tokens},
            }

        turns += 1
        # Echo the assistant's tool_use turn, then answer each tool_use block.
        convo.append({"role": "assistant", "content": resp.content})
        tool_results = []
        for block in resp.content:
            if getattr(block, "type", None) != "tool_use":
                continue
            try:
                result = _execute_tool(block.name, block.input or {}, surfaced)
            except Exception as e:  # never let one bad tool call kill the turn
                result = {"error": f"{type(e).__name__}: {e}"}
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": app.json.dumps(result, default=str),
            })
        convo.append({"role": "user", "content": tool_results})

        if turns >= max_tool_turns:
            # Force a final synthesis from what we have rather than looping forever.
            convo.append({
                "role": "user",
                "content": "Tool budget reached — answer now from what you've gathered, "
                           "citing the relevant [[slug]] nodes, and note any gaps.",
            })
            resp = app.anthropic_client.messages.create(
                model=model, max_tokens=2048, system=SYSTEM_PROMPT, messages=convo,
            )
            _account(resp)
            answer = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
            return {
                "answer": answer,
                "citations": _build_citations(answer, surfaced),
                "surfaced": sorted(surfaced),
                "model": model,
                "turns": turns,
                "usage": {"input_tokens": in_tokens, "output_tokens": out_tokens},
            }
