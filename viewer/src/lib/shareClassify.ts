// Classify a shared payload (from the Android share sheet, via send-intent) into a
// PKIS ingest kind. The share target is deliberately GENERAL — a URL might be a code
// resource or an academic source, a shared file might be a paper PDF, plain text is a
// capture. The classifier only proposes a default; the review screen lets the user
// override the kind before committing.

export type IngestKind = 'resource' | 'source' | 'capture'

const RESOURCE_HOSTS = [
  'github.com', 'gitlab.com', 'bitbucket.org', 'pypi.org', 'npmjs.com',
  'crates.io', 'hex.pm', 'pkg.go.dev', 'readthedocs.io', 'readthedocs.org',
  'huggingface.co',
]
const SOURCE_HOSTS = [
  'arxiv.org', 'doi.org', 'semanticscholar.org', 'aclanthology.org',
  'openreview.net', 'dl.acm.org', 'ieeexplore.ieee.org', 'biorxiv.org',
  'pubmed.ncbi.nlm.nih.gov', 'nature.com', 'sciencedirect.com',
]

export interface ShareInput { url?: string; title?: string; text?: string; type?: string }
export interface Classification {
  kind: IngestKind
  url: string
  title: string
  resourceType?: string
}

function hostOf(u: string): string {
  try { return new URL(u).hostname.replace(/^www\./, '') } catch { return '' }
}

// Shares frequently arrive as text with a trailing URL — pull the first URL out.
function firstUrl(s: string): string {
  const m = s.match(/https?:\/\/[^\s]+/)
  return m ? m[0] : ''
}

function hostMatches(host: string, list: string[]): boolean {
  return list.some((h) => host === h || host.endsWith('.' + h))
}

function inferResourceType(host: string): string {
  if (['pypi.org', 'npmjs.com', 'crates.io', 'hex.pm', 'pkg.go.dev'].includes(host)) return 'library'
  if (host === 'readthedocs.io' || host === 'readthedocs.org') return 'documentation'
  if (host === 'huggingface.co') return 'dataset'
  return 'tool' // github/gitlab/bitbucket default
}

export function classifyShare(input: ShareInput): Classification {
  const url = (input.url || firstUrl(input.text || '') || '').trim()
  const title = (input.title || '').trim()
  const type = (input.type || '').toLowerCase()
  const host = hostOf(url)

  // A shared file (PDF) → source (document/paper).
  if (type.includes('pdf') || /\.pdf($|\?)/i.test(url)) {
    return { kind: 'source', url, title }
  }
  if (url) {
    if (hostMatches(host, RESOURCE_HOSTS)) {
      return { kind: 'resource', url, title, resourceType: inferResourceType(host) }
    }
    if (hostMatches(host, SOURCE_HOSTS)) {
      return { kind: 'source', url, title }
    }
    // Generic URL → default to source (article); the user can override to resource/capture.
    return { kind: 'source', url, title }
  }
  // No URL → plain-text capture.
  return { kind: 'capture', url: '', title: title || (input.text || '').slice(0, 80) }
}

export const RESOURCE_TYPES = ['library', 'tool', 'platform', 'dataset', 'documentation', 'service']
