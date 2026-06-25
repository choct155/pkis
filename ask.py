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

# Eager retrieval: before the first model call we run the same hybrid search the
# model would call and inject the top-K nodes into the prompt. On a small graph
# this is cheap and collapses most questions from ~3 serial model calls to one —
# the number of serial calls is what dominates wall-clock latency.
PRELOAD_K = 8

SYSTEM_PROMPT = """\
You are the assistant for PKIS — a personal knowledge graph of interconnected \
markdown "nodes" (concepts, techniques, sources, hypotheses, …) spanning \
probability, machine learning, causal inference, information theory and related \
fields. The user is a technical expert; be precise and concise, and do not \
over-explain fundamentals.

Your job: answer questions **strictly from the graph**. The most relevant nodes \
for the question are usually PRELOADED for you under "Relevant nodes already \
retrieved" — read those first and answer directly from them when they suffice \
(no tool call needed). Reach for tools only when the preloaded set is \
insufficient: `get_node` to read a node's full body, `get_related` / \
`get_dependency_chain` to follow edges for multi-hop questions ("how does X \
connect to Y?", "what does X depend on?"), or `search_wiki` to find nodes the \
preload missed. Never answer from your own prior knowledge alone.

When you do decide to use a tool, call it immediately — do not write any \
explanatory text before the tool call.

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


def _execute_tool(name, args, surfaced, profile=None):
    """Run one read tool, recording every iri it surfaces so we can build a
    reliable citation set even if the model's inline [[...]] are imperfect.
    Returns a JSON-serialisable result for the tool_result block. `profile`
    selects the retrieval regime for search_wiki (the lab's ask comparison)."""
    import app

    if name == "search_wiki":
        res = app.tool_search_wiki(args["query"], max_results=args.get("max_results", 8), profile=profile)
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


def _system_blocks():
    """System as a cacheable block: the static prompt + tool schemas form a stable
    prefix across every request, so a `cache_control` breakpoint here turns the
    ~1.5k-token system+tools prefill into a cache read on calls 2..N."""
    return [{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}]


def _mark_cache(convo):
    """Keep exactly one moving message-level cache breakpoint on the latest
    message, so each tool turn re-reads the prior (cached) prefix and only writes
    the new delta. Clearing older breakpoints keeps us within the 4-breakpoint
    limit. Only list-content messages (tool_result / preloaded) are markable."""
    for m in convo:
        c = m.get("content")
        if isinstance(c, list):
            for blk in c:
                if isinstance(blk, dict):
                    blk.pop("cache_control", None)
    last = convo[-1].get("content")
    if isinstance(last, list) and last and isinstance(last[-1], dict):
        last[-1]["cache_control"] = {"type": "ephemeral"}


def _preload_block(question, surfaced, profile=None):
    """Run the hybrid search the model would otherwise call, and format the top-K
    hits as a context block. Records their IRIs so citations resolve even if the
    model never calls get_node on them. Returns None when nothing is found.
    `profile` selects the retrieval regime (the lab's ask comparison)."""
    import app
    results = _enrich_search_results(app.tool_search_wiki(question, max_results=PRELOAD_K, profile=profile) or [])
    if not results:
        return None
    lines = ["Relevant nodes already retrieved from the graph for this question "
             "(cite by [[slug]]; call get_node for a node's full body if you need more):", ""]
    for r in results:
        surfaced.add(r.get("iri"))
        dom = ", ".join(r.get("domain") or []) or "—"
        lines.append(f"- [[{r['slug']}]] · {r.get('node_type','?')} · {dom}\n  {(r.get('excerpt') or '').strip()}")
    return "\n".join(lines)


_STATUS = {
    "search_wiki": "searching the graph…",
    "get_node": "reading nodes…",
    "get_related": "following connections…",
    "get_dependency_chain": "tracing prerequisites…",
}


def _ask_events(messages, tier="reader", model=DEFAULT_MODEL, max_tool_turns=MAX_TOOL_TURNS, profile=None):
    """The single engine implementation, as a generator of events. Both the
    streaming endpoint (forwards events as SSE) and run_ask (drains them) use it.

    Events:
      {"type":"status","text":…}  a tool-use turn started; the client should
                                  discard any partial answer streamed this turn
                                  (pre-tool narration) and show the status.
      {"type":"delta","text":…}   a chunk of answer text.
      {"type":"done", …}          final payload: answer, citations, surfaced,
                                  model, turns, usage.

    Every model call is streamed so the final answer reaches the client token by
    token. Preload (eager retrieval) collapses most questions to a single call.
    """
    import app

    convo = [dict(m) for m in messages]
    surfaced = set()
    in_tokens = out_tokens = 0
    turns = 0
    system = _system_blocks()

    # Eager retrieval on the latest question → inject as a context block ahead of it.
    if convo and convo[-1].get("role") == "user" and isinstance(convo[-1].get("content"), str):
        q = convo[-1]["content"]
        block = _preload_block(q, surfaced, profile)
        if block:
            convo[-1] = {"role": "user", "content": [
                {"type": "text", "text": block},
                {"type": "text", "text": q},
            ]}

    def _account(final):
        nonlocal in_tokens, out_tokens
        in_tokens += final.usage.input_tokens
        out_tokens += final.usage.output_tokens
        app.log_usage(app.USAGE_DB_PATH, final, origin="pkis-ask", project="pkis",
                      attributes={"surface": "ask", "tier": tier})

    def _done(answer):
        return {"type": "done", "answer": answer,
                "citations": _build_citations(answer, surfaced),
                "surfaced": sorted(surfaced), "model": model, "turns": turns,
                "usage": {"input_tokens": in_tokens, "output_tokens": out_tokens}}

    while True:
        _mark_cache(convo)
        use_tools = turns < max_tool_turns
        parts = []
        kwargs = dict(model=model, max_tokens=2048, system=system, messages=convo)
        if use_tools:
            kwargs["tools"] = READ_TOOL_SCHEMAS
        with app.anthropic_client.messages.stream(**kwargs) as stream:
            for event in stream:
                if (event.type == "content_block_delta"
                        and getattr(event.delta, "type", None) == "text_delta"):
                    parts.append(event.delta.text)
                    yield {"type": "delta", "text": event.delta.text}
            final = stream.get_final_message()
        _account(final)

        if final.stop_reason != "tool_use":
            answer = "".join(parts) or "".join(
                b.text for b in final.content if getattr(b, "type", None) == "text")
            yield _done(answer)
            return

        # Tool-use turn: the streamed `parts` (if any) were pre-tool narration —
        # the status event tells the client to drop them.
        turns += 1
        names = [b.name for b in final.content if getattr(b, "type", None) == "tool_use"]
        yield {"type": "status", "text": _STATUS.get(names[0] if names else "", "consulting the graph…")}
        convo.append({"role": "assistant", "content": final.content})
        tool_results = []
        for block in final.content:
            if getattr(block, "type", None) != "tool_use":
                continue
            try:
                result = _execute_tool(block.name, block.input or {}, surfaced, profile)
            except Exception as e:  # never let one bad tool call kill the turn
                result = {"error": f"{type(e).__name__}: {e}"}
            tool_results.append({"type": "tool_result", "tool_use_id": block.id,
                                 "content": app.json.dumps(result, default=str)})
        convo.append({"role": "user", "content": tool_results})
        if turns >= max_tool_turns:
            # Next iteration runs WITHOUT tools (use_tools False) → forces a final
            # streamed synthesis from what's gathered.
            convo.append({"role": "user", "content":
                          "Tool budget reached — answer now from what you've gathered, "
                          "citing the relevant [[slug]] nodes, and note any gaps."})


def run_ask(messages, tier="reader", model=DEFAULT_MODEL, max_tool_turns=MAX_TOOL_TURNS, profile=None):
    """Non-streaming convenience wrapper (used by the JSON endpoint and the future
    MCP tool): drain the event stream and return the final payload dict
    {answer, citations, surfaced, model, turns, usage}. `profile` selects the
    retrieval regime used for the answer (the lab's ask comparison)."""
    done = None
    for ev in _ask_events(messages, tier=tier, model=model, max_tool_turns=max_tool_turns, profile=profile):
        if ev["type"] == "done":
            done = ev
    return {k: v for k, v in (done or {}).items() if k != "type"}
