// Surface a link through the OS share sheet (Web Share API, great on Android),
// falling back to copying it to the clipboard. `path` is app-relative
// (e.g. "/app/?s=token"); we resolve it against the current origin.
export type ShareResult = 'shared' | 'copied' | 'cancelled' | 'failed'

export async function shareLink(path: string, title: string): Promise<ShareResult> {
  const url = new URL(path, window.location.origin).toString()
  if (typeof navigator !== 'undefined' && navigator.share) {
    try {
      await navigator.share({ title, url })
      return 'shared'
    } catch (e) {
      // User dismissed the sheet — not an error, don't then copy behind their back.
      if ((e as { name?: string })?.name === 'AbortError') return 'cancelled'
      // Otherwise fall through to clipboard.
    }
  }
  try {
    await navigator.clipboard.writeText(url)
    return 'copied'
  } catch {
    return 'failed'
  }
}
