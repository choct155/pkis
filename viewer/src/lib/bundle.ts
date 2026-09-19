// Standalone HTML export for `format: writing` assets.
//
// A writing asset cites other PKIS nodes — as [[wikilinks]] and as bare
// `pkis:type:slug` IRIs in its references table — and those nodes cite external
// papers. Sending someone just the document leaves every one of those references
// dead: they have no PKIS access. So the export walks the document's references
// one level deep, renders each referenced node into the same file as an
// appendix, and rewrites internal links to in-document anchors. External sources
// become real URLs, since those a reader CAN follow.
//
// One level deep, deliberately: transitive closure would pull in most of the
// wiki and bury the argument the document is making.
import { getNode, resolveSlugs, publishExport } from './api'
import { renderMarkdown } from './markdown'
import { renderMath } from './katex'
import { isNative } from './nativeAuth'
import { shareLink } from './share'

const IRI_RE = /pkis:[a-z-]+:[a-z0-9][a-z0-9-]*/gi

export interface Appendix {
  slug: string
  title: string
  kind: string
  html: string
  sources: { label: string; url: string | null }[]
}

export const esc = (v: string) =>
  v.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')

// Markdown → HTML with math typeset, via a detached element (KaTeX walks the
// DOM, so the content has to be in one — it needn't be in the document).
function renderToHtml(md: string): string {
  const el = document.createElement('div')
  el.innerHTML = renderMarkdown(md)
  renderMath(el)
  return el.innerHTML
}

// Every node this document points at: [[wikilinks]] plus the bare IRIs the
// references table uses. Reading both means the export is complete whether or
// not a given document has been written with wikilinks.
function collectSlugs(root: HTMLElement): string[] {
  const out = new Set<string>()
  root.querySelectorAll<HTMLElement>('a.wikilink[data-slug]').forEach((a) => {
    const s = a.dataset.slug?.trim()
    if (s) out.add(s)
  })
  root.querySelectorAll('code').forEach((c) => {
    const found = (c.textContent || '').match(IRI_RE)
    found?.forEach((iri) => {
      const s = iri.split(':').pop()?.trim()
      if (s) out.add(s)
    })
  })
  return [...out]
}

const slugOf = (iri: string) => iri.split(':').pop() || iri
const titleCase = (s: string) => s.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())

export async function buildAppendices(root: HTMLElement): Promise<Appendix[]> {
  const slugs = collectSlugs(root)
  if (!slugs.length) return []

  const iriBySlug = await resolveSlugs(slugs)
  const referenced = slugs.filter((s) => iriBySlug[s])

  const nodes = await Promise.all(
    referenced.map(async (slug) => {
      try {
        return { slug, node: await getNode(iriBySlug[slug] as string) }
      } catch {
        return null   // a node we can't fetch is dropped, not fatal to the export
      }
    })
  )
  const fetched = nodes.filter((n): n is NonNullable<typeof n> => n !== null)

  // Resolve the papers those nodes cite, so the reader gets real, followable
  // links (arXiv, DOI) rather than bare slugs.
  const srcSlugs = [...new Set(
    fetched.flatMap((f) => (f.node.frontmatter?.sources as string[] | undefined) ?? [])
  )]
  const srcIri = srcSlugs.length ? await resolveSlugs(srcSlugs) : {}
  const srcMeta = new Map<string, { label: string; url: string | null }>()
  await Promise.all(
    srcSlugs.map(async (s) => {
      const iri = srcIri[s]
      if (!iri) return
      try {
        const fm = (await getNode(iri)).frontmatter as Record<string, unknown>
        const url = (fm.source_url as string) || (fm.doi as string) || null
        srcMeta.set(s, { label: (fm.title as string) || titleCase(s), url })
      } catch {
        /* skip a source we can't read */
      }
    })
  )

  return fetched.map(({ slug, node }) => {
    const fm = (node.frontmatter ?? {}) as Record<string, unknown>
    return {
      slug,
      title: (fm.title as string) || titleCase(slug),
      kind: (fm.knowledge_type as string) || slugOf(node.iri.split(':').slice(0, -1).join(':')),
      html: renderToHtml(node.content || ''),
      sources: (((fm.sources as string[]) ?? []).map((s) => srcMeta.get(s)).filter(Boolean)) as
        { label: string; url: string | null }[],
    }
  })
}

