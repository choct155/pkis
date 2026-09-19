"""
Published standalone exports (/pkis-api/export).

The Android app is a WebView with no download handler, so the viewer cannot hand
a generated file to the user there at all. Publishing the export and sharing its
URL is the route that works on every platform — which means the write side must
stay owner-only, and the read side must stay open, since recipients have no PKIS
account.
"""

import pytest

HTML = "<!doctype html><title>Paper</title><p>body</p>"


@pytest.fixture
def exports(appmod, monkeypatch, tmp_path):
    monkeypatch.setattr(appmod, "EXPORTS_DIR", tmp_path / "exports")
    return tmp_path / "exports"


@pytest.mark.integration
def test_publish_requires_write_access(client, exports):
    """An unauthenticated caller must not be able to plant a file that is then
    served from the app's own origin."""
    r = client.post("/pkis-api/export", json={"slug": "paper", "html": HTML})
    assert r.status_code == 403
    assert not exports.exists()


@pytest.mark.integration
def test_published_export_is_readable_without_auth(appmod, monkeypatch, client, exports):
    """The whole point is a link a recipient can open with no PKIS account."""
    monkeypatch.setattr(appmod, "is_write_authorized", lambda _req: True)
    url = client.post("/pkis-api/export",
                      json={"slug": "paper", "html": HTML}).get_json()["url"]

    r = client.get(url)
    assert r.status_code == 200
    assert "body" in r.get_data(as_text=True)


@pytest.mark.integration
def test_same_document_reuses_its_url(appmod, monkeypatch, client, exports):
    """Content-addressed, so re-exporting an unchanged document doesn't litter
    the directory with copies — and an edit gets a NEW url rather than silently
    changing a link already sent to someone."""
    monkeypatch.setattr(appmod, "is_write_authorized", lambda _req: True)
    pub = lambda h: client.post("/pkis-api/export",  # noqa: E731
                                json={"slug": "paper", "html": h}).get_json()["url"]

    assert pub(HTML) == pub(HTML)
    assert pub(HTML + "<p>edited</p>") != pub(HTML)


@pytest.mark.integration
@pytest.mark.parametrize("name", ["../../../etc/passwd", "..%2fsecret.html", "notes.txt"])
def test_export_reads_cannot_escape_the_export_directory(client, exports, name):
    r = client.get(f"/pkis-api/export/{name}")
    assert r.status_code in (400, 404)


@pytest.mark.integration
def test_slug_cannot_steer_the_written_path(appmod, monkeypatch, client, exports):
    """The slug is caller-supplied and ends up in a filename."""
    monkeypatch.setattr(appmod, "is_write_authorized", lambda _req: True)
    name = client.post("/pkis-api/export",
                       json={"slug": "../../evil", "html": HTML}).get_json()["name"]

    assert "/" not in name and ".." not in name
    assert (exports / name).is_file()
    assert sorted(p.name for p in exports.iterdir()) == [name]
