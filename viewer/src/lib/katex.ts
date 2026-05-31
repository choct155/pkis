// KaTeX auto-render integration
// Uses the CDN-loaded auto-render since vite-plugin-pwa caches it

declare global {
  interface Window {
    renderMathInElement?: (el: Element, opts?: unknown) => void
  }
}

const KATEX_OPTS = {
  delimiters: [
    { left: '$$', right: '$$', display: true },
    { left: '$', right: '$', display: false },
  ],
  throwOnError: false,
}

export function renderMath(el: HTMLElement | null): void {
  if (!el) return
  // Use dynamic import with string literal to bypass TS module resolution for sub-path
  // Falls back to window global if not available
  const autoRenderPath = 'katex/dist/contrib/auto-render.js'
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  ;(import(/* @vite-ignore */ autoRenderPath) as Promise<any>)
    .then((mod) => {
      const render = mod.default ?? mod
      if (typeof render === 'function') render(el, KATEX_OPTS)
    })
    .catch(() => {
      window.renderMathInElement?.(el, KATEX_OPTS)
    })
}