// Point internal references at the bundled copy. A reference we did not bundle
// becomes plain text: a dead link in a document sent outside PKIS is worse than
// no link, because it looks like something the reader failed to open.
function linkify(scope: HTMLElement, bundled: Map<string, Appendix>) {
  scope.querySelectorAll<HTMLAnchorElement>('a.wikilink[data-slug]').forEach((a) => {
    const app = bundled.get(a.dataset.slug || '')
    if (!app) {
      a.replaceWith(document.createTextNode(a.textContent || ''))
      return
    }
    a.removeAttribute('data-slug')
    a.setAttribute('href', `#node-${app.slug}`)
  })
  scope.querySelectorAll('code').forEach((c) => {
    const text = (c.textContent || '').trim()
    if (!/^pkis:/i.test(text)) return
    const app = bundled.get(slugOf(text))
    if (!app) return
    const a = document.createElement('a')
    a.setAttribute('href', `#node-${app.slug}`)
    c.replaceWith(a)
    a.appendChild(c)
  })
}

function appendixHtml(a: Appendix): string {
  const sources = a.sources.length
    ? `<p class="pk-sources"><strong>Sources:</strong> ${a.sources
        .map((s) => (s.url ? `<a href="${esc(s.url)}">${esc(s.label)}</a>` : esc(s.label)))
        .join(' · ')}</p>`
    : ''
  return `<section class="pk-node" id="node-${esc(a.slug)}">
<h2>${esc(a.title)}</h2>
<p class="pk-kind">${esc(a.kind)}</p>
${sources}
${a.html}
</section>`
}

// Deliberately independent of the app's theme: these documents get forwarded and
// printed, so they render light, on any device, with no network fetch.
const DOC_CSS = `
:root { color-scheme: light }
body { margin: 0; background: #fff; color: #1a1a1a;
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  -webkit-text-size-adjust: 100% }
.pk-wrap { max-width: 46rem; margin: 0 auto; padding: 3rem 1.5rem 6rem }
h1, h2, h3, h4 { line-height: 1.25; margin: 2.2em 0 .6em; font-weight: 650 }
h1 { font-size: 2rem; margin-top: 0 }
h2 { font-size: 1.4rem; padding-bottom: .3em; border-bottom: 1px solid #e5e5e5 }
h3 { font-size: 1.15rem }
h4 { font-size: 1rem }
p, ul, ol, blockquote, table, pre { margin: 0 0 1.1em }
ul, ol { padding-left: 1.4em }
li { margin: .3em 0 }
a { color: #0b5cad }
strong { font-weight: 650 }
blockquote { margin-left: 0; padding: .1em 0 .1em 1.1em; border-left: 3px solid #d8d8d8; color: #444 }
code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: .89em; background: #f4f4f5; padding: .15em .35em; border-radius: 3px }
pre { background: #f7f7f8; padding: 1em; border-radius: 6px; overflow-x: auto }
pre code { background: none; padding: 0 }
table { border-collapse: collapse; width: 100%; display: block; overflow-x: auto }
th, td { border: 1px solid #e0e0e0; padding: .5em .7em; text-align: left; vertical-align: top }
th { background: #f7f7f8; font-weight: 650 }
hr { border: 0; border-top: 1px solid #e5e5e5; margin: 2.4em 0 }
img { max-width: 100% }
.pk-appendix { margin-top: 4rem; border-top: 3px double #d8d8d8; padding-top: 2rem }
.pk-appendix > h2 { border: 0; font-size: 1.5rem }
.pk-lede { color: #555; font-size: .95rem }
.pk-toc { padding-left: 1.2em }
.pk-node { margin-top: 3rem; padding-top: 1.4rem; border-top: 1px solid #ececec }
.pk-kind { margin: -.4em 0 .9em; color: #777; font-size: .8rem;
  text-transform: uppercase; letter-spacing: .06em }
.pk-sources { font-size: .9rem; color: #444; background: #fafafa;
  border-left: 3px solid #e0e0e0; padding: .6em .9em; margin-bottom: 1.4em }
.pk-foot { margin-top: 4rem; padding-top: 1rem; border-top: 1px solid #e5e5e5;
  color: #777; font-size: .82rem }
@media print {
  .pk-wrap { max-width: none; padding: 0 }
  a { color: inherit }
  .pk-node, .pk-appendix { break-inside: auto }
}
`

export type SaveResult = 'shared' | 'downloaded' | 'cancelled' | 'failed' | 'unsupported'

/**
 * Hand a generated file to the user, by whichever route the platform actually
 * supports.
 *
 * The Android app is a Capacitor WebView with no DownloadListener, so a blob
 * `<a download>` there does nothing at all — no file, no error, no prompt. The
 * OS share sheet is the route that works natively (it can save to Files/Drive
 * or send the document onward), so try that first wherever it is offered.
 *
 * The download fallback has two details that decide whether it works at all,
 * and getting either wrong also looks like the button doing nothing:
 *  - the anchor must be IN the document when clicked; several browsers ignore
 *    a click on a detached one;
 *  - the object URL must outlive the click. Revoking it on the next line can
 *    cancel the save before the browser has read the blob, and the larger the
 *    file the more reliably the revoke wins that race.
 */
