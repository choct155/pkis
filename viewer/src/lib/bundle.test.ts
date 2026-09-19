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
  publishExport: vi.fn(),
}))
vi.mock('./katex', () => ({ renderMath: vi.fn() }))
vi.mock('./nativeAuth', () => ({ isNative: vi.fn(() => false) }))
vi.mock('./share', () => ({ shareLink: vi.fn() }))

import { resolveSlugs, getNode, publishExport } from './api'
import { isNative } from './nativeAuth'
import { shareLink } from './share'

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
  const stubUrl = () => {
    const created: string[] = [], revoked: string[] = []
    vi.stubGlobal('URL', {
      createObjectURL: () => { const u = `blob:stub-${created.length}`; created.push(u); return u },
      revokeObjectURL: (u: string) => { revoked.push(u) },
    })
    return { created, revoked }
  }

  it('uses the OS share sheet when the platform offers it — the only route that works in the Android app', async () => {
    const { saveFile } = await import('./bundle')
    const share = vi.fn().mockResolvedValue(undefined)
    vi.stubGlobal('navigator', { canShare: () => true, share })
    try {
      expect(await saveFile('paper.html', '<p>hi</p>')).toBe('shared')
      const arg = share.mock.calls[0][0]
      expect(arg.files[0].name).toBe('paper.html')
    } finally { vi.unstubAllGlobals() }
  })

  it('treats a dismissed share sheet as a choice, not a failure to retry as a download', async () => {
    const { saveFile } = await import('./bundle')
    const err = Object.assign(new Error('x'), { name: 'AbortError' })
    vi.stubGlobal('navigator', { canShare: () => true, share: vi.fn().mockRejectedValue(err) })
    const click = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(() => {})
    try {
      expect(await saveFile('paper.html', 'x')).toBe('cancelled')
      expect(click).not.toHaveBeenCalled()
    } finally { click.mockRestore(); vi.unstubAllGlobals() }
  })

  it('falls back to a download, from an attached anchor, keeping the blob alive', async () => {
    const { saveFile } = await import('./bundle')
    const { created, revoked } = stubUrl()
    vi.stubGlobal('navigator', { canShare: () => false })
    let attachedAtClick: boolean | null = null
    let downloadAttr: string | null = null
    const click = vi.spyOn(HTMLAnchorElement.prototype, 'click')
      .mockImplementation(function (this: HTMLAnchorElement) {
        attachedAtClick = document.body.contains(this)
        downloadAttr = this.getAttribute('download')
      })
    vi.useFakeTimers()
    try {
      expect(await saveFile('paper.html', '<p>hi</p>')).toBe('downloaded')
      expect(attachedAtClick).toBe(true)          // a detached anchor is silently ignored
      expect(downloadAttr).toBe('paper.html')
      expect(revoked).toEqual([])                 // revoking now can cancel the save
      vi.runAllTimers()
      expect(revoked).toEqual(created)
    } finally {
      vi.useRealTimers(); click.mockRestore(); vi.unstubAllGlobals()
    }
  })

  it('leaves no stray anchor behind in the document', async () => {
    const { saveFile } = await import('./bundle')
    stubUrl()
    vi.stubGlobal('navigator', { canShare: () => false })
    const click = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(() => {})
    try {
      const before = document.querySelectorAll('a').length
      await saveFile('paper.html', 'x')
      expect(document.querySelectorAll('a').length).toBe(before)
    } finally { click.mockRestore(); vi.unstubAllGlobals() }
  })
})


describe('deliverExport — getting the export to the user on each platform', () => {
  const afterNative = () => { vi.unstubAllGlobals(); vi.mocked(isNative).mockReturnValue(false) }

  it('publishes and shares a LINK in the native app, which cannot save files at all', async () => {
    const { deliverExport } = await import('./bundle')
    vi.mocked(isNative).mockReturnValue(true)
    vi.mocked(publishExport).mockResolvedValue('/pkis-api/export/paper-abc123.html')
    vi.mocked(shareLink).mockResolvedValue('shared')
    vi.stubGlobal('navigator', { canShare: () => false })
    const click = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(() => {})
    try {
      const r = await deliverExport('paper', 'Paper', '<p>x</p>')
      expect(r).toEqual({ how: 'shared', url: '/pkis-api/export/paper-abc123.html' })
      // The WebView silently ignores this, so it must never be attempted there.
      expect(click).not.toHaveBeenCalled()
      expect(vi.mocked(publishExport).mock.calls[0][0]).toBe('paper')
    } finally { click.mockRestore(); afterNative() }
  })

  it('reports a copied link when there is no share sheet to take it', async () => {
    const { deliverExport } = await import('./bundle')
    vi.mocked(isNative).mockReturnValue(true)
    vi.mocked(publishExport).mockResolvedValue('/pkis-api/export/p.html')
    vi.mocked(shareLink).mockResolvedValue('copied')
    vi.stubGlobal('navigator', { canShare: () => false })
    try {
      expect((await deliverExport('paper', 'Paper', 'x')).how).toBe('copied')
    } finally { afterNative() }
  })

  it('never claims success when publishing fails', async () => {
    const { deliverExport } = await import('./bundle')
    vi.mocked(isNative).mockReturnValue(true)
    vi.mocked(publishExport).mockRejectedValue(new Error('offline'))
    vi.stubGlobal('navigator', { canShare: () => false })
    try {
      expect((await deliverExport('paper', 'Paper', 'x')).how).toBe('failed')
    } finally { afterNative() }
  })

  it('downloads on the web instead of publishing anything', async () => {
    const { deliverExport } = await import('./bundle')
    vi.stubGlobal('URL', { createObjectURL: () => 'blob:x', revokeObjectURL: () => {} })
    vi.stubGlobal('navigator', { canShare: () => false })
    const click = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(() => {})
    vi.mocked(publishExport).mockClear()
    try {
      expect((await deliverExport('paper', 'Paper', 'x')).how).toBe('downloaded')
      expect(publishExport).not.toHaveBeenCalled()
    } finally { click.mockRestore(); vi.unstubAllGlobals() }
  })
})
