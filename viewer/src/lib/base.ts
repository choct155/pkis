// Single source of truth for the API origin, shared by api.ts and nativeAuth.ts
// (kept in its own module so the two can both import it without a cycle).
//
// Web build talks to the same-origin backend ('/pkis-api', co-hosted by nginx).
// The native (Capacitor) build has no same-origin backend, so it injects the host
// root at build time via VITE_API_BASE_URL (see .env.example); we append the prefix.
export const API_BASE = (import.meta.env.VITE_API_BASE_URL ?? '') + '/pkis-api';
