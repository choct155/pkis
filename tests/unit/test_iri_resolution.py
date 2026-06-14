"""
Seam F — node load / IRI resolution (ARCHITECTURE_AUDIT.md §7 Seam F).

Pure-ish functions over the file tree: slug_from_path, iri_from_slug, parse_iri,
find_node_path, find_node_path_by_iri, load_node. A slug/IRI mismatch or alias
collision here silently returns the wrong node or None — high-value, cheap to
unit-test against the fixture wiki.
"""

import pytest


@pytest.mark.unit
def test_iri_from_slug_scheme(appmod):
    assert appmod.iri_from_slug("concept", "entropy") == "pkis:concept:entropy"


@pytest.mark.unit
def test_parse_iri_round_trips(appmod):
    ns, ntype, slug = appmod.parse_iri("pkis:concept:bayesian-inference")
    assert (ns, ntype, slug) == ("pkis", "concept", "bayesian-inference")


@pytest.mark.unit
def test_parse_iri_rejects_malformed(appmod):
    assert appmod.parse_iri("not-an-iri") == (None, None, None)


@pytest.mark.unit
def test_slug_from_path(appmod, isolated_wiki):
    p = isolated_wiki.wiki / "concepts" / "entropy.md"
    assert appmod.slug_from_path(p) == "entropy"


@pytest.mark.unit
def test_find_node_path_locates_seeded_node(appmod, isolated_wiki):
    p = appmod.find_node_path("bayesian-inference")
    assert p is not None and p.name == "bayesian-inference.md"


@pytest.mark.unit
def test_find_node_path_returns_none_for_missing(appmod, isolated_wiki):
    assert appmod.find_node_path("no-such-slug") is None


@pytest.mark.unit
def test_find_by_iri_handles_singular_type(appmod, isolated_wiki):
    """Canonical IRIs use the SINGULAR type (pkis:concept:...) but nodes live in
    the PLURAL folder (concepts/). find_node_path_by_iri must bridge that via
    TYPE_TO_FOLDER — a real subtlety flagged in the audit."""
    p = appmod.find_node_path_by_iri("pkis:concept:entropy")
    assert p is not None and p.parent.name == "concepts"


@pytest.mark.unit
def test_load_node_shape(appmod, isolated_wiki):
    p = appmod.find_node_path("bayesian-inference")
    node = appmod.load_node(p)
    for key in ("iri", "slug", "node_type", "frontmatter", "content", "title"):
        assert key in node
    assert node["slug"] == "bayesian-inference"
    assert node["iri"] == "pkis:concept:bayesian-inference"  # from frontmatter id


@pytest.mark.unit
def test_alias_collision_detection(appmod, isolated_wiki):
    """STUB: build_alias_registry + tool_check_alias_collision must flag a surface
    form that maps to multiple canonical nodes. Seed two nodes sharing an alias
    and assert the collision is reported."""
    pytest.skip("Phase-2 stub — seed colliding aliases and assert detection")
