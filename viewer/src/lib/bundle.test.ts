// @vitest-environment jsdom
/**
 * bundle.ts — the standalone export for writing assets.
 *
 * What matters here is that a document sent OUTSIDE PKIS reads correctly: the
 * nodes it cites travel with it, internal references point at the bundled
 * copies, and references that could not be bundled don't leave dead links.
 */
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { buildStandaloneHtml, buildAppendices } from './bundle'

vi.mock('./api', () => ({
  resolveSlugs: vi.fn(),
  getNode: vi.fn(),
}))
vi.mock('./katex', () => ({ renderMath: vi.fn() }))

import { resolveSlugs, getNode } from './api'

const NODES: Record<string, { title: string; body: string; sources?: string[] }> = {
  'coverage-driven-graph-traversal': {
    title: 'Coverage-Driven Graph Traversal',
    body: '## Definition\n\nTraverse by expected coverage gain.',
    sources: ['angelopoulos-ppi-plus-2023'],
  },
  'continuous-hardening-mixture-framework': {
    title: 'Continuous Hardening Mixture Framework',
    body: 'A mixture over hardening states.',
  },
}
const SOURCES: Record<string, { title: string; source_url: string }> = {
  'angelopoulos-ppi-plus-2023': {
    title: 'PPI++: Efficient Prediction-Powered Inference',
    source_url: 'https://arxiv.org/abs/2311.01453',
  },
}

beforeEach(() => {
  vi.mocked(resolveSlugs).mockImplementation(async (slugs: string[]) =>
    Object.fromEntries(slugs.map((s) => [
      s,
      NODES[s] ? `pkis:framework:${s}` : SOURCES[s] ? `pkis:source:${s}` : null,
    ]))
  )
  vi.mocked(getNode).mockImplementation(async (iri: string) => {
    const slug = iri.split(':').pop() as string
    if (NODES[slug]) {
      return {
        iri,
        content: NODES[slug].body,
        frontmatter: {
          title: NODES[slug].title,
          knowledge_type: 'framework',
          sources: NODES[slug].sources ?? [],
        },
      } as never
    }
    return { iri, content: '', frontmatter: SOURCES[slug] } as never
  })
})

// The two ways a writing asset cites a node: an inline wikilink, and the bare
// IRI its references table uses.
function article(): HTMLElement {
  const el = document.createElement('article')
  el.innerHTML = `
    <p>See <a class="wikilink" data-slug="coverage-driven-graph-traversal">traversal</a>.</p>
    <p>And <a class="wikilink" data-slug="never-written-node">a node that doesn't exist</a>.</p>
    <table><tr><td><code>pkis:framework:continuous-hardening-mixture-framework</code></td></tr></table>`
  return el
}

describe('buildAppendices', () => {
  it('bundles nodes cited as wikilinks and as bare IRIs, and drops unresolvable ones', async () => {
    const apps = await buildAppendices(article())
    expect(apps.map((a) => a.slug).sort()).toEqual([
      'continuous-hardening-mixture-framework',
      'coverage-driven-graph-traversal',
    ])
  })

  it('carries each node body and its external sources', async () => {
    const apps = await buildAppendices(article())
    const traversal = apps.find((a) => a.slug === 'coverage-driven-graph-traversal')!
    expect(traversal.html).toContain('expected coverage gain')
    expect(traversal.sources).toEqual([
      { label: 'PPI++: Efficient Prediction-Powered Inference',
        url: 'https://arxiv.org/abs/2311.01453' },
    ])
  })
})

describe('buildStandaloneHtml', () => {
  it('rewrites a bundled reference to an in-document anchor', async () => {
    const html = await buildStandaloneHtml('Position Paper', article())
    expect(html).toContain('href="#node-coverage-driven-graph-traversal"')
    expect(html).toContain('id="node-coverage-driven-graph-traversal"')
  })

  it('turns a reference it could not bundle into plain text, not a dead link', async () => {
    const html = await buildStandaloneHtml('Position Paper', article())
    expect(html).toContain("a node that doesn't exist")
    expect(html).not.toContain('never-written-node')
  })

  it('links the bare IRI in the references table to the bundled copy', async () => {
    const html = await buildStandaloneHtml('Position Paper', article())
    expect(html).toContain('href="#node-continuous-hardening-mixture-framework"')
  })

  it('emits external sources as real, followable URLs', async () => {
    const html = await buildStandaloneHtml('Position Paper', article())
    expect(html).toContain('https://arxiv.org/abs/2311.01453')
  })

  it('is self-contained: styles inlined, no external stylesheet for math-free text', async () => {
    const html = await buildStandaloneHtml('Position Paper', article())
    expect(html).toContain('<style>')
    expect(html).not.toContain('<link rel="stylesheet"')
  })

  it('keeps the document readable when it cites nothing at all', async () => {
    const bare = document.createElement('article')
    bare.innerHTML = '<p>No references here.</p>'
    const html = await buildStandaloneHtml('Bare', bare)
    expect(html).toContain('No references here.')
    expect(html).not.toContain('Appendix')
  })
})

describe('saveFile', () => {
  it('clicks an anchor that is attached to the document, and keeps the blob alive', async () => {
    const { saveFile } = await import('./bundle')
    const created: string[] = []
    const revoked: string[] = []
    vi.stubGlobal('URL', {
      createObjectURL: (_b: Blob) => { const u = `blob:stub-${created.length}`; created.push(u); return u },
      revokeObjectURL: (u: string) => { revoked.push(u) },
    })

    // Capture whether the anchor was in the document AT click time — a detached
    // anchor is the failure mode where nothing visible happens at all.
    let attachedAtClick: boolean | null = null
    let downloadAttr: string | null = null
    const click = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(function (this: HTMLAnchorElement) {
      attachedAtClick = document.body.contains(this)
      downloadAttr = this.getAttribute('download')
    })

    vi.useFakeTimers()
    try {
      saveFile('paper.html', '<p>hi</p>')
      expect(click).toHaveBeenCalledOnce()
      expect(attachedAtClick).toBe(true)
      expect(downloadAttr).toBe('paper.html')

      // Revoking synchronously can cancel the save before the bytes are read.
      expect(revoked).toEqual([])
      vi.runAllTimers()
      expect(revoked).toEqual(created)
    } finally {
      vi.useRealTimers()
      click.mockRestore()
      vi.unstubAllGlobals()
    }
  })

  it('leaves no stray anchor behind in the document', async () => {
    const { saveFile } = await import('./bundle')
    vi.stubGlobal('URL', { createObjectURL: () => 'blob:x', revokeObjectURL: () => {} })
    const click = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(() => {})
    try {
      const before = document.querySelectorAll('a').length
      saveFile('paper.html', 'x')
      expect(document.querySelectorAll('a').length).toBe(before)
    } finally {
      click.mockRestore()
      vi.unstubAllGlobals()
    }
  })
})
