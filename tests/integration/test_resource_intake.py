"""
Resource node intake — the `resource` knowledge type (external tools/libraries/
platforms/docs/datasets/services with a lifecycle). create_resource_stub stages a
resource node with its lifecycle frontmatter + ## Summary / ## Relationship
Candidates body; URL is taken as-is (no enrichment). Promotion reuses
commit_staged_node → wiki/resources/.
"""
import pytest


def _seed_catalog(env):
    (env.wiki / "index.md").write_text("# Index\n")
    (env.wiki / "log.md").write_text("# Log\n")
    (env.wiki / "resources").mkdir(parents=True, exist_ok=True)


@pytest.mark.integration
def test_create_resource_stub_stages_with_lifecycle_fields(appmod, isolated_wiki):
    import frontmatter
    res = appmod.tool_create_resource_stub(
        title="OpenWiki", slug="openwiki",
        resource_url="https://github.com/example/openwiki",
        resource_type="documentation", status="active",
        last_evaluated="2026-07-04",
        technological_scope=["python", "markdown"],
        domain=["knowledge-representation"], tags=["coding-agents"],
        summary="Structured docs for codebases, for coding agents.",
    )
    assert res["iri"] == "pkis:resource:openwiki"
    assert res["knowledge_type"] == "resource"
    staged = appmod.STAGING_DIR / f"{res['slug']}.md"
    fm = frontmatter.load(str(staged)).metadata
    assert fm["knowledge_type"] == "resource"
    assert fm["resource_url"] == "https://github.com/example/openwiki"
    assert fm["resource_type"] == "documentation"
    assert fm["status"] == "active"
    assert fm["last_evaluated"] == "2026-07-04"
    assert fm["technological_scope"] == ["python", "markdown"]
    assert fm["staged_by"] == "mcp-create-resource-stub"
    body = frontmatter.load(str(staged)).content
    assert "## Summary" in body and "## Relationship Candidates" in body
    assert "## Key Concepts" not in body


@pytest.mark.integration
def test_create_resource_stub_requires_url_and_valid_vocab(appmod, isolated_wiki):
    with pytest.raises(ValueError):
        appmod.tool_create_resource_stub(title="No URL")
    with pytest.raises(ValueError):
        appmod.tool_create_resource_stub(title="Bad type", resource_url="https://x",
                                         resource_type="framework")   # not in vocab
    with pytest.raises(ValueError):
        appmod.tool_create_resource_stub(title="Bad status", resource_url="https://x",
                                         status="sunset")             # not in vocab


@pytest.mark.integration
def test_create_resource_stub_defaults(appmod, isolated_wiki):
    import frontmatter
    res = appmod.tool_create_resource_stub(title="Minimal Tool", resource_url="https://x/y")
    fm = frontmatter.load(str(appmod.STAGING_DIR / f"{res['slug']}.md")).metadata
    assert fm["status"] == "active"            # default
    assert fm["last_evaluated"]                # defaulted to ingest date
    assert fm["maturity"] == "evolving"        # valid vocab (not the spec example's 'stub')


@pytest.mark.integration
def test_resource_commit_promotes_and_implemented_by_edge(appmod, isolated_wiki):
    _seed_catalog(isolated_wiki)
    # a live concept the resource implements
    isolated_wiki.write_node("concepts", "knowledge-representation",
                             id="pkis:concept:knowledge-representation",
                             knowledge_type="concept", title="Knowledge Representation",
                             domain=["kr"])
    res = appmod.tool_create_resource_stub(
        title="OpenWiki", slug="openwiki", resource_url="https://github.com/example/openwiki",
        resource_type="documentation")
    commit = appmod.tool_commit_staged_node(staged_id=res["staged_id"])
    assert commit["status"] == "committed"
    assert appmod.find_node_path("openwiki") is not None    # lives in wiki/resources/

    # concept --implemented-by--> resource, graph-visible
    appmod.tool_add_connections(edges=[{
        "subject": "knowledge-representation", "target": "openwiki",
        "predicate": "implemented-by", "note": "agent-readable codebase docs",
    }])
    appmod.STORE.invalidate_nodes(); appmod.STORE.invalidate_graph()
    G = appmod.get_graph()
    ci, ri = "pkis:concept:knowledge-representation", "pkis:resource:openwiki"
    assert G.has_edge(ci, ri)
    assert (G.get_edge_data(ci, ri) or {}).get("edge_type") == "implemented-by"


@pytest.mark.integration
def test_resource_stub_rest_route_is_write_gated(appmod, isolated_wiki, monkeypatch):
    client = appmod.app.test_client()
    body = {"title": "Rest Tool", "resource_url": "https://github.com/x/y", "resource_type": "tool"}
    # anonymous → write-gated 401 (auth is dormant in tests)
    assert client.post("/pkis-api/resource-stub", json=body).status_code == 401
    # with the static write key → stages
    monkeypatch.setattr(appmod, "WRITE_KEY", "k")
    r = client.post("/pkis-api/resource-stub", headers={"Authorization": "Bearer k"}, json=body)
    assert r.status_code == 200
    assert (appmod.STAGING_DIR / "rest-tool.md").exists()   # slug derived + staged
