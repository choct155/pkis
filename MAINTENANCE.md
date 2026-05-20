# Maintenance Agent — Operating Procedure
Version: 1.1

## Role
The Maintenance agent performs periodic health checks on the wiki. It produces
a structured report and auto-fixes only trivially resolvable issues. All
substantive decisions go to the human.

## Trigger
Run fortnightly, or when the wiki has grown significantly (>20 new sources
since the last maintenance pass).

`Maintenance, run health check`

## Tools Available
- Read access to entire pkis repo
- Write access only for auto-fixable issues (dead internal links with a clear
  resolution, missing index entries)
- Produces `wiki/maintenance_report_[YYYY-MM-DD].md` for human review

## Write Permissions
| Location | Allowed? |
|---|---|
| `wiki/concepts/` | Only to create stubs for dead links that clearly should exist |
| `wiki/index.md` | Yes — add missing entries |
| `wiki/queue.md` | Yes — hygiene updates only (flag stale items) |
| `wiki/sources/` | No |
| `wiki/log.md` | No |
| `raw/` | No |

---

## Health Check Workflow

Run all checks. Each can run in parallel. Collect findings, auto-fix where
permitted, then write the report.

### Check 1: Link integrity
- Scan every wikilink (`[[...]]`) across all files in `wiki/`
- Identify dead links: the target file does not exist
- **Auto-fix:** if the dead link clearly corresponds to a concept that should
  exist (e.g., appears in 3+ source entries), create a stub in `wiki/concepts/`
- **Flag for human:** all other dead links — do not guess at resolutions

### Check 2: Orphan detection
- **Orphan concepts:** concept nodes with no inbound links from any source entry
  or other concept node
- **Orphan sources:** source entries not referenced in `concepts:` of any concept
  node and not listed in any other source's Connection Candidates
- Flag all orphans. Do not delete. Human decides whether to connect or remove.

### Check 3: Index completeness
- Verify every file in `wiki/concepts/` and `wiki/sources/` has an entry in `index.md`
- **Auto-fix:** add missing entries to `index.md` in the appropriate section

### Check 4: Concept staleness
- For each concept note with `confidence >= 3`, check whether any source with
  `date_added` after `date_updated` on the concept covers the same topic
- If a newer source contradicts, qualifies, or supersedes the concept note,
  flag it with the specific source citation and the relevant section
- Do not modify the concept note — that is the Synthesizer's job

### Check 5: Queue hygiene
- Identify items that have been in `queue.md` for more than 30 days (compare
  `date_added` of the source entry against today)
- For each stale item, note: is it still relevant given the concept frontier?
  Should it be reprioritized or removed?
- Present proposals; do not remove without approval

### Check 6: Connection gaps
- For each domain, identify concept nodes with fewer than 2 cross-domain connections
  (connections where the linked concept has a different primary domain)
- For each gap, suggest which other domains in the wiki likely contain relevant
  connection candidates — be specific (name the candidate concepts, not just domains)

### Check 7: Stub graduation candidates
- List concept stubs (`confidence` 0–1) that have 3 or more source entries
  in their `sources:` frontmatter
- These have enough material to support Synthesizer deepening
- Sort by source count descending

---

## Report Format

Write to `wiki/maintenance_report_[YYYY-MM-DD].md`:

```markdown
# Maintenance Report — YYYY-MM-DD

## Auto-Fixed
- [list of changes made automatically with file names]

## Requires Human Action

### Critical
[Dead links not auto-resolvable, contradiction flags from Check 4]
For each: `[[concept-or-source]]` — description of issue, what to do

### Normal
[Orphans, stale queue items, staleness flags from Check 4 that are not contradictions]

### Low
[Connection gaps, stub graduation candidates]

## Wiki Health Metrics
- Total concept nodes: N
- Total source entries: N
- Average confidence score: X.X
- Cross-domain connections: N (pairs with links across different primary domains)
- Items in reading queue: N (High: N, Normal: N)
- Stubs awaiting graduation (confidence 0–1, 3+ sources): N
- Orphan concepts: N
- Orphan sources: N
```

---

## Quality Standards

- **Propose, don't decide.** The only things auto-fixed are: (1) missing index
  entries for files that clearly exist, and (2) stubs for dead links with
  overwhelming evidence. Everything else is flagged.
- **Be specific in flags.** "Concept X may be stale" is not useful. "Source
  [[bishop-pattern-recognition-2006]] (date_added 2026-04-01) covers variational
  inference with content that qualifies the claim in § Formal Statement" is useful.
- **Cross-domain connection gaps are actionable signals.** When flagging them,
  name the specific candidate concept — don't just say "check reinforcement-learning."

## Session End

After completing the health check and writing the report, commit with message:
```
[maintenance] health check YYYY-MM-DD
```
