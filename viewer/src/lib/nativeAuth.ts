// Native-app (Capacitor APK) sign-in. The packaged WebView is served from
// https://localhost, so the web cookie/redirect flow can't reach it. Instead we
// run a PKCE flow against the PKIS backend:
//
//   1. signInNative(): generate a PKCE verifier/challenge, open the WorkOS hosted
//      login in the SYSTEM BROWSER at /auth/native/start?challenge=...
//   2. After login the backend redirects to com.pkis.app://auth-callback?code=...
//      which the OS routes back to the app (handled in initNativeAuthListener).
//   3. onCallback(): POST {code, verifier} to /auth/native/token → access+refresh.
//   4. The access token rides in the Authorization header (authHeader); the refresh
//      token is persisted (Keystore-backed in increment 3) for silent re-auth.
//
// On web this module is inert (isNative() === false); useAuth keeps the cookie flow.
import { Capacitor } from '@capacitor/core'
import { Browser } from '@capacitor/browser'
import { App } from '@capacitor/app'
import { Preferences } from '@capacitor/preferences'
import { NativeBiometric } from '@capgo/capacitor-native-biometric'
import { API_BASE } from './base'

const REFRESH_KEY = 'pkis.native.refresh'   // Preferences fallback (no biometric hw)
const BIO_SERVER = 'pkis.native'            // Keystore credential key

// Tokens held in memory for the session. The access token is short-lived; the
// refresh token is loaded once (biometric-gated on launch) and reused for silent
// mid-session refreshes without re-prompting.
let accessToken: string | null = null
let refreshToken: string | null = null
// The verifier for an in-flight sign-in, kept until the deep link returns.
let pendingVerifier: string | null = null
// Guard so the deep-link listener is registered at most once.
let listenerRegistered = false

// ── Refresh-token storage (hardware Keystore when biometric is available, else
// Capacitor Preferences). Reads on launch are gated behind a biometric prompt. ──
async function biometricAvailable(): Promise<boolean> {
  try {
    return (await NativeBiometric.isAvailable()).isAvailable === true
  } catch {
    return false
  }
}

async function storeRefresh(token: string): Promise<void> {
  if (await biometricAvailable()) {
    try {
      await NativeBiometric.setCredentials({ username: 'pkis', password: token, server: BIO_SERVER })
      await Preferences.remove({ key: REFRESH_KEY })  // don't keep a plaintext copy
      return
    } catch {
      /* fall through to Preferences */
    }
  }
  await Preferences.set({ key: REFRESH_KEY, value: token })
}

// Load the stored refresh token. When `prompt` is true (launch restore), require a
// biometric check first; mid-session refreshes use the in-memory copy and never
// call this. Returns null if absent or the user cancels the prompt.
async function loadRefresh(prompt: boolean): Promise<string | null> {
  if (await biometricAvailable()) {
    try {
      if (prompt) {
        await NativeBiometric.verifyIdentity({
          reason: 'Unlock PKIS', title: 'PKIS', subtitle: 'Authenticate to continue',
        })
      }
      const c = await NativeBiometric.getCredentials({ server: BIO_SERVER })
      if (c?.password) return c.password
    } catch {
      return null  // no stored credential, or the user cancelled the prompt
    }
  }
  const { value } = await Preferences.get({ key: REFRESH_KEY })
  return value ?? null
}

async function clearRefresh(): Promise<void> {
  await Preferences.remove({ key: REFRESH_KEY })
  try {
    if (await biometricAvailable()) await NativeBiometric.deleteCredentials({ server: BIO_SERVER })
  } catch {
    /* best effort */
  }
}

export function isNative(): boolean {
  return Capacitor.isNativePlatform()
}

export function hasAccessToken(): boolean {
  return accessToken !== null
}

export function authHeader(): Record<string, string> {
  return accessToken ? { Authorization: `Bearer ${accessToken}` } : {}
}

// ── PKCE helpers (Web Crypto; the WebView is a secure context) ───────────────
function b64url(bytes: Uint8Array): string {
  let s = ''
  for (const b of bytes) s += String.fromCharCode(b)
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

function randomVerifier(): string {
  const a = new Uint8Array(32)
  crypto.getRandomValues(a)
  return b64url(a)
}

async function challengeOf(verifier: string): Promise<string> {
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(verifier))
  return b64url(new Uint8Array(digest))
}

// ── Sign-in ──────────────────────────────────────────────────────────────────
export async function signInNative(): Promise<void> {
  const verifier = randomVerifier()
  pendingVerifier = verifier
  const challenge = await challengeOf(verifier)
  await Browser.open({ url: `${API_BASE}/auth/native/start?challenge=${encodeURIComponent(challenge)}` })
}

async function onCallback(code: string): Promise<boolean> {
  const verifier = pendingVerifier
  pendingVerifier = null
  if (!verifier) return false
  try {
    const res = await fetch(`${API_BASE}/auth/native/token`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, verifier }),
    })
    if (!res.ok) return false
    const data = await res.json()
    accessToken = data.access_token
    refreshToken = data.refresh_token
    await storeRefresh(data.refresh_token)
    return true
  } catch {
    return false
  }
}

// Register the deep-link handler once at startup. `onSignedIn` fires after a
// successful token exchange so the app can refresh its auth state.
export function initNativeAuthListener(onSignedIn: () => void): void {
  if (!isNative() || listenerRegistered) return
  listenerRegistered = true
  App.addListener('appUrlOpen', async ({ url }) => {
    try {
      const u = new URL(url)
      const code = u.searchParams.get('code')
      if (!code) return // not our auth deep link (or an error= came back)
      await Browser.close().catch(() => {})
      if (await onCallback(code)) onSignedIn()
    } catch {
      /* ignore malformed / non-auth deep links */
    }
  })
}

// Rotate the in-memory refresh token for a fresh access+refresh pair. No biometric
// prompt — the refresh token was already unlocked at login or launch. A 401 means
// the refresh token is dead (expired/revoked): clear it so we stop looping.
async function rotate(): Promise<boolean> {
  if (!refreshToken) return false
  try {
    const res = await fetch(`${API_BASE}/auth/native/refresh`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh_token: refreshToken }),
    })
    if (!res.ok) {
      if (res.status === 401) {
        refreshToken = null
        accessToken = null
        await clearRefresh()
      }
      return false
    }
    const data = await res.json()
    accessToken = data.access_token
    refreshToken = data.refresh_token
    await storeRefresh(data.refresh_token)
    return true
  } catch {
    return false
  }
}

// Mid-session token heal (called by api.ts on a 401). Uses the in-memory refresh
// token; never prompts for biometrics.
export async function refreshAccessToken(): Promise<boolean> {
  return rotate()
}

// On launch: biometric-unlock the stored refresh token, then mint a fresh access
// token. Returns true if a session was restored.
export async function restoreNativeSession(): Promise<boolean> {
  if (!isNative()) return false
  const stored = await loadRefresh(true)   // biometric gate
  if (!stored) return false
  refreshToken = stored
  return rotate()
}

export async function signOutNative(): Promise<void> {
  try {
    await fetch(`${API_BASE}/auth/native/logout`, { method: 'POST', headers: authHeader() })
  } catch {
    /* best effort */
  }
  accessToken = null
  refreshToken = null
  await clearRefresh()
}
