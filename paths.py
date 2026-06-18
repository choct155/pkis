"""
Canonical filesystem paths for PKIS tools/ and scripts/ (B4).

Single source of truth for where things live, so standalone operational scripts
stop re-deriving `/home/pkis/...` literals independently (they had drifted: some
read env, most hardcoded). Every value is env-overridable with the same default the
scripts used, so importing this changes nothing on the VPS but makes the paths
discoverable and testable.

Two groups:
  * Code/graph paths (WIKI_DIR, REPO_DIR, …) — re-exported from config.py, the
    authority the running server already uses.
  * Operational paths (PROPOSALS_DIR, DOCS_DIR, …) — VPS work dirs that live
    OUTSIDE the git repo and so are not in config; defined here.

`bootstrap()` puts the repo root on sys.path so a tools/ script can `import usage` /
`import config` regardless of CWD — call it right after the inline path insert that
locates this module.
"""

import os
import sys
from pathlib import Path

# The code repo root (this file sits at it, next to app.py / config.py / usage.py).
REPO_ROOT = Path(__file__).resolve().parent


def bootstrap() -> Path:
    """Ensure REPO_ROOT is importable; return it. Idempotent."""
    p = str(REPO_ROOT)
    if p not in sys.path:
        sys.path.insert(0, p)
    return REPO_ROOT


bootstrap()

# Code/graph paths — authoritative in config.py (re-exported here so scripts have
# one import). config is importable now that REPO_ROOT is on the path.
from config import (  # noqa: E402
    WIKI_DIR, RAW_DIR, REPO_DIR, STAGING_DIR, DOCS_DIR, USAGE_DB_PATH,
)

# Operational paths — VPS work dirs outside the git repo. Env-overridable; defaults
# match the literals the scripts used before B4.
PROPOSALS_DIR        = Path(os.environ.get("PKIS_PROPOSALS_DIR", "/home/pkis/proposals"))
DOCS_BOOKS_DIR       = Path(os.environ.get("PKIS_DOCS_BOOKS_DIR", "/home/pkis/docs/books"))
DOCS_SOURCES_DIR     = Path(os.environ.get("PKIS_DOCS_SOURCES_DIR", "/home/pkis/docs/sources"))
READER_DIR           = Path(os.environ.get("PKIS_READER_DIR", str(WIKI_DIR / "reader")))
USAGE_DIR            = Path(os.environ.get("PKIS_USAGE_DIR", "/home/pkis/usage"))
DISCOVERY_INBOX_PATH = Path(os.environ.get("PKIS_DISCOVERY_INBOX", "/home/pkis/discovery_inbox.json"))
DISCOVERY_PRIOR_PATH = Path(os.environ.get("PKIS_DISCOVERY_PRIOR", "/home/pkis/discovery_prior.json"))
ENV_FILE             = Path(os.environ.get("PKIS_ENV", "/home/pkis/.env"))
INBOX_MD             = Path(os.environ.get("PKIS_INBOX_MD", str(WIKI_DIR / "inbox.md")))
