#!/usr/bin/env python3
"""Architect reconciliation — keep docs/STATUS.md current automatically.

The Architect agent owns docs/STATUS.md (the canonical current-state snapshot) but
nothing was running it, so STATUS drifted ~2 weeks. This is the headless version:
it gathers ground truth (live node count, narrated count, git log since STATUS was
last touched) and asks the model to refresh STATUS.md, then commits + pushes if it
changed. Runs daily via cron and after each deploy via a git post-merge hook.

Scope is deliberately just STATUS.md — cheap (~one Sonnet call) and safe. The deeper
ARCHITECTURE.md drift audit stays a manual `Architect, run`.

  python tools/architect_reconcile.py        # reconcile + commit + push if changed
  python tools/architect_reconcile.py --dry   # print proposed STATUS, no write
"""
import os, re, sys, glob, subprocess, datetime

REPO = "/home/pkis/pkis-wiki"
WIKI = f"{REPO}/wiki"
STATUS = f"{REPO}/docs/STATUS.md"
MODEL = os.environ.get("PKIS_ARCHITECT_MODEL", "claude-sonnet-4-6")


def sh(*args, cwd=REPO):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True).stdout.strip()


def ground_truth(force=False):
    nodes = len([f for f in glob.glob(f"{WIKI}/**/*.md", recursive=True)
                 if "/reader/" not in f and os.path.basename(f) not in
                 ("index.md", "log.md", "queue.md", "inbox.md")])
    narrated = len(glob.glob(f"{WIKI}/reader/*/audio.mp3"))
    cur = open(STATUS).read()
    m = re.search(r"_Last updated:\s*([0-9-]+)_", cur)
    since = m.group(1) if m else "?"
    # Commits SINCE STATUS.md was last changed — a precise range (not --since=<date>,
    # which drops same-day commits and would make the post-deploy hook a no-op).
    if force:
        rng = "HEAD~40..HEAD"
    else:
        last = sh("git", "log", "-1", "--format=%H", "--", "docs/STATUS.md")
        rng = f"{last}..HEAD" if last else "HEAD~40..HEAD"
    log = sh("git", "log", rng, "--pretty=- %s", "--no-merges")
    log = "\n".join(log.splitlines()[:80])
    return cur, nodes, narrated, since, log


SYSTEM = (
    "You are the PKIS Architect. You maintain docs/STATUS.md — the single canonical "
    "snapshot of current build state. Given the CURRENT STATUS.md, live ground-truth "
    "counts, and the git commit subjects since it was last updated, produce a REFRESHED "
    "STATUS.md. Rules: keep the existing structure and section headings; update only "
    "what has drifted (counts, the _Last updated_ date, component status, recent-session "
    "summary, next priorities); fold the commit log into the component table + 'Most "
    "recent session' rather than listing raw commits; be terse and factual; never invent "
    "components not evidenced by the commits or current doc. Output ONLY the full markdown "
    "of the new STATUS.md, nothing else."
)


def reconcile(cur, nodes, narrated, since, log, today):
    import anthropic
    c = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    user = (f"TODAY: {today}\nLIVE COUNTS: {nodes} nodes, {narrated} narrated chapters\n"
            f"STATUS LAST UPDATED: {since}\n\nCOMMITS SINCE THEN:\n{log}\n\n"
            f"=== CURRENT docs/STATUS.md ===\n{cur}")
    r = c.messages.create(model=MODEL, max_tokens=4000, system=SYSTEM,
                          messages=[{"role": "user", "content": user}])
    out = r.content[0].text.strip()
    if out.startswith("```"):
        out = re.sub(r"^```[a-z]*\n|\n```$", "", out)
    return out.strip() + "\n"


def main():
    dry = "--dry" in sys.argv
    force = "--force" in sys.argv
    today = datetime.date.today().isoformat()
    cur, nodes, narrated, since, log = ground_truth(force=force)
    if not log.strip():
        print("no commits since last STATUS update — nothing to reconcile"); return
    new = reconcile(cur, nodes, narrated, since, log, today)
    if not new.startswith("# PKIS Status"):
        print("model output does not look like STATUS.md — aborting, no write"); sys.exit(1)
    if dry:
        print(new); return
    if new.strip() == cur.strip():
        print("STATUS.md already current — no change"); return
    open(STATUS, "w").write(new)
    sh("git", "add", "docs/STATUS.md")
    subprocess.run(["git", "-c", "user.name=pkis-architect", "-c", "user.email=pkis@pkis.dev",
                    "commit", "-q", "-m", f"docs(status): architect auto-reconcile {today}"], cwd=REPO)
    push = subprocess.run(["git", "push", "-q", "origin", "main"], cwd=REPO, capture_output=True, text=True)
    print(f"STATUS.md reconciled + committed ({today}); push rc={push.returncode}")


if __name__ == "__main__":
    main()