export async function saveFile(
  filename: string, content: string, type = 'text/html',
): Promise<SaveResult> {
  const file = new File([content], filename, { type })
  if (typeof navigator !== 'undefined' && navigator.canShare?.({ files: [file] })) {
    try {
      await navigator.share({ files: [file], title: filename })
      return 'shared'
    } catch (e) {
      // Dismissing the sheet is a choice, not a failure — don't then quietly
      // download the file behind the user's back.
      if ((e as { name?: string })?.name === 'AbortError') return 'cancelled'
      // Anything else: fall through and try a plain download.
    }
  }
  // The native WebView has no download handler: the click below would do
  // nothing and we'd have no way to tell, so never claim a save we can't make.
  if (isNative()) return 'unsupported'
  try {
    const url = URL.createObjectURL(new Blob([content], { type }))
    const a = document.createElement('a')
    a.href = url
    a.download = filename
    a.rel = 'noopener'
    a.style.display = 'none'
    document.body.appendChild(a)
    a.click()
    a.remove()
    setTimeout(() => URL.revokeObjectURL(url), 30_000)
    return 'downloaded'
  } catch {
    return 'failed'
  }
}

export type DeliverResult = 'shared' | 'copied' | 'downloaded' | 'cancelled' | 'failed'

/**
 * Get a finished export to the user by whatever route their platform actually
 * supports, and never report success we cannot stand behind.
 *
 * Order matters. A real file is best where it can be had, so the OS share sheet
 * and the desktop download come first. Where neither exists — the Android app —
 * the export is published to a public URL and the LINK is shared instead. That
 * is also the better artifact for this document's purpose: a recipient with no
 * PKIS account can open a link on any device, where an 83KB attachment is
 * something they have to keep.
 */
export async function deliverExport(
  slug: string, title: string, html: string,
): Promise<{ how: DeliverResult; url?: string }> {
  const saved = await saveFile(`${slug}.html`, html)
  if (saved !== 'unsupported') return { how: saved as DeliverResult }

  try {
    const url = await publishExport(slug, html)
    const shared = await shareLink(url, title)
    if (shared === 'failed') return { how: 'failed', url }
    return { how: shared === 'shared' ? 'shared' : shared === 'copied' ? 'copied' : 'cancelled', url }
  } catch {
    return { how: 'failed' }
  }
}

/** Render the open document plus its referenced nodes into one standalone file. */
export async function buildStandaloneHtml(title: string, root: HTMLElement): Promise<string> {
  const appendices = await buildAppendices(root)
  const bundled = new Map(appendices.map((a) => [a.slug, a]))

  const body = document.createElement('div')
  body.className = 'pk-wrap'

  const main = document.createElement('article')
  main.innerHTML = root.innerHTML
  body.appendChild(main)

  if (appendices.length) {
    const appendix = document.createElement('section')
    appendix.className = 'pk-appendix'
    appendix.innerHTML = `<h2>Appendix — Referenced PKIS Nodes</h2>
<p class="pk-lede">The nodes this document cites, included in full so it can be read
without access to PKIS. Links above jump to these; each node lists its own sources.</p>
<ol class="pk-toc">${appendices
      .map((a) => `<li><a href="#node-${esc(a.slug)}">${esc(a.title)}</a></li>`)
      .join('')}</ol>
${appendices.map(appendixHtml).join('\n')}`
    body.appendChild(appendix)
  }

  linkify(body, bundled)

  const foot = document.createElement('p')
  foot.className = 'pk-foot'
  foot.textContent = `Exported from PKIS on ${new Date().toISOString().slice(0, 10)}`
    + (appendices.length ? ` · ${appendices.length} referenced node(s) included` : '')
  body.appendChild(foot)

  // KaTeX's CSS and fonts can't be inlined, so when the bundle actually contains
  // math, link the app's stylesheets absolutely: equations typeset for a reader
  // who is online and degrade to plain markup for one who isn't. A math-free
  // document — the common case — stays fully self-contained.
  const sheets = body.querySelector('.katex')
    ? Array.from(document.querySelectorAll<HTMLLinkElement>('link[rel="stylesheet"]'))
        .map((l) => `<link rel="stylesheet" href="${esc(l.href)}">`).join('')
    : ''

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
${sheets}
<style>${DOC_CSS}</style>
</head>
<body>${body.outerHTML}</body>
</html>`
}
