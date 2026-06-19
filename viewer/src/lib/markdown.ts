import { marked } from 'marked'

marked.setOptions({
  gfm: true,
  breaks: true,
})

export function renderMarkdown(md: string): string {
  if (!md) return ''
  // Protect display math blocks from marked's escaping
  const placeholders: string[] = []
  let protected_ = md.replace(/\$\$[\s\S]+?\$\$/g, (m) => {
    placeholders.push(m)
    return `%%MATH_BLOCK_${placeholders.length - 1}%%`
  })
  protected_ = protected_.replace(/\$[^$\n]+?\$/g, (m) => {
    placeholders.push(m)
    return `%%MATH_INLINE_${placeholders.length - 1}%%`
  })

  // Obsidian-style internal links: [[slug]] or [[slug|label]] → an in-app anchor
  // (no href; the viewer resolves data-slug → IRI and navigates). marked doesn't
  // understand this syntax, so without this it renders as dead literal text.
  protected_ = protected_.replace(
    /\[\[([^\]|\n]+?)(?:\|([^\]\n]+?))?\]\]/g,
    (_m, slug, label) => {
      const s = String(slug).trim().replace(/"/g, '')
      const text = String(label ?? slug).trim()
      return `<a class="wikilink" data-slug="${s}">${text}</a>`
    }
  )

  let html = marked.parse(protected_) as string
  placeholders.forEach((p, i) => {
    html = html.replace(
      new RegExp(`%%MATH_(BLOCK|INLINE)_${i}%%`, 'g'),
      p
    )
  })
  return html
}
