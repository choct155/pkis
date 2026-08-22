"""Narration resilience: one failing section (content-filter block, transient API
error) must not abort an hour-long reader build — it falls back to the raw section
text. But if EVERY section fails (a real outage / credit problem) the build aborts,
so that signal isn't masked by a shipped-but-empty narration."""
import pytest

reader_build = pytest.importorskip("tools.reader_build")


def _segs():
    return [
        {"id": "S1", "title": "Intro", "paper_md": "raw text one"},
        {"id": "S2", "title": "Blocked", "paper_md": "raw text two"},
        {"id": "S3", "title": "Outro", "paper_md": "raw text three"},
    ]


def test_one_blocked_section_falls_back_to_raw_text(monkeypatch):
    def fake_narrate(seg, ctx):
        if seg["id"] == "S2":
            raise RuntimeError("Error code: 400 - Output blocked by content filtering policy")
        return f"narrated {seg['id']}"
    monkeypatch.setattr(reader_build, "narrate", fake_narrate)

    segs = _segs()
    fails = reader_build.narrate_segments(segs, ctx=[])

    assert fails == 1
    assert segs[0]["narration"] == "narrated S1"
    assert segs[1]["narration"] == "raw text two"      # fallback keeps the content
    assert segs[2]["narration"] == "narrated S3"        # build continued past the failure


def test_total_narration_failure_aborts(monkeypatch):
    monkeypatch.setattr(reader_build, "narrate",
                        lambda s, c: (_ for _ in ()).throw(RuntimeError("credit balance is too low")))
    with pytest.raises(RuntimeError, match="all 3 sections"):
        reader_build.narrate_segments(_segs(), ctx=[])
