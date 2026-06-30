"""
Finding intake — the narrow, human-gated inbound gate (PKIS Lab Assistant Extension
Part B). create_finding_stub accepts a scrubbed, aggregate finding object from an
external system (OpGraph) and stages it as a `finding` node with an `evidence-for`
edge to a live hypothesis. PKIS validates ONLY schema + that hypothesis_ref resolves
to a live hypothesis; it never recomputes stats and never scrubs content.
"""

import pytest


def _seed_catalog(env):
    # commit_staged_node git-adds index.md + log.md alongside the promoted node.
    (env.wiki / "index.md").write_text("# Index\n")
    (env.wiki / "log.md").write_text("# Log\n")
    (env.wiki / "findings").mkdir(parents=True, exist_ok=True)


def _live_hypothesis(env, slug="test-hyp", domain=("ned",)):
    env.write_node("hypotheses", slug,
                   id=f"pkis:hypothesis:{slug}", knowledge_type="hypothesis",
                   title="Test Hypothesis", domain=list(domain), status="open")
    return f"pkis:hypothesis:{slug}"


def _finding(hyp_ref="pkis:hypothesis:test-hyp"):
    return {
        "finding_id": "11111111-1111-1111-1111-111111111111",
        "generated_at": "2026-06-29T12:00:00Z",
        "hypothesis_ref": hyp_ref,
        "summary": "structural_priors beat alias_lookup on indirect mentions.",
        "statistics": {
            "strategy": "structural_priors", "comparison_strategy": "alias_lookup",
            "metric": "precision", "value": 0.84, "comparison_value": 0.61,
            "n": 340, "confidence_interval": [0.79, 0.88],
        },
        "stratification": {"mention_type": "indirect_referring_expression"},
        "source_pointer": {"system": "opgraph", "run_id": "run-xyz",
                           "log_date_range": ["2026-06-01", "2026-06-30"]},
    }


@pytest.mark.integration
def test_create_finding_stub_stages_with_inherited_domain_and_edge(appmod, isolated_wiki):
    import frontmatter
    _live_hypothesis(isolated_wiki, domain=("ned", "entity-resolution"))
    res = appmod.tool_create_finding_stub(**_finding())

    assert res["iri"].startswith("pkis:finding:")
    assert res["hypothesis_ref"] == "pkis:hypothesis:test-hyp"
    staged = appmod.STAGING_DIR / f"{res['slug']}.md"
    assert staged.exists()
    fm = frontmatter.load(str(staged)).metadata
    assert fm["knowledge_type"] == "finding"
    assert fm["domain"] == ["ned", "entity-resolution"]      # inherited from the hypothesis
    assert fm["source_system"] == "opgraph"
    assert fm["statistics"]["value"] == 0.84
    assert fm["evidence-for"] == ["test-hyp"]                 # typed edge to the hypothesis
    assert "opgraph" in fm["tags"] and "structural_priors" in fm["tags"]
    assert fm["staged_by"] == "mcp-create-finding-stub"


@pytest.mark.integration
def test_create_finding_stub_rejects_malformed(appmod, isolated_wiki):
    _live_hypothesis(isolated_wiki)
    bad_missing_summary = _finding(); bad_missing_summary["summary"] = ""
    with pytest.raises(ValueError):
        appmod.tool_create_finding_stub(**bad_missing_summary)
    bad_empty_stats = _finding(); bad_empty_stats["statistics"] = {}
    with pytest.raises(ValueError):
        appmod.tool_create_finding_stub(**bad_empty_stats)
    bad_source = _finding(); bad_source["source_pointer"] = {"run_id": "x"}  # no system
    with pytest.raises(ValueError):
        appmod.tool_create_finding_stub(**bad_source)


@pytest.mark.integration
def test_create_finding_stub_rejects_bad_hypothesis_ref(appmod, isolated_wiki):
    _live_hypothesis(isolated_wiki)
    # does not resolve to a live node
    with pytest.raises(ValueError):
        appmod.tool_create_finding_stub(**_finding(hyp_ref="pkis:hypothesis:nope"))
    # resolves, but is not a hypothesis (entropy concept is seeded by the fixture)
    with pytest.raises(ValueError):
        appmod.tool_create_finding_stub(**_finding(hyp_ref="pkis:concept:entropy"))


@pytest.mark.integration
def test_finding_commit_promotes_and_builds_evidence_for_edge(appmod, isolated_wiki):
    _seed_catalog(isolated_wiki)
    hyp_iri = _live_hypothesis(isolated_wiki)
    res = appmod.tool_create_finding_stub(**_finding())

    commit = appmod.tool_commit_staged_node(staged_id=res["staged_id"])
    assert commit["status"] == "committed"
    assert appmod.find_node_path(res["slug"]) is not None     # promoted live (wiki/findings/)

    appmod.STORE.invalidate_nodes()
    appmod.STORE.invalidate_graph()
    G = appmod.get_graph()
    assert G.has_edge(res["iri"], hyp_iri)
    assert (G.get_edge_data(res["iri"], hyp_iri) or {}).get("edge_type") == "evidence-for"
