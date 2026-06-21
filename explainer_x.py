"""Tier-2 dynamic explainers — a Flask blueprint pattern for explainers that need
SERVER-SIDE action (persistence, heavier compute, secret keys, auth-gated writes)
while reusing the PKIS app's auth, deploy pipeline, and usage logging.

The graduated model (see EXPLAINER_WORKFLOW.md):
  Tier 0/1  static self-contained HTML in wiki/assets/viz/<slug>.html  (the default)
  Tier 2    this file: a dynamic explainer served + backed by Flask routes
  Tier 3    a separate proxied service (only when it outgrows the monolith)

Mounting: registered under the EXISTING reverse-proxied prefix `/pkis-api/x`, so no
nginx change is needed (nginx already proxies /pkis-api/* to gunicorn). A dynamic
explainer lives at  /pkis-api/x/<name>/  with its API under /pkis-api/x/<name>/api/...

Promoting an explainer from static to dynamic is a metadata change, not a rewrite:
give its asset node (wiki/assets/<slug>.md) a frontmatter field
    viz_url: /pkis-api/x/<name>/
instead of `viz: <static-slug>` — tool_get_assets honors an explicit viz_url, and
the viewer hosts it identically (iframe). Add the routes for <name> here.

Add the hooks you need by extending register() — it receives the app plus optional
auth/usage callables so dynamic explainers reuse them rather than re-implementing.
"""
from flask import Blueprint, render_template_string, request, jsonify

explainer_x = Blueprint("explainer_x", __name__, url_prefix="/pkis-api/x")

# Auth / usage hooks injected at registration so explainer routes can reuse the
# app's WorkOS auth + Comptroller logging. Left as no-ops until wired.
_HOOKS = {"is_write_authorized": None, "log_usage": None}


def register(app, *, is_write_authorized=None, log_usage=None):
    """Mount the dynamic-explainer blueprint on the main PKIS app. Call once from
    app.py after the app is created. Pass the app's auth/usage helpers to share them."""
    _HOOKS["is_write_authorized"] = is_write_authorized
    _HOOKS["log_usage"] = log_usage
    if "explainer_x" not in app.blueprints:
        app.register_blueprint(explainer_x)
    return explainer_x


# ── Example dynamic explainer: /pkis-api/x/sample/ ────────────────────────────
# Proves the pattern end-to-end: an HTML shell that calls a server action. Copy
# this pair (shell route + api route) as the template for a real dynamic explainer.
_SAMPLE_SHELL = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sample dynamic explainer</title>
<style>
 body{font-family:system-ui,sans-serif;background:#111;color:#eee;padding:24px;line-height:1.5}
 button{font:inherit;background:#E5484D;color:#fff;border:0;border-radius:6px;padding:8px 14px;cursor:pointer}
 pre{background:#1b1b1b;padding:12px;border-radius:6px;overflow:auto}
 .muted{color:#999;font-size:14px}
</style></head><body>
<h1>Sample dynamic explainer</h1>
<p class="muted">Served by a Flask blueprint (Tier 2), so it can take server-side
action — persist data, run compute, call a model with a server-held key.</p>
<button onclick="ping()">call the server</button>
<pre id="out">(click the button)</pre>
<script>
async function ping(){
  const r = await fetch('api/echo', {method:'POST',
    headers:{'content-type':'application/json'}, body:JSON.stringify({hello:'pkis'})});
  document.getElementById('out').textContent = JSON.stringify(await r.json(), null, 2);
}
</script></body></html>"""


@explainer_x.route("/sample/")
def sample_shell():
    return render_template_string(_SAMPLE_SHELL)


@explainer_x.route("/sample/api/echo", methods=["POST"])
def sample_echo():
    body = request.get_json(silent=True) or {}
    # A real explainer would compute/persist here; this just echoes to prove the
    # round-trip. Reuse the injected hooks for auth-gated writes or usage logging.
    return jsonify({"ok": True, "you_sent": body, "served_by": "explainer_x blueprint"})
